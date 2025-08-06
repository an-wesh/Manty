export const PLATFORM_SPECS = {
  instagram: {
    aspectRatios: ['1:1', '4:5', '9:16'],
    maxCaptionLength: 2200,
    maxHashtags: 30,
    recommendedHashtags: 11,
    supportedFormats: ['jpg', 'png', 'mp4', 'mov']
  },
  tiktok: {
    aspectRatios: ['9:16'],
    maxCaptionLength: 300,
    maxHashtags: 100,
    recommendedHashtags: 5,
    supportedFormats: ['mp4', 'mov', 'avi']
  },
  youtube: {
    aspectRatios: ['16:9', '9:16'],
    maxTitleLength: 100,
    maxDescriptionLength: 5000,
    recommendedTags: 15,
    supportedFormats: ['mp4', 'mov', 'avi', 'wmv']
  },
  facebook: {
    aspectRatios: ['16:9', '1:1', '4:5'],
    maxCaptionLength: 63206,
    maxHashtags: 30,
    recommendedHashtags: 5,
    supportedFormats: ['jpg', 'png', 'mp4', 'mov']
  }
} as const;

export const MOOD_COLORS = {
  happy: '#FFD700',
  energetic: '#FF6B35',
  calm: '#4A90E2',
  peaceful: '#7ED321',
  mysterious: '#9013FE',
  romantic: '#E91E63',
  nostalgic: '#8D6E63',
  dramatic: '#212121'
} as const;

export const TREND_CATEGORIES = [
  'lifestyle',
  'fashion',
  'beauty',
  'food',
  'travel',
  'fitness',
  'technology',
  'art',
  'music',
  'comedy',
  'education',
  'business'
] as const;

export const CONFIDENCE_THRESHOLDS = {
  HIGH: 0.8,
  MEDIUM: 0.6,
  LOW: 0.4
} as const;

export const FILE_UPLOAD_LIMITS = {
  maxFileSize: 100 * 1024 * 1024, // 100MB
  maxFiles: 10,
  allowedTypes: ['image/jpeg', 'image/png', 'image/webp', 'video/mp4', 'video/mov']
} as const;