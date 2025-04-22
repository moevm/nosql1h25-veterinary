import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path' // ← добавь это

export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './') // указывает на корень frontend/
        }
    },
    server: {
        port: 3000
    }
})
