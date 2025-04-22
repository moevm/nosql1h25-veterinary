import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import DoctorPage from '../components/DoctorPage.vue'
import AdminPageBranch from '@/components/AdminPageBranch.vue'
import AdminPageReport from '@/components/AdminPageReport.vue'
import AdminPageServices from '@/components/AdminPageServices.vue'
import UserPageGetPet from "@/components/UserPageGetPet.vue";
import UserPageMakeAppointment from "@/components/UserPageMakeAppointment.vue";
import UserPageAppointments from "@/components/UserPageАppointments.vue";
import UserPage from '../components/UserPage.vue'
import AdminPageUsers from "@/components/AdminPageUsers.vue";
import AdminPagePet from "@/components/AdminPagePet.vue";

const routes = [
    { path: '/', component: LoginPage },
    { path: '/doctor', component: DoctorPage },
    { path: '/admin',  redirect: '/admin/User' },
    { path: '/admin/User', component: AdminPageUsers },
    { path: '/admin/Pet', component: UserPageGetPet },
    { path: '/admin/Bookings', component: UserPageMakeAppointment },
    { path: '/admin/AppointmentUser', component: UserPageAppointments },

    { path: '/admin/Procedure', component: AdminPageServices },
    { path: '/admin/Office', component: AdminPageBranch },
    { path: '/admin/Appointment', component: AdminPageReport },
    { path: '/admin/Pet', component: AdminPagePet },
    { path: '/user', component: UserPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
