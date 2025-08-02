# Create API routes
os.makedirs('src/pages/api/auth', exist_ok=True)
os.makedirs('src/pages/api/ai', exist_ok=True)
os.makedirs('src/pages/api/media', exist_ok=True)

# NextAuth configuration
nextauth_api = '''import NextAuth from "next-auth"
import { authOptions } from "@/lib/auth"

export default NextAuth(authOptions)'''

with open('src/pages/api/auth/[...nextauth].ts', 'w') as f:
    f.write(nextauth_api)

# Media analysis API
analyze_media_api = '''import { NextApiRequest, NextApiResponse } from 'next';
import { getServerSession } from 'next-auth/next';
import { authOptions } from '@/lib/auth';
import { openaiService } from '@/services/ai/openai';
import { pineconeService } from '@/services/database/pinecone';
import { prisma } from '@/lib/db';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const session = await getServerSession(req, res, authOptions);
    if (!session?.user?.id) {
      return res.status(401).json({ message: 'Unauthorized' });
    }

    const { mediaUrl, mediaId } = req.body;

    if (!mediaUrl) {
      return res.status(400).json({ message: 'Media URL is required' });
    }

    // Analyze media with OpenAI Vision
    const analysis = await openaiService.analyzeMedia(mediaUrl);

    // Generate embeddings for trend matching
    const embedding = await openaiService.generateEmbedding(
      JSON.stringify(analysis)
    );

    // Find matching trends
    const matchingTrends = await pineconeService.findSimilarTrends(
      embedding,
      5 // top 5 matches
    );

    // Save analysis to database (would require Prisma schema)
    // const savedAnalysis = await prisma.mediaAnalysis.create({...});

    res.status(200).json({
      analysis: {
        ...analysis,
        id: `analysis_${Date.now()}`,
        mediaId,
        userId: session.user.id,
        embedding,
        matchingTrends,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      matchingTrends,
    });
  } catch (error) {
    console.error('Error analyzing media:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
}'''

with open('src/pages/api/ai/analyze-media.ts', 'w') as f:
    f.write(analyze_media_api)

# Caption generation API
caption_generation_api = '''import { NextApiRequest, NextApiResponse } from 'next';
import { getServerSession } from 'next-auth/next';
import { authOptions } from '@/lib/auth';
import { openaiService } from '@/services/ai/openai';
import { CaptionRequest } from '@/types';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const session = await getServerSession(req, res, authOptions);
    if (!session?.user?.id) {
      return res.status(401).json({ message: 'Unauthorized' });
    }

    const captionRequest: CaptionRequest = req.body;

    if (!captionRequest.mediaAnalysis || !captionRequest.platform) {
      return res.status(400).json({ message: 'Media analysis and platform are required' });
    }

    // Generate captions using OpenAI
    const captions = await openaiService.generateCaption(captionRequest);

    // Format response with metadata
    const formattedCaptions = captions.map((caption, index) => ({
      id: `caption_${Date.now()}_${index}`,
      text: caption,
      platform: captionRequest.platform,
      tone: captionRequest.tone,
      characterCount: caption.length,
      hashtags: caption.match(/#\\w+/g) || [],
      createdAt: new Date(),
    }));

    res.status(200).json({
      success: true,
      captions: formattedCaptions,
    });
  } catch (error) {
    console.error('Error generating captions:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
}'''

with open('src/pages/api/ai/generate-caption.ts', 'w') as f:
    f.write(caption_generation_api)

# Media upload API
media_upload_api = '''import { NextApiRequest, NextApiResponse } from 'next';
import { getServerSession } from 'next-auth/next';
import { authOptions } from '@/lib/auth';
import formidable from 'formidable';
import { cloudinaryService } from '@/services/storage/cloudinary';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  try {
    const session = await getServerSession(req, res, authOptions);
    if (!session?.user?.id) {
      return res.status(401).json({ message: 'Unauthorized' });
    }

    const form = formidable({
      maxFileSize: 100 * 1024 * 1024, // 100MB
      multiples: true,
    });

    const [fields, files] = await form.parse(req);
    
    const uploadedFiles = Array.isArray(files.file) ? files.file : [files.file];
    const results = [];

    for (const file of uploadedFiles) {
      if (!file) continue;

      // Upload to Cloudinary
      const url = await cloudinaryService.uploadFromUrl(file.filepath);
      
      // Save file metadata to database (would require Prisma schema)
      const mediaFile = {
        id: `media_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
        userId: session.user.id,
        filename: file.newFilename || file.originalFilename || 'unnamed',
        originalName: file.originalFilename || 'unnamed',
        mimeType: file.mimetype || 'application/octet-stream',
        size: file.size,
        url,
        thumbnailUrl: cloudinaryService.generateThumbnail(url),
        createdAt: new Date(),
        updatedAt: new Date(),
      };

      results.push(mediaFile);
    }

    res.status(200).json({
      success: true,
      files: results,
    });
  } catch (error) {
    console.error('Error uploading media:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
}'''

with open('src/pages/api/media/upload.ts', 'w') as f:
    f.write(media_upload_api)

print("Created API routes for authentication, AI analysis, and media upload")