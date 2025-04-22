import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import DoctorPage from '../components/DoctorPage.vue'
import AdminPage from '../components/AdminPage.vue'
import AdminPageBranch from '@/components/AdminPageBranch.vue'
import AdminPageReport from '@/components/AdminPageReport.vue'
import AdminPageServices from '@/components/AdminPageServices.vue'
import AdminTables from '@/components/AdminTables.vue'
import UserPage from '../components/UserPage.vue'
import AdminPageUsers from "@/components/AdminPageUsers.vue";

const routes = [
    { path: '/', component: LoginPage },
    { path: '/doctor', component: DoctorPage },
    { path: '/admin', component: AdminPage },
    { path: '/admin/User', component: AdminPageUsers },
    { path: '/admin/Procedure', component: AdminPageServices },
    { path: '/admin/Office', component: AdminPageBranch },
    { path: '/admin/Appointment', component: AdminPageReport },
    { path: '/user', component: UserPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
