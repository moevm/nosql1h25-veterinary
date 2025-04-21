<template>
  <div class="login-page">
    <h2 class="title">Вход</h2>
    <form class="login-form" @submit.prevent="login">
      <input type="text" v-model="form.login" placeholder="Логин" required />
      <input type="password" v-model="form.password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import { loginUser } from '@/api/auth'

export default {
  name: 'LoginPage',
  data() {
    return {
      form: {
        login: '',
        password: ''
      },
      error: null
    }
  },
  methods: {
    async login() {
      this.error = null
      try {
        const user = await loginUser(this.form)
        console.log('Успешный вход:', user)
        this.$router.push('/')
      } catch (err) {
        this.error = err.response?.data?.message || 'Ошибка авторизации'
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  background-color: #e6f9e6; /* светло-зелёный фон */
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #2e7d32; /* тёмно-зелёный */
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 300px;
}

.login-form input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

.login-form button {
  padding: 10px;
  background-color: #c5f6c6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-form button:hover {
  background-color: #81e285;
}

.error {
  color: red;
  text-align: center;
}
</style>
