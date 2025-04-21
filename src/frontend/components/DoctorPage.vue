<template>
  <div>
    <Header />
    <h1>Страница доктора</h1>
  </div>
</template>

<script>
import Doctor from '../models/Doctor.js';
import { getDoctorById } from '../api/entity.js';
import Header from './Header.vue';

export default {
  components: { Header }
}
</script>
