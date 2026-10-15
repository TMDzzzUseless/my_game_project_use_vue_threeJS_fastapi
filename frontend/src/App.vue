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
      // 可以在這裡把 data.access_token 存到 localStorage 供後續遊戲 API 使用
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

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #1a1a1a;
  color: white;
  font-family: sans-serif;
}

.login-card {
  background: #2a2a2a;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
  width: 320px;
  text-align: center;
}

h1 {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  color: #42b883;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #444;
  background: #333;
  color: white;
  font-size: 1rem;
}

button {
  padding: 10px;
  border-radius: 6px;
  border: none;
  background: #42b883;
  color: white;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
}

button:hover {
  background: #35495e;
}

.message {
  margin-top: 1rem;
  font-size: 0.9rem;
  color: #ff6b6b;
}

.message.success {
  color: #42b883;
}
</style>
