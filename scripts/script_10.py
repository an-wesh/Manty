# Create React components
os.makedirs('src/components/upload', exist_ok=True)
os.makedirs('src/components/common', exist_ok=True)

# File uploader component
file_uploader = '''\'use client\';

import React, { useCallback, useState } from \'react\';
import { useDropzone } from \'react-dropzone\';
import { Upload, X, FileImage, FileVideo } from \'lucide-react\';
import { Button } from \'@/components/ui/button\';
import { Progress } from \'@/components/ui/progress\';
import { Card } from \'@/components/ui/card\';
import { useUpload } from \'@/hooks/useUpload\';
import { formatFileSize } from \'@/lib/utils\';

interface FileUploaderProps {
  onUploadComplete?: (files: UploadedFile[]) => void;
  maxFiles?: number;
  acceptedTypes?: string[];
}

interface UploadedFile {
  id: string;
  name: string;
  size: number;
  type: string;
  url: string;
  progress: number;
  status: \'uploading\' | \'completed\' | \'error\';
}

export function FileUploader({ 
  onUploadComplete, 
  maxFiles = 10,
  acceptedTypes = [\'image/*\', \'video/*\']
}: FileUploaderProps) {
  const [files, setFiles] = useState<UploadedFile[]>([]);
  const { uploadFile } = useUpload();

  const onDrop = useCallback(async (acceptedFiles: File[]) => {
    const newFiles: UploadedFile[] = acceptedFiles.map(file => ({
      id: Math.random().toString(36).substr(2, 9),
      name: file.name,
      size: file.size,
      type: file.type,
      url: \'\',
      progress: 0,
      status: \'uploading\' as const,
    }));

    setFiles(prev => [...prev, ...newFiles]);

    // Upload files one by one
    for (let i = 0; i < acceptedFiles.length; i++) {
      const file = acceptedFiles[i];
      const fileId = newFiles[i].id;

      try {
        const uploadedUrl = await uploadFile(file, (progress) => {
          setFiles(prev => 
            prev.map(f => 
              f.id === fileId 
                ? { ...f, progress }
                : f
            )
          );
        });

        setFiles(prev => 
          prev.map(f => 
            f.id === fileId 
              ? { ...f, url: uploadedUrl, status: \'completed\', progress: 100 }
              : f
          )
        );
      } catch (error) {
        setFiles(prev => 
          prev.map(f => 
            f.id === fileId 
              ? { ...f, status: \'error\' }
              : f
          )
        );
      }
    }

    const completedFiles = files.filter(f => f.status === \'completed\');
    onUploadComplete?.(completedFiles);
  }, [files, uploadFile, onUploadComplete]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: acceptedTypes.reduce((acc, type) => ({ ...acc, [type]: [] }), {}),
    maxFiles,
  });

  const removeFile = (fileId: string) => {
    setFiles(prev => prev.filter(f => f.id !== fileId));
  };

  const getFileIcon = (type: string) => {
    if (type.startsWith(\'image/\')) return <FileImage className="h-8 w-8" />;
    if (type.startsWith(\'video/\')) return <FileVideo className="h-8 w-8" />;
    return <Upload className="h-8 w-8" />;
  };

  return (
    <div className="w-full space-y-4">
      {/* Dropzone */}
      <Card
        {...getRootProps()}
        className={`border-2 border-dashed p-8 text-center cursor-pointer transition-colors ${
          isDragActive 
            ? \'border-primary bg-primary/5\' 
            : \'border-gray-300 hover:border-primary/50\'
        }`}
      >
        <input {...getInputProps()} />
        <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
        <p className="text-lg font-medium text-gray-600 mb-2">
          {isDragActive ? \'Drop files here\' : \'Drag & drop files here\'}
        </p>
        <p className="text-sm text-gray-500 mb-4">
          Or click to browse (max {maxFiles} files)
        </p>
        <Button variant="outline">
          Choose Files
        </Button>
      </Card>

      {/* File List */}
      {files.length > 0 && (
        <div className="space-y-2">
          <h3 className="font-medium text-gray-700">Uploaded Files</h3>
          {files.map((file) => (
            <Card key={file.id} className="p-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  {getFileIcon(file.type)}
                  <div>
                    <p className="font-medium text-sm">{file.name}</p>
                    <p className="text-xs text-gray-500">
                      {formatFileSize(file.size)}
                    </p>
                  </div>
                </div>
                
                <div className="flex items-center space-x-2">
                  {file.status === \'uploading\' && (
                    <div className="w-24">
                      <Progress value={file.progress} className="h-2" />
                    </div>
                  )}
                  
                  <div className={`text-xs px-2 py-1 rounded-full ${
                    file.status === \'completed\' 
                      ? \'bg-green-100 text-green-700\'
                      : file.status === \'error\'
                      ? \'bg-red-100 text-red-700\'
                      : \'bg-blue-100 text-blue-700\'
                  }`}>
                    {file.status}
                  </div>
                  
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => removeFile(file.id)}
                  >
                    <X className="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}'''

with open('src/components/upload/FileUploader.tsx', 'w') as f:
    f.write(file_uploader)

# Header component
header_component = '''\'use client\';

import React from \'react\';
import Link from \'next/link\';
import { useAuth } from \'@/hooks/useAuth\';
import { Button } from \'@/components/ui/button\';
import { User, LogOut, Settings } from \'lucide-react\';

export function Header() {
  const { user, isAuthenticated, signIn, signOut } = useAuth();

  return (
    <header className="bg-white border-b border-gray-200 px-4 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center space-x-8">
          <Link href="/" className="text-2xl font-bold text-primary">
            Manty
          </Link>
          
          {isAuthenticated && (
            <nav className="flex space-x-6">
              <Link href="/dashboard" className="text-gray-600 hover:text-primary">
                Dashboard
              </Link>
              <Link href="/upload" className="text-gray-600 hover:text-primary">
                Upload
              </Link>
              <Link href="/trends" className="text-gray-600 hover:text-primary">
                Trends
              </Link>
              <Link href="/projects" className="text-gray-600 hover:text-primary">
                Projects
              </Link>
            </nav>
          )}
        </div>

        <div className="flex items-center space-x-4">
          {isAuthenticated ? (
            <>
              <div className="flex items-center space-x-2">
                <User className="h-5 w-5 text-gray-500" />
                <span className="text-sm text-gray-700">{user?.name || user?.email}</span>
              </div>
              <Button variant="outline" size="sm" onClick={() => signOut()}>
                <LogOut className="h-4 w-4 mr-2" />
                Sign Out
              </Button>
            </>
          ) : (
            <Button onClick={() => signIn()}>
              Sign In
            </Button>
          )}
        </div>
      </div>
    </header>
  );
}'''

with open('src/components/common/Header.tsx', 'w') as f:
    f.write(header_component)

print("Created React components for file upload and header")