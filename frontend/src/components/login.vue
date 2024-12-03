<template> 
  <!-- for alt nav bar -->
    <div class="row m-0">
        <div class="col-sm-6 order-2 order-sm-1" :style="{ backgroundColor: 'var(--primary-background-color)' }"></div>
        <div class="col-sm-6 order-1 order-sm-2">
            <nav class="navbar navbar-expand-md navbar-container py-2 px-0 mx-4 my-2">
                <a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a>
                <button class="navbar-toggler toggle-button-style" type="button" data-toggle="collapse" data-target="#toggleCollapse" aria-expanded="false" aria-controls="toggleCollapse"> 
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="container-xxl px-0">
                    <div class="collapse navbar-collapse text-center justify-content-end" id="toggleCollapse">
                        <ul class="navbar-nav"> 
                            <button 
                                class="h-100 nav-link d-flex align-items-center" 
                                :class="{ 'selected-role': selectedRole === 'student' }" @click="selectRole('student')"
                            >
                                Student
                            </button>
                            <button 
                                class="h-100 nav-link d-flex align-items-center" 
                                :class="{ 'selected-role': selectedRole === 'admin' }" @click="selectRole('admin')"
                            >
                                Admin
                            </button>
                            <button 
                                class="h-100 nav-link d-flex align-items-center" 
                                :class="{ 'selected-role': selectedRole === 'instructor' }" @click="selectRole('instructor')"
                            >
                                Instructor
                            </button>
                            <button 
                                class="h-100 nav-link d-flex align-items-center" 
                                :class="{ 'selected-role': selectedRole === 'support' }" @click="selectRole('support')"
                            >
                                Support
                            </button>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    </div>
    <div class="row vh-100 m-0">
        <div class="col-sm-6 p-4" :style="{ backgroundColor: 'var(--primary-background-color)' }"> 
            <div class="image-container mt-4 d-flex justify-content-center">
                <img src="../assets/login_page_base.png" alt="Register Image" max-width=300 height=400>
            </div>
            <div class="welcome-text mt-4 d-flex justify-content-center">
                <h2 class="lh-1">Welcome to the log in portal</h2> 
            </div>
        </div>
        <div class="col-sm-6 p-4 mt-4 d-flex justify-content-center"> 
            <div class="main-section w-100 p-lg-4 m-lg-4 p-sm-2 m-sm-2">
                <div class="login-info row my-4">
                    <div class="col-2">
                        <img src="../assets/pfp1.png" alt="Profile Icon" class="img-fluid">
                    </div>
                    <div class="col-10 d-flex align-items-center justify-content-start">
                        <h3 class="lh-1">Log in</h3>
                    </div> 
                </div>
                <form @submit.prevent="handleLogin">
                    <div class="form-container w-100">
                        <div class="mb-3">
                            <label for="exampleFormControlInput1" class="form-label">Enter Email address</label>
                            <input type="email" class="form-control" placeholder="Email address..." v-model="email"
                            :style="{ backgroundColor: 'var(--primary-blue-form-input-color)' }">
                        </div>
                        <div class="mb-3">
                            <label for="exampleFormControlInput1" class="form-label">Enter Password</label>
                            <input type="password" class="form-control" placeholder="Password..." v-model="password"
                            :style="{ backgroundColor: 'var(--primary-blue-form-input-color)' }">
                        </div>
                    </div>
                    <div class="btn-group w-100">
                        <div class="row m-0 w-100 gap-sm-2 gap-1">
                            <div class="col-lg-2 col-md-3 col-sm-3 col-3 d-flex justify-content-start m-0 p-0">
                                <button class="btn btn-primary btn-md" type="submit">Log In</button>
                            </div>
                            <div class="col-lg-2 col-md-3 col-sm-3 col-3 d-flex justify-content-start m-0 p-0"> 
                                <router-link to="/register" class="btn btn-outline-secondary btn-md">
                                    Register
                                </router-link>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { loginAdmin } from "@/services/authService";

export default {
    data() {
        return { 
            userId: '', 
            email: "", 
            password: "", 
            selectedRole: "student",
        };
    },
    methods: { 
        selectRole(role) {
            this.selectedRole = role;  
        },
        async handleLogin() {
            try {
                const response = await loginAdmin({ 
                    email: this.email,
                    password: this.password,
                    role: this.selectedRole
                });

                // console.log(response)
        
                localStorage.setItem("access_token", response.access_token);
                localStorage.setItem("user_id", response.user_id);
                localStorage.setItem("role", response.role);

                alert("Login successful!");
                
                if (this.selectedRole == 'student') {
                    this.$router.push(`/student-dashboard/${response.user_id}`);
                }
                else if (this.selectedRole == 'admin') {
                    this.$router.push(`/admin-dashboard/${response.user_id}`);
                }
                else if (this.selectedRole == 'instructor') {
                    this.$router.push(`/instructor-dashboard/${response.user_id}`);
                }
                else if (this.selectedRole == 'support') {
                    this.$router.push(`/support-dashboard/${response.user_id}`);
                }
                else{
                    this.$router.push(`/`);
                }
            } catch (error) {
                console.error(error);
                alert("Login failed: " + (error.response?.data?.detail || "Unknown error"));
            }
        },
    }, 
    mounted() {
        const storedUser = JSON.parse(localStorage.getItem('user')); // Retrieve from storage
    }, 
}
</script>