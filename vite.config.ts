import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/GittiAI/' // для GitHub Pages! Имя репозитория
})
