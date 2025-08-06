import { Pinecone } from '@pinecone-database/pinecone';
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

export const pineconeService = new PineconeService();