<template>
  <div>
    <Header />
    <UserTables />
  </div>
</template>

<script>
import Header from './Header.vue';
import UserTables from './UserTables.vue';


export default {
  components: { Header, UserTables }
}
</script>
