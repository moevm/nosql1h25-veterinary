<template>
  <DataTable
    title="Мои питомцы"
    system-title="pet"
    :items="pets"
    :columns="columns"
    :filters="filters"
    @add="$emit('add')"
  />
</template>

<script>
import DataTable from './DataTable.vue';

export default {
  components: { DataTable },
  props: ['pets'],
  data() {
    return {
      columns: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
        { field: 'pet_type.type_name', label: 'Вид' },
        { field: 'birthdate', label: 'Дата рождения', formatter: this.formatDate },
        { field: 'gender', label: 'Пол' },
      ],
      filters: [
        { field: 'name', label: 'Имя' },
        { field: 'breed', label: 'Порода' },
        { field: 'gender', label: 'Пол', type: 'select', options: ['Мужской', 'Женский'] },
        { field: 'birthdate__start', label: 'Дата рождения (с)', type: 'date' },
        { field: 'birthdate__end', label: 'Дата рождения (по)', type: 'date' },
      ],
    };
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
  },
};
</script>
