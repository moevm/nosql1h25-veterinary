<template>
  <div>
    <Header />
    <ProcedureTable />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import ProcedureTable from "@/components/ProcedureTable.vue";

export default {
  components: { Header: HeaderAdmin, ProcedureTable }
}
</script>