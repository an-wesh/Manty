# Create core TypeScript types
types_index = '''// User and Authentication Types
export interface User {
  id: string;
  email: string;
  name?: string;
  image?: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface Session {
  user: User;
  expires: string;
}

// Media Types
export interface MediaFile {
  id: string;
  userId: string;
  filename: string;
  originalName: string;
  mimeType: string;
  size: number;
  url: string;
  thumbnailUrl?: string;
  metadata?: Record<string, any>;
  createdAt: Date;
  updatedAt: Date;
}

// Analysis Types
export interface MediaAnalysis {
  id: string;
  mediaId: string;
  userId: string;
  mood: string;
  moodConfidence: number;
  sceneType: string;
  sceneConfidence: number;
  colorPalette: string[];
  objects: string[];
  composition: string;
  style: string;
  lighting: string;
  emotions: string[];
  embedding?: number[];
  matchingTrends?: TrendMatch[];
  createdAt: Date;
  updatedAt: Date;
}

// Trend Types
export interface Trend {
  id: string;
  name: string;
  category: string;
  platforms: Platform[];
  popularity: number;
  hashtags: string[];
  colors: string[];
  mood: string;
  description: string;
  embedding?: number[];
  isActive: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface TrendMatch {
  trendId: string;
  trend?: Trend;
  score: number;
  compatibilityReasons: string[];
}

// Platform Types
export type Platform = 'instagram' | 'tiktok' | 'facebook' | 'youtube' | 'twitter' | 'pinterest';

export interface PlatformSpec {
  platform: Platform;
  aspectRatios: string[];
  maxCaptionLength: number;
  maxHashtags: number;
  recommendedHashtags: number;
  supportedFormats: string[];
}

// Project Types
export interface Project {
  id: string;
  userId: string;
  name: string;
  description?: string;
  platform: Platform;
  status: 'draft' | 'in_progress' | 'completed' | 'archived';
  mediaFiles: MediaFile[];
  analyses: MediaAnalysis[];
  captions: GeneratedCaption[];
  thumbnail?: string;
  createdAt: Date;
  updatedAt: Date;
}

// Caption Types
export interface CaptionRequest {
  mediaAnalysis: MediaAnalysis;
  platform: Platform;
  tone: 'casual' | 'professional' | 'funny' | 'inspirational' | 'promotional';
  targetAudience?: string;
  count?: number;
  includeHashtags?: boolean;
  maxLength?: number;
}

export interface GeneratedCaption {
  id: string;
  projectId?: string;
  mediaId: string;
  platform: Platform;
  text: string;
  hashtags: string[];
  tone: string;
  characterCount: number;
  engagementScore?: number;
  createdAt: Date;
}

// API Response Types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T = any> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNext: boolean;
    hasPrev: boolean;
  };
}

// Component Props Types
export interface ComponentProps {
  className?: string;
  children?: React.ReactNode;
}'''

with open('src/types/index.ts', 'w') as f:
    f.write(types_index)

# Create utility functions
utils_ts = '''import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const formatFileSize = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

export const formatDate = (date: Date): string => {
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
};

export const generateId = (): string => {
  return Math.random().toString(36).substr(2, 9);
};

export const sleep = (ms: number): Promise<void> => {
  return new Promise(resolve => setTimeout(resolve, ms));
};

export const debounce = <T extends (...args: any[]) => any>(
  func: T,
  wait: number
): ((...args: Parameters<T>) => void) => {
  let timeout: NodeJS.Timeout;
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(null, args), wait);
  };
};

export const validateEmail = (email: string): boolean => {
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  return emailRegex.test(email);
};

export const truncateText = (text: string, maxLength: number): string => {
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength) + '...';
};

export const getColorPalette = (colors: string[]): string[] => {
  return colors.slice(0, 5); // Limit to 5 colors
};

export const calculateConfidenceColor = (confidence: number): string => {
  if (confidence >= 0.8) return 'text-green-600';
  if (confidence >= 0.6) return 'text-yellow-600';
  return 'text-red-600';
};'''

with open('src/lib/utils.ts', 'w') as f:
    f.write(utils_ts)

print("Created core TypeScript types and utility functions")