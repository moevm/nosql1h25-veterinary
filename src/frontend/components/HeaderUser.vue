<template>
  <header class="header">
    <nav class="nav">
      <button @click="$router.push('/user/appointments')">Мои приёмы</button>
      <button @click="$router.push('/user/add-pet')">Добавить питомца</button>
      <button @click="$router.push('/user/bookings')">Записи на приём</button>

      <div class="dropdown" @click="toggleDropdown">
        <button class="dropdown-button">☰</button>
        <div class="dropdown-menu" v-if="dropdownOpen">
          <a @click="goToProfile">Профиль</a>
          <a @click="logout">Выход</a>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  data() {
    return {
      dropdownOpen: false
    }
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen
    },
    goToProfile() {
      this.dropdownOpen = false
      alert('Переход в профиль')
    },
    logout() {
      this.dropdownOpen = false
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.header {
  background-color: #e6f9e6;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  background-color: #81c784;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

button:hover {
  background-color: #66bb6a;
}

.dropdown {
  position: relative;
}

.dropdown-button {
  font-size: 1.2rem;
  background-color: #388e3c;
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  color: white;
  cursor: pointer;
}

.dropdown-button:hover {
  background-color: #2e7d32;
}

.dropdown-menu {
  position: absolute;
  right: 0;
  top: 40px;
  background-color: #ffffff;
  border: 1px solid #a5d6a7;
  border-radius: 5px;
  box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  min-width: 120px;
  z-index: 100;
}

.dropdown-menu a {
  padding: 0.5rem 1rem;
  cursor: pointer;
  text-align: left;
  white-space: nowrap;
  color: #2e7d32;
  font-weight: 500;
}

.dropdown-menu a:hover {
  background-color: #f1f8e9;
}
</style>
