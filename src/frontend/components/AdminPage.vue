components/AdminPage.vue
вот так было:
<template>
  <div>
    <Header />
    <h1>Страница администратора</h1>
  </div>
</template>

<script>
import Header from './Header.vue';

export default {
  components: { Header }
}
</script>
