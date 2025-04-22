<template>
  <div>
    <Header />
    <UserTable />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import UserTable from "@/components/UserTable.vue";

export default {
  components: { Header: HeaderAdmin, UserTable }
}
</script>