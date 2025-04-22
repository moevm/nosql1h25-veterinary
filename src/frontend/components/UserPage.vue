<template>
  <div>
    <Header />
    <UserTables />
  </div>
</template>

<script>
import HeaderUser from './HeaderUser.vue';
import UserTables from './UserTables.vue';


export default {
name: 'UserPage',
  components: { HeaderUser, UserTables }
}
</script>
