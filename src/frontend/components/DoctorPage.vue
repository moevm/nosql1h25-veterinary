<template>
  <div>
    <Header />
    <div v-if="doctor">
      <p>Имя: {{ doctor.name }}</p>
      <p>Специализация: {{ doctor.specialization }}</p>
    </div>
    <div v-else>
      Загрузка данных доктора...
    </div>
  </div>
</template>

<script>
import { Doctor } from '@/models/Doctor';
import { getDoctorById } from '@/api/entity';
import HeaderDoctor from './HeaderDoctor.vue';
import DoctorTables from './DoctorTables.vue';

export default {
  name: 'DoctorPage',
  components: {
    Header: HeaderDoctor, DoctorTables
  },
  data() {
    return {
      doctor: null
    }
  },
  async mounted() {
    try {
      const data = await getDoctorById(1); // Пример ID
      this.doctor = new Doctor(data);
    } catch (error) {
      console.error('Ошибка загрузки доктора:', error);
    }
  }
}
</script>
