<template>
  <DataTable
    title="Услуги"
    system-title="procedure"
    :items="items"
    :columns="columns"
    :filters="filters"
    @add="$emit('addProcedure')"
    @edit="$emit('editProcedure', $event)"
    @delete="$emit('deleteProcedure', $event)"
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
    };
  },
};
</script>