<template>
  <div>
    <Header />
    <AdminTables />
  </div>
</template>

<script>
import Header from './Header.vue';
import AdminTables from './AdminTables.vue';

export default {
  components: { Header, AdminTables }
}
</script>
