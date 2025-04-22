<script>
import {Doctor} from '@/models/Doctor';
import { getDoctorById } from '@/api/entity';
import Header from './Header.vue';

export default {
  components: { Header },
  data() {
    return {
      doctor: null
    }
  },
  async mounted() {
    // Временный пример — загружаем доктора с id 1
    const data = await getDoctorById(1)
    this.doctor = new Doctor(data)
  }
}
</script>
