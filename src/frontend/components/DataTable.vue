<template>
  <div class="data-table">
    <div class="table-header">
      <h2>{{ title }}</h2>
      <div class="table-controls">
        <button v-if="allowCreate" @click="onCreate" class="btn btn-primary">
          Добавить
        </button>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Поиск..."
          class="search-input"
        />
      </div>
    </div>
    
    <table>
      <thead>
        <tr>
          <th v-for="column in columns" :key="column.key">
            {{ column.title }}
          </th>
          <th v-if="hasActions">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.id">
          <td v-for="column in columns" :key="column.key">
            {{ item[column.key] }}
          </td>
          <td v-if="hasActions" class="actions">
            <button @click="onEdit(item)" class="btn btn-edit">✏️</button>
            <button @click="onDelete(item)" class="btn btn-delete">🗑️</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    items: Array,
    columns: Array,
    allowCreate: Boolean,
    hasActions: Boolean,
  },
  data() {
    return {
      searchQuery: '',
    };
  },
  computed: {
    filteredItems() {
      if (!this.searchQuery) return this.items;
      return this.items.filter(item => 
        Object.values(item).some(
          val => String(val).toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  methods: {
    onCreate() {
      this.$emit('create');
    },
    onEdit(item) {
      this.$emit('edit', item);
    },
    onDelete(item) {
      this.$emit('delete', item);
    },
  },
};
</script>

<style scoped>
.data-table {
  margin: 20px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f8f9fa;
  font-weight: 600;
}

.actions {
  display: flex;
  gap: 8px;
}

.btn {
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #42b983;
  color: white;
}

.btn-edit {
  background-color: #ffc107;
  color: white;
}

.btn-delete {
  background-color: #dc3545;
  color: white;
}

.search-input {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-left: 10px;
}
</style>
