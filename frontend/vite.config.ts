import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
            port: 3000,      // 👈 設定前端固定跑在 3000 埠
            strictPort: true, // 如果 3000 被佔用直接報錯，不自動跳號
          },
  proxy: {
          '/api': {
          target: 'http://127.0.0.1:8000', //api強制連8000
          changeOrigin: true,
                  }
          },
})
