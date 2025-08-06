import OpenAI from 'openai';
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

export const openaiService = new OpenAIService();