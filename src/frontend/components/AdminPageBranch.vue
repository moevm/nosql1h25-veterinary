<template>
  <div>
    <Header />
    <OfficeTable />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import OfficeTable from "@/components/OfficeTable.vue";

export default {
  components: { Header: HeaderAdmin, OfficeTable }
}
</script>