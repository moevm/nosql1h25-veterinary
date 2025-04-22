// src/api/entity.js
import axios from 'axios'

const API_URL = 'http://172.18.21.37:5000/api/filter'

export async function filterEntity(entityName, filters = {}) {
    const response = await axios.post(`${API_URL}/${entityName}`, {
        data: filters
    })
    return response.data
}
