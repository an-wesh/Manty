# Let me create the complete codebase files for the Manty application
# I'll start by creating the package.json and core configuration files

import os
import json

# Create the project directory structure
project_structure = {
    "public": ["favicon.ico", "logo.png", "manifest.json"],
    "src": {
        "components": {
            "ui": ["button.tsx", "card.tsx", "input.tsx", "select.tsx", "textarea.tsx", "modal.tsx", "progress.tsx", "badge.tsx", "tabs.tsx", "index.ts"],
            "common": ["Header.tsx", "Navbar.tsx", "Footer.tsx", "LoadingSpinner.tsx"],
            "upload": ["FileUploader.tsx", "DragDropZone.tsx", "UploadProgress.tsx"],
            "analysis": ["AnalysisCard.tsx", "ColorPalette.tsx", "MoodIndicator.tsx", "ConfidenceScore.tsx"],
            "trends": ["TrendCard.tsx", "TrendList.tsx", "HashtagSuggestions.tsx", "PlatformSelector.tsx"],
            "editor": ["ImageEditor.tsx", "FilterPanel.tsx", "AspectRatioSelector.tsx", "BeforeAfterView.tsx"],
            "caption": ["CaptionGenerator.tsx", "ToneSelector.tsx", "CharacterCounter.tsx"],
            "project": ["ProjectCard.tsx", "ProjectGrid.tsx", "ProjectDetails.tsx"]
        },
        "pages": {
            "api": {
                "auth": ["[...nextauth].ts", "signin.ts"],
                "social": ["instagram.ts", "tiktok.ts", "facebook.ts", "youtube.ts"],
                "ai": ["analyze-media.ts", "generate-caption.ts", "match-trends.ts", "apply-filters.ts"],
                "media": ["upload.ts", "process.ts", "delete.ts"],
                "trends": ["search.ts", "popular.ts", "platform-specific.ts"],
                "projects": ["create.ts", "update.ts", "delete.ts", "[id].ts"],
                "user": ["profile.ts", "preferences.ts"]
            }
        },
        "services": {
            "ai": ["openai.ts", "langchain.ts", "vision-analysis.ts"],
            "storage": ["cloudinary.ts", "s3.ts", "file-manager.ts"],
            "database": ["pinecone.ts", "weaviate.ts", "vector-search.ts"],
            "social": ["instagram-api.ts", "tiktok-api.ts", "facebook-api.ts", "youtube-api.ts"],
            "queue": ["bullmq.ts", "job-processor.ts"]
        },
        "hooks": ["useAuth.ts", "useUpload.ts", "useAnalysis.ts", "useTrends.ts", "useEditor.ts", "useProjects.ts", "useLocalStorage.ts"],
        "lib": ["auth.ts", "db.ts", "utils.ts", "constants.ts", "validation.ts", "middleware.ts"],
        "types": ["auth.ts", "media.ts", "analysis.ts", "trends.ts", "projects.ts", "api.ts", "index.ts"],
        "styles": ["globals.css", "components.css", "utilities.css"],
        "app": {
            "dashboard": ["page.tsx", "layout.tsx"],
            "upload": ["page.tsx"],
            "analysis": ["page.tsx"],
            "trends": ["page.tsx"],
            "editor": ["page.tsx"],
            "projects": ["page.tsx", "[id]/page.tsx"],
            "auth": {
                "signin": ["page.tsx"],
                "callback": ["page.tsx"]
            }
        }
    }
}

# Create package.json
package_json = {
    "name": "manty",
    "version": "1.0.0",
    "private": True,
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start",
        "lint": "next lint",
        "type-check": "tsc --noEmit",
        "test": "vitest",
        "test:ui": "vitest --ui"
    },
    "dependencies": {
        "next": "^14.2.0",
        "react": "^18.3.0",
        "react-dom": "^18.3.0",
        "typescript": "^5.4.0",
        "@next/font": "^14.2.0",
        "next-auth": "^4.24.0",
        "@auth/prisma-adapter": "^2.0.0",
        "@prisma/client": "^5.14.0",
        "prisma": "^5.14.0",
        "openai": "^4.52.0",
        "langchain": "^0.2.0",
        "@langchain/openai": "^0.2.0",
        "@pinecone-database/pinecone": "^2.2.0",
        "cloudinary": "^2.2.0",
        "aws-sdk": "^2.1654.0",
        "bullmq": "^5.7.0",
        "ioredis": "^5.4.0",
        "@radix-ui/react-slot": "^1.0.2",
        "@radix-ui/react-dialog": "^1.0.5",
        "@radix-ui/react-select": "^2.0.0",
        "@radix-ui/react-tabs": "^1.0.4",
        "@radix-ui/react-progress": "^1.0.3",
        "class-variance-authority": "^0.7.0",
        "clsx": "^2.1.0",
        "tailwind-merge": "^2.3.0",
        "tailwindcss": "^3.4.0",
        "tailwindcss-animate": "^1.0.7",
        "react-dropzone": "^14.2.0",
        "react-image-crop": "^11.0.0",
        "canvas": "^2.11.0",
        "sharp": "^0.33.0",
        "zod": "^3.23.0",
        "react-hook-form": "^7.51.0",
        "@hookform/resolvers": "^3.4.0",
        "date-fns": "^3.6.0",
        "lucide-react": "^0.376.0"
    },
    "devDependencies": {
        "@types/node": "^20.12.0",
        "@types/react": "^18.3.0",
        "@types/react-dom": "^18.3.0",
        "eslint": "^8.57.0",
        "eslint-config-next": "^14.2.0",
        "autoprefixer": "^10.4.19",
        "postcss": "^8.4.0",
        "vitest": "^1.6.0",
        "@vitest/ui": "^1.6.0",
        "jsdom": "^24.0.0",
        "@testing-library/react": "^15.0.0",
        "@testing-library/jest-dom": "^6.4.0"
    }
}

# Save package.json
with open('package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("Created package.json")
print("Project structure mapped - ready to create all files")