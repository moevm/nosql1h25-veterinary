// src/api/entity.js
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api/filter'

export async function filterEntity(entityName, filters = {}) {
    const response = await axios.get(`${API_URL}/${entityName}`, {
        data: filters
    })
    return response.data
}
