# Create Next.js App Router pages
os.makedirs('src/app', exist_ok=True)
os.makedirs('src/app/dashboard', exist_ok=True)
os.makedirs('src/app/upload', exist_ok=True)

# Root layout
layout_tsx = '''import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { SessionProvider } from 'next-auth/react'
import { Header } from '@/components/common/Header'
import '@/styles/globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Manty - AI-Powered Social Media Trend Analysis',
  description: 'Analyze your photos and videos with AI, match them with current trends, and create viral content optimized for social media.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <SessionProvider>
          <div className="min-h-screen bg-background">
            <Header />
            <main className="max-w-7xl mx-auto px-4 py-8">
              {children}
            </main>
          </div>
        </SessionProvider>
      </body>
    </html>
  )
}'''

with open('src/app/layout.tsx', 'w') as f:
    f.write(layout_tsx)

# Home page
page_tsx = '''\'use client\';

import React from \'react\';
import Link from \'next/link\';
import { Button } from \'@/components/ui/button\';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from \'@/components/ui/card\';
import { Upload, Brain, TrendingUp, Zap, Camera, Hash } from \'lucide-react\';

export default function HomePage() {
  return (
    <div className="space-y-16">
      {/* Hero Section */}
      <section className="text-center space-y-8">
        <div className="space-y-4">
          <h1 className="text-4xl md:text-6xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AI-Powered Social Media Trend Analysis
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Analyze your photos and videos with AI, match them with current trends, and create viral content optimized for Instagram, TikTok, and YouTube.
          </p>
        </div>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Button asChild size="lg" className="text-lg px-8 py-6">
            <Link href="/upload">
              <Upload className="mr-2 h-5 w-5" />
              Get Started
            </Link>
          </Button>
          <Button variant="outline" size="lg" className="text-lg px-8 py-6">
            View Demo
          </Button>
        </div>
      </section>

      {/* Features Section */}
      <section className="space-y-12">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Powerful Features for Content Creators
          </h2>
          <p className="text-lg text-gray-600">
            Everything you need to create viral content that resonates with your audience
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Brain className="h-12 w-12 text-blue-600 mb-4" />
              <CardTitle>AI Media Analysis</CardTitle>
              <CardDescription>
                Advanced AI analyzes your photos and videos to detect mood, scene type, colors, and composition
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <TrendingUp className="h-12 w-12 text-green-600 mb-4" />
              <CardTitle>Trend Matching</CardTitle>
              <CardDescription>
                Match your content with current trends across Instagram, TikTok, YouTube, and other platforms
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Zap className="h-12 w-12 text-purple-600 mb-4" />
              <CardTitle>Smart Editing</CardTitle>
              <CardDescription>
                Apply trend-based filters, effects, and optimizations to make your content viral-ready
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Hash className="h-12 w-12 text-orange-600 mb-4" />
              <CardTitle>Caption Generation</CardTitle>
              <CardDescription>
                AI-generated captions and hashtags optimized for each platform and your target audience
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Camera className="h-12 w-12 text-red-600 mb-4" />
              <CardTitle>Multi-Platform</CardTitle>
              <CardDescription>
                Optimize content for Instagram, TikTok, YouTube, Facebook, and more with platform-specific features
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Upload className="h-12 w-12 text-teal-600 mb-4" />
              <CardTitle>Batch Processing</CardTitle>
              <CardDescription>
                Upload multiple files at once and process them in batches for efficient workflow management
              </CardDescription>
            </CardHeader>
          </Card>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-12 text-center text-white">
        <h2 className="text-3xl font-bold mb-4">
          Ready to Create Viral Content?
        </h2>
        <p className="text-xl mb-8 opacity-90">
          Join thousands of content creators who use Manty to boost their social media engagement
        </p>
        <Button asChild size="lg" variant="secondary" className="text-lg px-8 py-6">
          <Link href="/upload">
            Start Analyzing Now
          </Link>
        </Button>
      </section>
    </div>
  );
}'''

with open('src/app/page.tsx', 'w') as f:
    f.write(page_tsx)

