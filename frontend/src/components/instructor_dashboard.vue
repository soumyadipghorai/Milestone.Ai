<template>
    <div class="landing-page"  :style="{ backgroundColor: 'var(--primary-background-color)' }"> 
        <div class="container mb-0">
            <nav class="navbar navbar-expand-md navbar-container py-2 px-0">
                <a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a>
                <button class="navbar-toggler toggle-button-style" type="button" data-toggle="collapse" data-target="#toggleCollapse" aria-expanded="false" aria-controls="toggleCollapse"> 
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="container-xxl px-0">
                    <div class="collapse navbar-collapse text-center justify-content-end" id="toggleCollapse">
                        <ul class="navbar-nav d-flex align-items-center">
                            <li class="h-100 nav-link"> 
                                <router-link :to="isLoggedIn ? `/student-dashboard/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
                                    Dashboard
                                </router-link>
                            </li> 
                            <li>
                                <div class="dropdown h-100 nav-link d-flex align-items-center py-0">
                                    <a class=" dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        <img src="@/assets/notification.png" alt="" width="30">
                                        <span class="position-absolute top-10 start-90 translate-middle p-2 bg-danger border border-light rounded-circle">
                                            <span class="visually-hidden">New alerts</span>
                                        </span>
                                    </a>

                                    <ul class="dropdown-menu">
                                        <li><a class="dropdown-item" href="#">Action</a></li>
                                        <li><a class="dropdown-item" href="#">Another action</a></li>
                                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                                    </ul>
                                </div>
                            </li>
                            <li><a class="h-100 nav-link d-flex align-items-center" href="/login"> 
                                <button v-if="isLoggedIn" class="btn btn-primary btn-md" @click="logout">
                                    Log Out
                                </button>
                                <router-link v-else :to="`/login`" class="btn btn-primary">
                                    log In
                                </router-link>
                            </a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="loading vh-100 d-flex justify-content-center align-items-center" v-if="loading">
                <dotlottie-player src="https://lottie.host/60c22126-f9b3-4a76-881a-177db0874030/dvfbPo4NAa.lottie" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player>
            </div>
            <div class="done" v-else>
                <div class="dashboard-body my-4" :class="{ blurred: blocked }" v-if="dashboardData.status.registered">
                    <div class="row mx-0 my-4">
                        <div class="col-lg-6">
                            <div class="card p-4" :style="{backgroundColor : 'var(--primary-dark-color)', height: '50vh'}">
                                <h4 class="lh-2 my-2 text-light">Leader Board</h4>
                                <div class="leader-board-item overflow-auto">
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp4.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Aniket 
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            160 commits 
                                        </div>
                                    </div>
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp1.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Soumyadip Ghorai
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            150 commits 
                                        </div>
                                    </div>
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp2.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Aditya Aman
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            100 commits 
                                        </div>
                                    </div>
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp3.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Mohak
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            0 commits 
                                        </div>
                                    </div>
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp3.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Mohak
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            0 commits 
                                        </div>
                                    </div>
                                    <div class="row m-0" :style="{borderBottom : '1px dotted var(--primary-background-color)'}">
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp3.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            Mohak
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            0 commits 
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="card  p-4"  :style="{height: '50vh'}">
                                <h4 class="lh-2 my-2 p-2">Student details</h4>
                                <div class="student-info overflow-auto">
                                    <div class="row my-2">
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-danger rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-success rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row my-2">
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-warning rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-success rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row my-2">
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-warning rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-success rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row my-2">
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-warning rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="card p-0" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                <div class="row m-0">
                                                    <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                                        <img src="@/assets/pfp2.png" alt="" width="30">
                                                    </div>
                                                    <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                                        Soumyadip
                                                    </div>
                                                    <div class="col-2 my-2 text-light d-flex justify-content-center align-items-center bg-success rounded-circle">
                                                        3
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row m-0">
                        <div class="col-lg-7">
                            <div class="card p-4" :style="{height: '60vh'}">
                                <div class="row mb-4 mx-0">
                                    <div class="col-6 p-0 d-flex justify-content-start align-items-center">
                                        <h4 class="lh-2">Student progress</h4>
                                    </div>
                                    <div class="col-6 p-0 d-flex justify-content-end align-items-center">
                                        <div class="dropdown-center">
                                            <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                                Semester
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a class="dropdown-item" href="#">Semester 1</a></li>
                                                <li><a class="dropdown-item" href="#">Semester 2</a></li>
                                                <li><a class="dropdown-item" href="#">Semester 3</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                                <div class="student-progress-bar overflow-auto px-2">
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                    <div class="row my-3">
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped" style="width: 10%"></div>
                                            </div> 
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="card p-4 h-100 text-light bg-primary-subtle text-dark" :style="bgStyle1">
                                <h4 class="lh-2 my-2">Status Updates</h4>
                                <div id="carouselExampleIndicators" class="carousel slide h-100">
                                    <div class="carousel-indicators">
                                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button> 
                                    </div>
                                    <div class="carousel-inner h-100">
                                        <div class="carousel-item mx-2 bg-dark active card p-4 h-100 text-light">
                                            <div class="text-section mx-4">
                                                <div class="tag row mb-4 mt-2">
                                                    <div class="col-4 p-2 rounded-2 mx-2 d-flex align-items-center" :style="{backgroundColor : 'var(--in-progress-bg-color)'}">Feedback</div>
                                                    <div class="col-4 p-2 rounded-2 mx-2 d-flex align-items-center" :style="{backgroundColor : 'var(--done-bg-color)'}">Bugs</div> 
                                                </div>
                                                <h5 class="lh-2 my-2">Please Extend the deadlines for 10 days...</h5>
                                                <p class="text-secondary mb-4">20.08.2024</p>
                                                <div class="row m-0">
                                                    <div class="col-6 p-0 d-flex justify-content-start">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/like.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b>8+</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-6 p-0 d-flex justify-content-end">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/comment.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b>7+</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="carousel-item bg-dark active card p-4 h-100 text-light">
                                            <div class="text-section mx-4">
                                                <div class="tag row mb-4 mt-2">
                                                    <div class="col-4 p-2 rounded-2 mx-2 d-flex align-items-center" :style="{backgroundColor : 'var(--in-progress-bg-color)'}">Feedback</div>
                                                    <div class="col-4 p-2 rounded-2 mx-2 d-flex align-items-center" :style="{backgroundColor : 'var(--done-bg-color)'}">Bugs</div> 
                                                </div>
                                                <h5 class="lh-2 my-2">Please Extend the deadlines for 10 days...</h5>
                                                <p class="text-secondary mb-4">20.08.2024</p>
                                                <div class="row m-0">
                                                    <div class="col-6 p-0 d-flex justify-content-start">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/like.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b>8+</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-6 p-0 d-flex justify-content-end">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/comment.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b>7+</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div> 
                                    </div>
                                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Previous</span>
                                    </button>
                                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Next</span>
                                    </button>
                                </div>
                            </div> 
                        </div>
                    </div>
                </div>
    
                <div class="dashboard-body my-4" v-else>
                    <h4 class="lh-2"> You Have not registered to any project yet!!</h4>
                    <p class="text-secondary lh-2">Please choose one from the available projects...</p> 
                    <div class="available-projects-container my-4">
                        <div class="row" > 
                            <div 
                                v-for="(project, index) in dashboardData.status.new_project" 
                                :key="index" 
                                class="col-12 col-md-4 mb-4"
                            >
                                <div class="card h-100">
                                    <div class="card-body">
                                        <h5 class="card-title">{{ project.name }}</h5>
                                        <p class="card-text">{{ project.description.length > 200 ? project.description.slice(0, 200) + '...' : project.description  }}</p>
                                    </div>
                                    <div class="card-footer text-center">
                                        <button class="btn btn-primary mx-2" @click="redirectToProjectDetails(project.id)">Edit</button>
                                        <button class="btn btn-outline-secondary" @click="enrollInProject(project.id)">Enroll</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>   
    import Swal from 'sweetalert2'; 
     import {getInstructorDashboard, projectEnroll} from '@/services/appService';
    export default { 
        // name: 'Home',
        data() {
            return {                
                user_id : null,
                role: null,
                blocked: true, 
                selectedOption: "dashboard",     
                dashboardData: null,  
                loading: true
            };
        },
        computed: { 
            isLoggedIn() { 
                this.user_id = localStorage.getItem('user_id');
                return !!localStorage.getItem('user_id');
            },
        } ,
        methods: {
            logout() {
                localStorage.removeItem('user_id'); 
                localStorage.removeItem('access_token');  
                localStorage.removeItem('role');  
                this.$router.push('/login');  
            },
            selectOption(option) {
                this.selectedOption = option;  
            },
            async fetchDashboard() {
                try {
                    const response = await getInstructorDashboard(this.user_id);
                    this.dashboardData = response;  
                    console.log(response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            redirectToProjectDetails(projectId) {
                this.$router.push(`/project-details/${projectId}`);
            },
            async enrollInProject(projectId) {
                try {
                    const response = await projectEnroll({
                        user_id: this.user_id, 
                        role: this.role, 
                        project_id: projectId
                    }); 
                    this.dashboardData.status.registered = true;
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }
        },
        mounted() { 
            const storedUserId = localStorage.getItem('user_id');
            const storedRole = localStorage.getItem('role');
        
            if (storedUserId && storedRole) {
                this.user_id = storedUserId;
                this.role = storedRole;

                if (this.role === 'student') { 
                    // alert("You don't have access to this page!"); 
                    Swal.fire({
                        title: 'Access Denied',
                        text: "You don't have access to this page!",
                        icon: 'error',
                        confirmButtonText: 'OK',
                    });


                    setTimeout(() => {
                        this.$router.push('/login');
                    }, 2000);

                } else {
                    this.blocked = false; 
                }

            } else { 
                this.$router.push('/login');
            }

            this.fetchDashboard();
        },
    };
</script>