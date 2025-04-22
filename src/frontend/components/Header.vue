<template>
  <header class="header">
    <nav>
      <button @click="$router.push('/doctor')">Доктор</button>
      <button @click="$router.push('/admin')">Админ</button>
      <button @click="$router.push('/user')">Пользователь</button>
      <button @click="goToProfile">Профиль</button>
      <button @click="logout">Выход</button>
    </nav>
  </header>
</template>

<script>
export default {
  methods: {
    goToProfile() {
      // пока просто заглушка
      alert("Переход в профиль");
    },
    logout() {
      // очистить токен, перейти на логин
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-around;
  background-color: #f4f4f4;
  padding: 1rem;
}
button {
  padding: 0.5rem 1rem;
  margin: 0 0.5rem;
}
</style>
