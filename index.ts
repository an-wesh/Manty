// User and Authentication Types
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
}