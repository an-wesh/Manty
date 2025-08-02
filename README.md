# Manty - AI-Powered Social Media Trend Analysis

Manty is a comprehensive full-stack application that helps content creators analyze their photos and videos using AI, match them with current social media trends, and generate optimized content for maximum engagement across platforms like Instagram, TikTok, YouTube, and Facebook.

## 🚀 Features

- **AI Media Analysis**: Advanced computer vision analysis of photos and videos
- **Trend Matching**: Real-time matching with current social media trends
- **Multi-Platform Support**: Optimized for Instagram, TikTok, YouTube, Facebook
- **Smart Caption Generation**: AI-powered captions and hashtag suggestions
- **Batch Processing**: Upload and analyze multiple files simultaneously
- **Project Management**: Organize and track your content projects
- **OAuth Integration**: Sign in with social media accounts
- **Real-time Processing**: Live progress tracking and instant results

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** with App Router
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **ShadCN UI** for components
- **Lucide React** for icons

### Backend
- **Next.js API Routes** for serverless functions
- **NextAuth.js** for authentication
- **Prisma** with PostgreSQL for database
- **OpenAI GPT-4 Vision** for AI analysis
- **Pinecone** for vector similarity search
- **Cloudinary** for media storage

### Infrastructure
- **Vercel** for deployment
- **PostgreSQL** database
- **Redis** for job queues
- **BullMQ** for background processing

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/manty.git
   cd manty
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   ```

   Fill in your environment variables:
   - Database URLs
   - OpenAI API key
   - Social media OAuth credentials
   - Cloudinary/AWS credentials
   - Pinecone configuration

4. **Set up the database**
   ```bash
   npx prisma generate
   npx prisma db push
   ```

5. **Run the development server**
   ```bash
   npm run dev
   ```

6. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🔧 Configuration

### OAuth Setup

1. **Instagram/Facebook**
   - Create a Facebook App at [developers.facebook.com](https://developers.facebook.com)
   - Enable Instagram Basic Display API
   - Add redirect URI: `https://your-domain.com/api/auth/callback/facebook`

2. **TikTok**
   - Create a TikTok App at [developers.tiktok.com](https://developers.tiktok.com)
   - Configure Login Kit for Web
   - Add redirect URI: `https://your-domain.com/api/auth/callback/tiktok`

3. **YouTube**
   - Create a Google Cloud Project
   - Enable YouTube Data API v3
   - Configure OAuth consent screen
   - Add redirect URI: `https://your-domain.com/api/auth/callback/google`

### AI Services

1. **OpenAI**
   - Get API key from [platform.openai.com](https://platform.openai.com)
   - Ensure you have access to GPT-4 Vision

2. **Pinecone**
   - Create account at [pinecone.io](https://pinecone.io)
   - Create an index with 1536 dimensions
   - Get API key and environment details

### Storage

1. **Cloudinary**
   - Create account at [cloudinary.com](https://cloudinary.com)
   - Get cloud name, API key, and secret
   - Create upload preset named "manty_uploads"

## 📁 Project Structure

```
/manty/
├── /public              # Static assets
├── /prisma             # Database schema
├── /src
│   ├── /app            # Next.js 14 App Router pages
│   ├── /components     # React components
│   │   ├── /ui         # ShadCN UI components
│   │   ├── /common     # Shared components
│   │   ├── /upload     # Upload-related components
│   │   ├── /analysis   # Analysis display components
│   │   └── /trends     # Trend-related components
│   ├── /pages/api      # API routes
│   │   ├── /auth       # Authentication endpoints
│   │   ├── /ai         # AI processing endpoints
│   │   ├── /media      # Media handling endpoints
│   │   └── /trends     # Trend data endpoints
│   ├── /services       # External service integrations
│   │   ├── /ai         # OpenAI, LangChain services
│   │   ├── /storage    # Cloudinary, S3 services
│   │   ├── /database   # Pinecone, vector operations
│   │   └── /social     # Social media API clients
│   ├── /hooks          # Custom React hooks
│   ├── /lib            # Utility functions and configs
│   ├── /types          # TypeScript type definitions
│   └── /styles         # Global styles and Tailwind config
├── next.config.js      # Next.js configuration
├── tailwind.config.js  # Tailwind CSS configuration
├── tsconfig.json       # TypeScript configuration
└── vercel.json         # Vercel deployment config
```

## 🚀 Deployment

### Vercel (Recommended)

1. **Connect your repository to Vercel**
2. **Set environment variables in Vercel dashboard**
3. **Deploy automatically on push to main branch**

### Manual Deployment

1. **Build the application**
   ```bash
   npm run build
   ```

2. **Start the production server**
   ```bash
   npm start
   ```

## 📊 API Endpoints

### Authentication
- `POST /api/auth/signin` - Sign in with OAuth providers
- `GET /api/auth/session` - Get current user session

### Media Processing
- `POST /api/media/upload` - Upload media files
- `POST /api/ai/analyze-media` - Analyze uploaded media
- `POST /api/ai/generate-caption` - Generate captions
- `GET /api/trends/search` - Search for trends

### Project Management
- `GET /api/projects` - List user projects
- `POST /api/projects` - Create new project
- `PUT /api/projects/[id]` - Update project
- `DELETE /api/projects/[id]` - Delete project

## 🧪 Testing

```bash
# Run unit tests
npm run test

# Run tests with UI
npm run test:ui

# Type checking
npm run type-check
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for GPT-4 Vision API
- Vercel for hosting and deployment
- The Next.js team for the amazing framework
- ShadCN for the beautiful UI components
- All the open-source contributors who made this possible

---

**Made with ❤️ for content creators worldwide**

For support, email support@manty.app or join our Discord community.
