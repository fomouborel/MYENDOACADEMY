import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: 'e2e',
  timeout: 30_000,
  use: { baseURL: 'http://localhost:4173/MYENDOACADEMY/' },
  webServer: { command: 'npx vite preview --port 4173 --strictPort', url: 'http://localhost:4173/MYENDOACADEMY/', reuseExistingServer: true },
  projects: [
    { name: 'ordinateur', use: { ...devices['Desktop Chrome'] } },
    { name: 'smartphone', use: { ...devices['Pixel 7'] } },
  ],
});
