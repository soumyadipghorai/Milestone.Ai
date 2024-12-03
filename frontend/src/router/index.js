import { createRouter, createWebHistory } from 'vue-router'
import login from '@/components/login.vue'
import home from '@/components/home.vue'
import register from '@/components/register.vue'
import admin_dashboard from '@/components/admin_dashboard.vue'
import student_dashboard from '@/components/student_dashboard.vue'
import support_dashboard from '@/components/support_dashboard.vue'
import instructor_dashboard from '@/components/instructor_dashboard.vue'
import project from '@/components/project.vue'
import project_details from '@/components/project_details.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: home, 
            props: true, 
        }, 
        {
            path:'/login',
            name:'login',
            component:login, 
            props: true, 
        },
        {
            path:'/register',
            name:'register',
            component:register, 
            props: true, 
        },
        {
            path:'/admin-dashboard/:userId',
            name:'admin_dashboard',
            component:admin_dashboard, 
            props: true, 
            meta: { requiresAuth: true }
        },
        {
            path:'/student-dashboard/:userId',
            name:'student_dashboard',
            component:student_dashboard, 
            props: true, 
            meta: { requiresAuth: true }
        },
        {
            path:'/support-dashboard/:user_id',
            name:'support_dashboard',
            component:support_dashboard, 
            props: true, 
            meta: { requiresAuth: true }
        },
        {
            path:'/project/:project_id/:user_id',
            name:'project',
            component:project, 
            props: true, 
            meta: { requiresAuth: true }
        },
        {
            path:'/instructor-dashboard/:userId',
            name:'instructor_dashboard',
            component:instructor_dashboard, 
            props: true, 
            meta: { requiresAuth: true }
        },
        {
            path:'/project-details/:project_id',
            name:'project_details',
            component:project_details, 
            props: true, 
            meta: { requiresAuth: true }
        }
    ]
})

router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('user_id'); // Check auth status
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!isAuthenticated) {
        next('/login'); // Redirect to login if not authenticated
        } else {
        next(); // Allow access if authenticated
        }
    } else {
        next(); // Always allow access to non-protected routes
    }
});


export default router