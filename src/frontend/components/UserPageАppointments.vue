<template>
  <div>
    <Header />
    <h1> Мои приёмы </h1>
    <UserTable />
  </div>
</template>

<script>
import HeaderUser from './HeaderUser.vue';

export default {
  name: 'UserPage',
  components: {
    Header: HeaderUser
  }
}
</script>
