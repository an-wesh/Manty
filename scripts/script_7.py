# Create service layer - OpenAI integration
os.makedirs('src/services/ai', exist_ok=True)

openai_service = '''import OpenAI from 'openai';
import { MediaAnalysis, CaptionRequest } from '@/types';

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export class OpenAIService {
  async analyzeMedia(imageUrl: string): Promise<MediaAnalysis> {
    try {
      const response = await openai.chat.completions.create({
        model: "gpt-4-vision-preview",
        messages: [
          {
            role: "user",
            content: [
              {
                type: "text",
                text: `Analyze this image and provide a detailed analysis in JSON format with the following structure:
                {
                  "mood": "string",
                  "moodConfidence": number,
                  "sceneType": "string", 
                  "sceneConfidence": number,
                  "colorPalette": ["hex codes"],
                  "objects": ["detected objects"],
                  "composition": "string",
                  "style": "string",
                  "lighting": "string",
                  "emotions": ["detected emotions"]
                }`
              },
              {
                type: "image_url",
                image_url: {
                  url: imageUrl,
                },
              },
            ],
          }
        ],
        max_tokens: 1000,
      });

      const analysisText = response.choices[0].message.content;
      return JSON.parse(analysisText || '{}');
    } catch (error) {
      console.error('Error analyzing media:', error);
      throw new Error('Failed to analyze media');
    }
  }

  async generateCaption(request: CaptionRequest): Promise<string[]> {
    try {
      const prompt = `Generate ${request.count || 3} engaging social media captions for ${request.platform} with the following requirements:
      - Tone: ${request.tone}
      - Target audience: ${request.targetAudience || 'general'}
      - Include relevant hashtags
      - Consider the image analysis: ${JSON.stringify(request.mediaAnalysis)}
      - Match trending style for ${request.platform}
      - Keep within character limits for ${request.platform}
      
      Return as JSON array of caption strings.`;

      const response = await openai.chat.completions.create({
        model: "gpt-4",
        messages: [
          {
            role: "system",
            content: "You are a social media expert who creates viral content. Generate engaging captions that match current trends and platform best practices."
          },
          {
            role: "user",
            content: prompt
          }
        ],
        max_tokens: 1000,
        temperature: 0.8,
      });

      const captionsText = response.choices[0].message.content;
      return JSON.parse(captionsText || '[]');
    } catch (error) {
      console.error('Error generating captions:', error);
      throw new Error('Failed to generate captions');
    }
  }

  async generateEmbedding(text: string): Promise<number[]> {
    try {
      const response = await openai.embeddings.create({
        model: "text-embedding-ada-002",
        input: text,
      });

      return response.data[0].embedding;
    } catch (error) {
      console.error('Error generating embedding:', error);
      throw new Error('Failed to generate embedding');
    }
  }
}

export const openaiService = new OpenAIService();'''

with open('src/services/ai/openai.ts', 'w') as f:
    f.write(openai_service)

# Create Pinecone service
os.makedirs('src/services/database', exist_ok=True)

pinecone_service = '''import { Pinecone } from '@pinecone-database/pinecone';
import { TrendMatch } from '@/types';

export class PineconeService {
  private pinecone: Pinecone;
  private indexName: string;

  constructor() {
    this.pinecone = new Pinecone({
      apiKey: process.env.PINECONE_API_KEY!,
      environment: process.env.PINECONE_ENVIRONMENT!,
    });
    this.indexName = process.env.PINECONE_INDEX_NAME || 'manty-trends';
  }

  async getIndex() {
    return this.pinecone.index(this.indexName);
  }

  async upsertTrend(trendId: string, embedding: number[], metadata: any) {
    try {
      const index = await this.getIndex();
      
      await index.upsert([{
        id: trendId,
        values: embedding,
        metadata
      }]);
    } catch (error) {
      console.error('Error upserting trend:', error);
      throw new Error('Failed to upsert trend');
    }
  }

  async findSimilarTrends(embedding: number[], topK: number = 5): Promise<TrendMatch[]> {
    try {
      const index = await this.getIndex();
      
      const queryResponse = await index.query({
        vector: embedding,
        topK,
        includeMetadata: true,
      });

      return queryResponse.matches?.map(match => ({
        trendId: match.id,
        score: match.score || 0,
        compatibilityReasons: this.generateCompatibilityReasons(match.score || 0)
      })) || [];
    } catch (error) {
      console.error('Error finding similar trends:', error);
      throw new Error('Failed to find similar trends');
    }
  }

  async generateEmbedding(text: string): Promise<number[]> {
    // This would typically use the same embedding model as OpenAI
    // For now, we'll create a mock embedding
    return new Array(1536).fill(0).map(() => Math.random() - 0.5);
  }

  private generateCompatibilityReasons(score: number): string[] {
    if (score >= 0.8) {
      return ['Excellent mood match', 'Perfect color palette alignment', 'Strong visual similarity'];
    } else if (score >= 0.6) {
      return ['Good thematic match', 'Similar visual elements', 'Complementary mood'];
    } else {
      return ['Basic compatibility', 'Some shared elements'];
    }
  }

  async deleteTrend(trendId: string) {
    try {
      const index = await this.getIndex();
      await index.delete1([trendId]);
    } catch (error) {
      console.error('Error deleting trend:', error);
      throw new Error('Failed to delete trend');
    }
  }

  async searchTrends(query: string, filters?: any): Promise<TrendMatch[]> {
    // Convert query to embedding first
    const embedding = await this.generateEmbedding(query);
    return this.findSimilarTrends(embedding);
  }
}

export const pineconeService = new PineconeService();'''

with open('src/services/database/pinecone.ts', 'w') as f:
    f.write(pinecone_service)

print("Created AI and database service layers")