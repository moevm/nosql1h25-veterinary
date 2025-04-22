<template>
  <div>
    <Header />
    <AdminTables />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import AdminTables from './AdminTables.vue';

export default {
  components: { Header: HeaderAdmin, AdminTables }
}
</script>