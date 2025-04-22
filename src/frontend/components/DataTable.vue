<template>
  <div class="data-table">
    <!-- Заголовок и кнопка добавления -->
    <div class="table-header">
      <h2>{{ title }}</h2>
      <button v-if="showAddButton" @click="showAddModal = true" class="add-button">
        Добавить
      </button>
    </div>

    <!-- Фильтры -->
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
      <button @click="loadItems" class="filter-button">Отфильтровать</button>
    </div>

    <!-- Таблица -->
    <table>
      <thead>
        <tr>
          <th v-for="column in columns" :key="column.field">{{ column.label }}</th>
          <th v-if="showActions">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.id">
          <td v-for="column in columns" :key="column.field">
            {{ formatValue(item[column.field], column) }}
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Модалка добавления -->
    <div v-if="showAddModal" class="modal-overlay">
      <div class="modal">
        <h3>Добавить {{ title }}</h3>
        <form @submit.prevent="handleAdd">
          <div v-for="column in addFormColumns" :key="column.field" class="form-group">
            <label :for="`add-${column.field}`">{{ column.label }}</label>
            <input
              v-if="!column.type || column.type === 'text'"
              :id="`add-${column.field}`"
              v-model="newItem[column.field]"
              :type="column.type || 'text'"
              :required="column.required !== false"
            />
            <select
              v-else-if="column.type === 'select'"
              :id="`add-${column.field}`"
              v-model="newItem[column.field]"
              :required="column.required !== false"
            >
              <option v-for="option in column.options" :key="option.value" :value="option.value">
                {{ option.label }}
              </option>
            </select>
          </div>

          <div class="modal-actions">
            <button type="button" @click="showAddModal = false" class="cancel-button">Отмена</button>
            <button type="submit" class="submit-button">Добавить</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { filterEntity, addEntity } from "@/api/entity.js";

export default {
  props: {
    title: String,
    systemTitle: String,
    items: Array,
    columns: Array,
    filters: Array,
    showAddButton: { type: Boolean, default: false },
    showActions: { type: Boolean, default: true },
    addFormConfig: { type: Object, default: () => ({}) },
  },
  data() {
    return {
      filterValues: {},
      localItems: [],
      showAddModal: false,
      newItem: {}
    };
  },
  computed: {
    filteredItems() {
      return this.localItems;
    },
    addFormColumns() {
      return this.columns.map(col => ({
        ...col,
        type: this.addFormConfig[col.field]?.type || col.type,
        options: this.addFormConfig[col.field]?.options,
        required: this.addFormConfig[col.field]?.required !== false
      }));
    }
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
    async handleAdd() {
      try {
        await addEntity(this.systemTitle, this.newItem);
        this.showAddModal = false;
        this.newItem = {};
        await this.loadItems();
        this.$emit('added');
      } catch (error) {
        console.error("Ошибка добавления:", error);
      }
    },
    formatValue(value, column) {
      return column.formatter ? column.formatter(value) : value;
    }
  },
  created() {
    this.loadItems();
  }
};
</script>

<style scoped>
/* 🎨 Используем стили из обоих шаблонов — смержены */

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

/* Модальное окно */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 500px;
  max-width: 90%;
  max-height: 90vh;
  overflow-y: auto;
}

.modal h3 {
  margin-top: 0;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.cancel-button {
  background-color: #f44336;
  color: white;
}

.submit-button {
  background-color: #4caf50;
  color: white;
}
</style>
