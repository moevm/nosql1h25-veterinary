<template>
  <div>
    <Header />
    <PetTable />
  </div>
</template>


<script>
import HeaderAdmin from './HeaderAdmin.vue';
import PetTable from "@/components/PetTable.vue";

export default {
  components: { Header: HeaderAdmin, PetTable }
}
</script>