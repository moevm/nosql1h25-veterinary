<template>
  <DataTable
    title="Мои питомцы"
    :items="pets"
    :columns="columns"
    :allow-create="true"
    :has-actions="true"
    @create="onCreatePet"
    @edit="onEditPet"
    @delete="onDeletePet"
  />
</template>

<script>
import DataTable from '../DataTable.vue';

export default {
  components: { DataTable },
  props: {
    pets: Array,
  },
  data() {
    return {
      columns: [
        { key: 'name', title: 'Имя' },
        { key: 'type', title: 'Вид' },
        { key: 'breed', title: 'Порода' },
        { key: 'age', title: 'Возраст' },
        { key: 'gender', title: 'Пол' },
      ],
    };
  },
  methods: {
    onCreatePet() {
      this.$emit('create-pet');
    },
    onEditPet(pet) {
      this.$emit('edit-pet', pet);
    },
    onDeletePet(pet) {
      this.$emit('delete-pet', pet);
    },
  },
};
</script>
