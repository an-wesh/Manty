'use client';

import React from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Upload, Brain, TrendingUp, Zap, Camera, Hash } from 'lucide-react';

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
}