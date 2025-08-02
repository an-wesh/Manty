# Create authentication configuration
os.makedirs('src/lib', exist_ok=True)

auth_ts = '''import { NextAuthOptions } from "next-auth";
import { PrismaAdapter } from "@auth/prisma-adapter";
import InstagramProvider from "next-auth/providers/instagram";
import FacebookProvider from "next-auth/providers/facebook";
import GoogleProvider from "next-auth/providers/google";
import { prisma } from "./db";

export const authOptions: NextAuthOptions = {
  adapter: PrismaAdapter(prisma),
  providers: [
    InstagramProvider({
      clientId: process.env.INSTAGRAM_CLIENT_ID!,
      clientSecret: process.env.INSTAGRAM_CLIENT_SECRET!,
      authorization: {
        params: {
          scope: "user_profile,user_media"
        }
      }
    }),
    FacebookProvider({
      clientId: process.env.FACEBOOK_APP_ID!,
      clientSecret: process.env.FACEBOOK_APP_SECRET!,
      authorization: {
        params: {
          scope: "pages_show_list,pages_read_engagement,instagram_basic,instagram_content_publish"
        }
      }
    }),
    GoogleProvider({
      clientId: process.env.YOUTUBE_CLIENT_ID!,
      clientSecret: process.env.YOUTUBE_CLIENT_SECRET!,
      authorization: {
        params: {
          scope: "https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube.upload"
        }
      }
    }),
  ],
  callbacks: {
    async session({ session, user }) {
      session.user.id = user.id;
      return session;
    },
    async jwt({ token, account }) {
      if (account) {
        token.accessToken = account.access_token;
        token.provider = account.provider;
      }
      return token;
    },
  },
  pages: {
    signIn: "/auth/signin",
    error: "/auth/error",
  },
  secret: process.env.NEXTAUTH_SECRET,
};'''

with open('src/lib/auth.ts', 'w') as f:
    f.write(auth_ts)

# Create database configuration
db_ts = '''import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined;
};

export const prisma = globalForPrisma.prisma ?? new PrismaClient();

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;'''

with open('src/lib/db.ts', 'w') as f:
    f.write(db_ts)

# Create constants
constants_ts = '''export const PLATFORM_SPECS = {
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
} as const;'''

with open('src/lib/constants.ts', 'w') as f:
    f.write(constants_ts)

print("Created authentication, database, and constants configuration")