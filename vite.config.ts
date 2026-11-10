/// <reference types="vitest/config" />
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';
import { fileURLToPath } from 'node:url';

// Chemin de base : GitHub Pages sert le site sous /<nom-du-dépôt>/.
// BASE_PATH permet de changer d'hébergeur (ex. Cloudflare Pages : "/") sans toucher au code.
const base = process.env.BASE_PATH ?? '/MYENDOACADEMY/';

export default defineConfig({
  base,
  resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } },
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg'],
      manifest: {
        name: 'ENDOCRINO ACADEMY',
        short_name: 'Endocrino',
        description: "Cours, entraînement et anciens examens d'endocrinologie",
        lang: 'fr',
        theme_color: '#0b2545',
        background_color: '#ffffff',
        display: 'standalone',
        start_url: base,
        scope: base,
        icons: [{ src: 'favicon.svg', sizes: 'any', type: 'image/svg+xml', purpose: 'any' }],
      },
      workbox: { globPatterns: ['**/*.{js,css,html,svg,png,json,md}'] },
    }),
  ],
  test: {
    environment: 'jsdom',
    include: ['src/**/*.test.{ts,tsx}', 'scripts/**/*.test.ts'],
    setupFiles: ['src/test-setup.ts'],
  },
});
