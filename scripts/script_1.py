# Create TypeScript configuration files
tsconfig_json = {
    "compilerOptions": {
        "target": "ES2022",
        "lib": ["dom", "dom.iterable", "ES2022"],
        "allowJs": True,
        "skipLibCheck": True,
        "strict": True,
        "forceConsistentCasingInFileNames": True,
        "noEmit": True,
        "esModuleInterop": True,
        "module": "esnext",
        "moduleResolution": "bundler",
        "resolveJsonModule": True,
        "isolatedModules": True,
        "jsx": "preserve",
        "incremental": True,
        "plugins": [
            {
                "name": "next"
            }
        ],
        "baseUrl": ".",
        "paths": {
            "@/*": ["./src/*"],
            "@/components/*": ["./src/components/*"],
            "@/components/ui/*": ["./src/components/ui/*"],
            "@/lib/*": ["./src/lib/*"],
            "@/hooks/*": ["./src/hooks/*"],
            "@/types/*": ["./src/types/*"],
            "@/services/*": ["./src/services/*"],
            "@/styles/*": ["./src/styles/*"]
        }
    },
    "include": [
        "next-env.d.ts",
        "**/*.ts",
        "**/*.tsx",
        ".next/types/**/*.ts"
    ],
    "exclude": ["node_modules"]
}

with open('tsconfig.json', 'w') as f:
    json.dump(tsconfig_json, f, indent=2)

# Create Next.js configuration
next_config = '''/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: [
      'res.cloudinary.com',
      's3.amazonaws.com',
      'graph.facebook.com',
      'i.ytimg.com',
      'p16-sign-va.tiktokcdn.com'
    ],
  },
  env: {
    NEXTAUTH_URL: process.env.NEXTAUTH_URL,
    NEXTAUTH_SECRET: process.env.NEXTAUTH_SECRET,
  },
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.resolve.fallback = {
        ...config.resolve.fallback,
        fs: false,
        net: false,
        tls: false,
      };
    }
    return config;
  },
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: '/api/:path*',
      },
    ];
  },
};

module.exports = nextConfig;'''

with open('next.config.js', 'w') as f:
    f.write(next_config)

# Create Vite configuration
vite_config = '''import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@/components': path.resolve(__dirname, './src/components'),
      '@/components/ui': path.resolve(__dirname, './src/components/ui'),
      '@/lib': path.resolve(__dirname, './src/lib'),
      '@/hooks': path.resolve(__dirname, './src/hooks'),
      '@/types': path.resolve(__dirname, './src/types'),
      '@/services': path.resolve(__dirname, './src/services'),
      '@/styles': path.resolve(__dirname, './src/styles'),
    },
  },
  server: {
    port: 3001,
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.ts'],
  },
});'''

with open('vite.config.ts', 'w') as f:
    f.write(vite_config)

print("Created TypeScript and build configuration files")