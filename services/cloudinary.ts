import { v2 as cloudinary } from 'cloudinary';

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET,
});

export class CloudinaryService {
  async uploadFile(
    file: File, 
    progressCallback?: (progress: number) => void
  ): Promise<string> {
    return new Promise((resolve, reject) => {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('upload_preset', 'manty_uploads'); // You need to create this preset

      const xhr = new XMLHttpRequest();

      xhr.upload.onprogress = (event) => {
        if (event.lengthComputable) {
          const progress = (event.loaded / event.total) * 100;
          progressCallback?.(progress);
        }
      };

      xhr.onload = () => {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          resolve(response.secure_url);
        } else {
          reject(new Error('Upload failed'));
        }
      };

      xhr.onerror = () => reject(new Error('Upload failed'));

      xhr.open('POST', `https://api.cloudinary.com/v1_1/${process.env.CLOUDINARY_CLOUD_NAME}/upload`);
      xhr.send(formData);
    });
  }

  async uploadFromUrl(url: string, folder?: string): Promise<string> {
    try {
      const result = await cloudinary.uploader.upload(url, {
        folder: folder || 'manty',
        resource_type: 'auto',
      });

      return result.secure_url;
    } catch (error) {
      console.error('Error uploading from URL:', error);
      throw new Error('Failed to upload from URL');
    }
  }

  async deleteFile(publicId: string): Promise<void> {
    try {
      await cloudinary.uploader.destroy(publicId);
    } catch (error) {
      console.error('Error deleting file:', error);
      throw new Error('Failed to delete file');
    }
  }

  async generateThumbnail(publicId: string): Promise<string> {
    return cloudinary.url(publicId, {
      width: 300,
      height: 300,
      crop: 'fill',
      quality: 'auto',
      format: 'webp'
    });
  }

  getOptimizedUrl(publicId: string, options?: any): string {
    return cloudinary.url(publicId, {
      quality: 'auto',
      format: 'auto',
      ...options
    });
  }
}

export const cloudinaryService = new CloudinaryService();