<template>
  <div class="data-table">
    <div class="table-header">
      <h2>{{ title }}</h2>
      <button v-if="showAddButton" @click="$emit('add')" class="add-button">
        Добавить
      </button>
    </div>

    <div class="table-filters">
      <div v-for="(filter, index) in filters" :key="index" class="filter-item">
        <label :for="`filter-${index}`">{{ filter.label }}</label>
        <input
          :id="`filter-${index}`"
          :type="filter.type || 'text'"
          v-model="filterValues[filter.field]"
          :placeholder="filter.placeholder || ''"
        />
      </div>

      <!-- 🔘 Кнопка "Отфильтровать" -->
      <button @click="loadItems" class="filter-button">
        Отфильтровать
      </button>
    </div>

    <table>
      <thead>
        <tr>
          <th v-for="column in columns" :key="column.field">
            {{ column.label }}
          </th>
          <th v-if="showActions">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.id">
          <td v-for="column in columns" :key="column.field">
            {{ formatValue(item[column.field], column) }}
          </td>
          <td v-if="showActions" class="actions">
            <button @click="$emit('edit', item)" class="edit-button">
              Редактировать
            </button>
            <button @click="$emit('delete', item)" class="delete-button">
              Удалить
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import {filterEntity} from "@/api/enity.js";

export default {
  props: {
    title: String,
    systemTitle: String,
    items: Array,
    columns: Array,
    filters: Array,
    showAddButton: {
      type: Boolean,
      default: true,
    },
    showActions: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      filterValues: {},
      localItems: [],
    };
  },
  computed: {
    filteredItems() {
      return this.localItems
    },
  },
  methods: {
    async loadItems() {
      try {
        const data = await filterEntity(this.systemTitle, this.filterValues);
        this.localItems = data;
      } catch (error) {
        console.error("Ошибка загрузки данных:", error);
      }
    },
    formatValue(value, column) {
      if (column.formatter) {
        return column.formatter(value);
      }
      return value;
    },
  },
  created() {
    this.loadItems(); // загружаем данные при инициализации
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

.table-filters {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
  flex-wrap: wrap;
}

.filter-item {
  display: flex;
  flex-direction: column;
}

.filter-item label {
  margin-bottom: 5px;
  font-weight: 500;
}

.filter-item input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
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
  background-color: #f4f4f4;
  font-weight: 600;
}

tr:hover {
  background-color: #f9f9f9;
}

.actions {
  display: flex;
  gap: 8px;
}

button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 500;
}

.add-button {
  background-color: #4caf50;
  color: white;
}

.edit-button {
  background-color: #2196f3;
  color: white;
}

.delete-button {
  background-color: #f44336;
  color: white;
}

button:hover {
  opacity: 0.9;
}
</style>
