import { useState, useCallback } from 'react';
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
}