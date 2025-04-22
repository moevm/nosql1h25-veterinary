<template>
  <div>
    <Header />
    <h1> Запись на приём </h1>
    <UserTable />
  </div>
</template>

<script>
import HeaderUser from './HeaderUser.vue';
import UserTables from './UserTables.vue';

export default {
  name: 'UserPage',
  components: {
    Header: HeaderUser, UserTables: UserTables
  }
}
</script>
