// src/api/auth.js
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api/users'

export async function loginUser({ login, password }) {
    const response = await axios.post(`${API_URL}/login`, {
        login,
        password
    })
    return response.data
}

export async function registerUser(payload) {
    const response = await axios.post(`${API_URL}/register`, payload)
    return response.data
}

export async function getUserById(id) {
    const response = await axios.get(`${API_URL}/user`, {
        data: { id }
    })
    return response.data
}
