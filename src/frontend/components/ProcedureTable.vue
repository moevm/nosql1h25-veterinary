<template>
  <DataTable
    title="Услуги"
    system-title="procedure"
    :items="items"
    :columns="columns"
    :filters="filters"
    :showAddButton="true"
    :addFormConfig="addFormConfig"
    @add="handleAddProcedure"
  />
</template>

<script>
import DataTable from './DataTable.vue';

export default {
  components: { DataTable },
  props: ['items'],
  data() {
    return {
      columns: [
        { field: 'name', label: 'Название' },
        { field: 'cost', label: 'Стоимость', formatter: v => v.toFixed(2) },
        { field: 'description', label: 'Описание' },
      ],
      filters: [
        { field: 'name', label: 'Название' },
        { field: 'cost__start', label: 'Стоимость (от)', type: 'number' },
        { field: 'cost__end', label: 'Стоимость (до)', type: 'number' },
        { field: 'description', label: 'Описание' },
      ],
      addFormConfig: {
        name: { required: true },
        cost: { type: 'number', required: true },
        description: { required: true },
        available: { 
          type: 'select', 
          options: [
            { value: true, label: 'Доступна' },
            { value: false, label: 'Недоступна' }
          ],
          required: true 
        }
      }
    };
  },
  methods: {
    handleAddProcedure(newProcedure) {
      console.log('Добавление новой услуги:', newProcedure);
     
    }
  }
};
</script>
