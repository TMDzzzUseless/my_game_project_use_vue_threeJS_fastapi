<script setup lang="ts">
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const message = ref('')
const isLoggedIn = ref(false)
const loggedInEmail = ref('')

const handleLogin = async () => {
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    })

    const data = await response.json()

    if (response.ok) {
      isLoggedIn.value = true
      loggedInEmail.value = data.user.email
      message.value = data.message
      localStorage.setItem('access_token', data.access_token)
    } else {
      message.value = data.detail || '登入失敗'
    }
  } catch (error) {
    message.value = '無法連線到後端伺服器，請確認 FastAPI 是否啟動！'
  }
}
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <h1>🎮 遊戲登入系統</h1>

      <div v-if="!isLoggedIn" class="form-group">
        <input 
          v-model="email" 
          type="email" 
          placeholder="請輸入 Email" 
        />
        <input 
          v-model="password" 
          type="password" 
          placeholder="請輸入密碼" 
        />
        <button @click="handleLogin">登入遊戲</button>
      </div>

      <div v-else class="welcome-box">
        <h2>歡迎回來！</h2>
        <p>帳號：{{ loggedInEmail }}</p>
        <p>準備好進入 3D 遊戲世界了嗎？</p>
      </div>

      <p class="message" :class="{ success: isLoggedIn }">{{ message }}</p>
    </div>
  </div>
</template>

<style>
/* 從 src/App.vue 進入 assets 資料夾抓取 login.css */
@import './assets/login.css';
</style>