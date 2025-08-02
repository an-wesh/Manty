# Create Tailwind and ShadCN configurations
tailwind_config = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  prefix: "",
  theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      keyframes: {
        "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
      },
      animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}'''

with open('tailwind.config.js', 'w') as f:
    f.write(tailwind_config)

# Create ShadCN components configuration
components_json = {
    "$schema": "https://ui.shadcn.com/schema.json",
    "style": "default",
    "rsc": True,
    "tsx": True,
    "tailwind": {
        "config": "tailwind.config.js",
        "css": "src/styles/globals.css",
        "baseColor": "slate",
        "cssVariables": True,
        "prefix": ""
    },
    "aliases": {
        "components": "@/components",
        "utils": "@/lib/utils",
        "ui": "@/components/ui"
    }
}

with open('components.json', 'w') as f:
    json.dump(components_json, f, indent=2)

# Create Vercel deployment configuration
vercel_json = {
    "buildCommand": "npm run build",
    "outputDirectory": ".next",
    "framework": "nextjs",
    "functions": {
        "src/pages/api/**/*.ts": {
            "maxDuration": 30
        }
    },
    "env": {
        "POSTGRES_URL": "@postgres-url",
        "NEXTAUTH_SECRET": "@nextauth-secret",
        "OPENAI_API_KEY": "@openai-api-key",
        "PINECONE_API_KEY": "@pinecone-api-key",
        "CLOUDINARY_CLOUD_NAME": "@cloudinary-cloud-name",
        "CLOUDINARY_API_KEY": "@cloudinary-api-key",
        "CLOUDINARY_API_SECRET": "@cloudinary-api-secret"
    },
    "rewrites": [
        {
            "source": "/api/(.*)",
            "destination": "/api/$1"
        }
    ]
}

with open('vercel.json', 'w') as f:
    json.dump(vercel_json, f, indent=2)

print("Created Tailwind, ShadCN, and Vercel configuration files")