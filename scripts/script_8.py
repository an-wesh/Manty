# Create storage service - Cloudinary
os.makedirs('src/services/storage', exist_ok=True)

cloudinary_service = '''import { v2 as cloudinary } from 'cloudinary';

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

export const cloudinaryService = new CloudinaryService();'''

with open('src/services/storage/cloudinary.ts', 'w') as f:
    f.write(cloudinary_service)

# Create custom React hooks
os.makedirs('src/hooks', exist_ok=True)

use_upload_hook = '''import { useState, useCallback } from 'react';
import { cloudinaryService } from '@/services/storage/cloudinary';

interface UseUploadOptions {
  onProgress?: (progress: number) => void;
  onComplete?: (url: string) => void;
  onError?: (error: Error) => void;
}

export function useUpload(options: UseUploadOptions = {}) {
  const [isUploading, setIsUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [error, setError] = useState<Error | null>(null);

  const uploadFile = useCallback(async (
    file: File,
    progressCallback?: (progress: number) => void
  ): Promise<string> => {
    setIsUploading(true);
    setError(null);
    setUploadProgress(0);

    try {
      const url = await cloudinaryService.uploadFile(file, (progress) => {
        setUploadProgress(progress);
        progressCallback?.(progress);
        options.onProgress?.(progress);
      });

      options.onComplete?.(url);
      return url;
    } catch (err) {
      const error = err instanceof Error ? err : new Error('Upload failed');
      setError(error);
      options.onError?.(error);
      throw error;
    } finally {
      setIsUploading(false);
    }
  }, [options]);

  const uploadMultiple = useCallback(async (
    files: File[]
  ): Promise<string[]> => {
    const urls: string[] = [];
    
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const url = await uploadFile(file, (progress) => {
        const totalProgress = ((i + progress / 100) / files.length) * 100;
        setUploadProgress(totalProgress);
      });
      urls.push(url);
    }
    
    return urls;
  }, [uploadFile]);

  const reset = useCallback(() => {
    setIsUploading(false);
    setUploadProgress(0);
    setError(null);
  }, []);

  return {
    uploadFile,
    uploadMultiple,
    isUploading,
    uploadProgress,
    error,
    reset,
  };
}'''

with open('src/hooks/useUpload.ts', 'w') as f:
    f.write(use_upload_hook)

# Create useAuth hook
use_auth_hook = '''import { useSession, signIn, signOut } from 'next-auth/react';
import { User } from '@/types';

export function useAuth() {
  const { data: session, status } = useSession();

  const user: User | null = session?.user ? {
    id: session.user.id,
    email: session.user.email || '',
    name: session.user.name || undefined,
    image: session.user.image || undefined,
    createdAt: new Date(),
    updatedAt: new Date(),
  } : null;

  return {
    user,
    isLoading: status === 'loading',
    isAuthenticated: status === 'authenticated',
    signIn,
    signOut,
  };
}'''

with open('src/hooks/useAuth.ts', 'w') as f:
    f.write(use_auth_hook)

print("Created storage service and custom React hooks")