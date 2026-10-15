import { defineConfig, devices } from "@playwright/test"

// ./verify starts the app (FastAPI serving the built frontend) and sets this.
const baseURL = process.env.PLAYWRIGHT_BASE_URL ?? "http://localhost:8000"

export default defineConfig({
  testDir: "./tests",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  reporter: "list",
  use: {
    baseURL,
    trace: "retain-on-failure",
  },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"] } }],
})