# Upload page
upload_page = '''\'use client\';

import React, { useState } from \'react\';
import { FileUploader } from \'@/components/upload/FileUploader\';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from \'@/components/ui/card\';
import { Button } from \'@/components/ui/button\';
import { Brain, TrendingUp } from \'lucide-react\';

interface UploadedFile {
  id: string;
  name: string;
  size: number;
  type: string;
  url: string;
  progress: number;
  status: \'uploading\' | \'completed\' | \'error\';
}

export default function UploadPage() {
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFile[]>([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const handleUploadComplete = (files: UploadedFile[]) => {
    setUploadedFiles(files);
  };

  const startAnalysis = async () => {
    setIsAnalyzing(true);
    
    // Simulate analysis process
    try {
      for (const file of uploadedFiles) {
        const response = await fetch(\'/api/ai/analyze-media\', {
          method: \'POST\',
          headers: {
            \'Content-Type\': \'application/json\',
          },
          body: JSON.stringify({
            mediaUrl: file.url,
            mediaId: file.id,
          }),
        });
        
        if (!response.ok) {
          throw new Error(\'Analysis failed\');
        }
        
        const result = await response.json();
        console.log(\'Analysis result:\', result);
      }
      
      // Redirect to dashboard after analysis
      window.location.href = \'/dashboard\';
    } catch (error) {
      console.error(\'Analysis error:\', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <div className="text-center space-y-4">
        <h1 className="text-3xl font-bold text-gray-900">
          Upload Your Media
        </h1>
        <p className="text-lg text-gray-600">
          Upload your photos and videos to analyze them with AI and discover trending opportunities
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Media Upload</CardTitle>
          <CardDescription>
            Drag and drop your images or videos, or click to browse. We support JPG, PNG, MP4, and MOV files up to 100MB each.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <FileUploader
            onUploadComplete={handleUploadComplete}
            maxFiles={10}
            acceptedTypes={[\'image/*\', \'video/*\']}
          />
        </CardContent>
      </Card>

      {uploadedFiles.length > 0 && (
        <div className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center">
                <Brain className="mr-2 h-5 w-5" />
                Ready for Analysis
              </CardTitle>
              <CardDescription>
                {uploadedFiles.length} file{uploadedFiles.length !== 1 ? \'s\' : \'\'} uploaded successfully. 
                Start the AI analysis to discover trends and optimization opportunities.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex flex-col sm:flex-row gap-4">
                <Button 
                  onClick={startAnalysis}
                  disabled={isAnalyzing}
                  className="flex-1"
                >
                  {isAnalyzing ? (
                    <>
                      <Brain className="mr-2 h-4 w-4 animate-spin" />
                      Analyzing...
                    </>
                  ) : (
                    <>
                      <Brain className="mr-2 h-4 w-4" />
                      Start AI Analysis
                    </>
                  )}
                </Button>
                <Button variant="outline" className="flex-1">
                  <TrendingUp className="mr-2 h-4 w-4" />
                  View Trends First
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      )}

      <div className="grid md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">What happens next?</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-sm font-medium">1</div>
              <p className="text-sm text-gray-600">AI analyzes your media for mood, colors, objects, and composition</p>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-sm font-medium">2</div>
              <p className="text-sm text-gray-600">We match your content with current trending topics and hashtags</p>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-sm font-medium">3</div>
              <p className="text-sm text-gray-600">Get personalized recommendations for optimization and captions</p>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Supported Platforms</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="grid grid-cols-2 gap-3">
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-gradient-to-r from-purple-500 to-pink-500 rounded-full"></div>
                <span className="text-sm">Instagram</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-black rounded-full"></div>
                <span className="text-sm">TikTok</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-red-500 rounded-full"></div>
                <span className="text-sm">YouTube</span>
              </div>
              <div className="flex items-center space-x-2">
                <div className="w-3 h-3 bg-blue-600 rounded-full"></div>
                <span className="text-sm">Facebook</span>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}'''

with open('src/app/upload/page.tsx', 'w') as f:
    f.write(upload_page)

print("Created Next.js App Router pages with layout and home/upload pages")