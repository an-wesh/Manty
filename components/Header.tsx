'use client';

import React from 'react';
import Link from 'next/link';
import { useAuth } from '@/hooks/useAuth';
import { Button } from '@/components/ui/button';
import { User, LogOut, Settings } from 'lucide-react';

export function Header() {
  const { user, isAuthenticated, signIn, signOut } = useAuth();

  return (
    <header className="bg-white border-b border-gray-200 px-4 py-3">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center space-x-8">
          <Link href="/" className="text-2xl font-bold text-primary">
            Manty
          </Link>

          {isAuthenticated && (
            <nav className="flex space-x-6">
              <Link href="/dashboard" className="text-gray-600 hover:text-primary">
                Dashboard
              </Link>
              <Link href="/upload" className="text-gray-600 hover:text-primary">
                Upload
              </Link>
              <Link href="/trends" className="text-gray-600 hover:text-primary">
                Trends
              </Link>
              <Link href="/projects" className="text-gray-600 hover:text-primary">
                Projects
              </Link>
            </nav>
          )}
        </div>

        <div className="flex items-center space-x-4">
          {isAuthenticated ? (
            <>
              <div className="flex items-center space-x-2">
                <User className="h-5 w-5 text-gray-500" />
                <span className="text-sm text-gray-700">{user?.name || user?.email}</span>
              </div>
              <Button variant="outline" size="sm" onClick={() => signOut()}>
                <LogOut className="h-4 w-4 mr-2" />
                Sign Out
              </Button>
            </>
          ) : (
            <Button onClick={() => signIn()}>
              Sign In
            </Button>
          )}
        </div>
      </div>
    </header>
  );
}