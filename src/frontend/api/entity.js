// src/api/entity.js
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api/filter'
const CREATE_URL = 'http://127.0.0.1:5000/api/create'


export async function filterEntity(entityName, filters = {}) {
    const response = await axios.post(`${API_URL}/${entityName}`, {
        data: filters
    })
    return response.data
}
export function getDoctorById() {

}
export async function addEntity(entityName, data = {}) {
    const response = await axios.post(`${CREATE_URL}/${entityName}`, data);
    return response.data; // Или можно вернуть response, если нужен код состояния
}