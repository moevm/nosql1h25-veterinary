<template>
  <div>
    <Header />
    <AppointmentTable />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import AppointmentTable from "@/components/AppointmentTable.vue";

export default {
  components: { Header: HeaderAdmin, AppointmentTable }
}
</script>