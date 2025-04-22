<template>
  <div>
    <Header />
    <DoctorTables />
  </div>
</template>

<script>
import Header from './Header.vue';
import DoctorTables from './DoctorTables.vue';

  
export default {
  components: { Header, DoctorTables }
}
</script>
