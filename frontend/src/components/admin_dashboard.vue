<template>
    <div class="landing-page"  :style="{ backgroundColor: 'var(--primary-background-color)' }"> 
        <div class="container">
            <nav class="navbar navbar-expand-md navbar-container py-2 px-0">
                <a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a>
                <button class="navbar-toggler toggle-button-style" type="button" data-toggle="collapse" data-target="#toggleCollapse" aria-expanded="false" aria-controls="toggleCollapse"> 
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="container-xxl px-0">
                    <div class="collapse navbar-collapse text-center justify-content-end" id="toggleCollapse">
                        <ul class="navbar-nav d-flex align-items-center">
                            <li class="h-100 nav-link"> 
                                <router-link :to="isLoggedIn ? `/admin-dashboard/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
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
                <!-- <dotlottie-player src="https://lottie.host/60c22126-f9b3-4a76-881a-177db0874030/dvfbPo4NAa.lottie" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player> -->
                loading...
            </div>
            <div class="done" v-else>
                <div class="dashboard-body my-4" :class="{ blurred: blocked }" v-if="dashboardData">
                    <div class="row mx-0 my-4">
                        <div class="col-lg-8">
                            <div class="card p-4" :style="{height: '50vh'}">
                                <h4 class="lh-2 my-2">Instructor Mapping</h4>
                                <p class="lh-2"><b>{{dashboardData.project_details.total_instructors}} total,</b>Instructors available</p>
                                <div class="row m-0 w-100 py-2 table-header" :style="{borderBottom : '1px dotted var(--dark-border-light)'}">
                                    <div class="col-3 d-flex align-items-center">
                                        <b>instructore Name</b>
                                    </div>
                                    <div class="col-2 d-flex align-items-center"><b>Student ID</b></div>
                                    <div class="col-2 d-flex align-items-center"><b>Milestones</b></div>
                                    <div class="col-3 row m-0 rounded-end"> 
                                        <b>Status</b>
                                    </div>
                                    <div class="col-2 d-flex align-items-center">
                                        <b>Finish Date</b>
                                    </div>
                                </div>
                                <div class="mapping-table w-100 overflow-auto">
                                    <div class="row m-0 w-100 py-2" :style="{borderBottom : '1px dotted var(--dark-border-light)'}" v-for="(projectDetails, projectIndex) in dashboardData.project_details.project_list" :key = "'project-' + projectIndex">
                                        <div class="col-3 row mx-0">
                                            <div class="col-3">
                                                <img src="@/assets/pfp1.png" alt="" width="30">
                                            </div>
                                            <div class="col-9 d-flex align-items-center">{{projectDetails.instructor_name}}</div>
                                        </div>
                                        <div class="col-2 d-flex align-items-center">{{projectDetails.total_student}}</div>
                                        <div class="col-2 d-flex align-items-center">{{projectDetails.total_milestones}}</div>
                                        <div class="col-3 row m-0 rounded-end" :style="{backgroundColor: 'var(--in-progress-bg-color)'}">
                                            <div class="col-2 d-flex align-items-center justify-content-center">
                                                <img src="@/assets/in-progress.png" alt="">
                                            </div>
                                            <div class="col-9 d-flex align-items-center">{{projectDetails.status}}</div>
                                        </div>
                                        <div class="col-2 d-flex align-items-center">{{projectDetails.finish_date}} days</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="card p-4 h-100">
                                <div class="text-section">
                                    <h4 class="lh-2 my-2">Project Details</h4>
                                    <p class="lh-2 text-secondary">Select and upload project details</p>
                                </div>
                                <form  @submit.prevent="uploadFile">
                                    <div class="mb-3"> 
                                        <input type="file" id="fileInput" accept="application/pdf" class="form-control h-100" row="2" @change="onFileChange">
                                    </div> 
                                    <div class="form-check my-2">
                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" :style="{backgroundColor: 'transparent'}" required>
                                        <label class="form-check-label text-secondary" for="flexCheckDefault">
                                            Milestone would be created using AI
                                        </label>
                                    </div>
                                    <div class="row m-0"> 
                                        <button type="submit" class="btn btn-outline-primary mx-0">
                                            <span v-if="fileUploading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                                Create Project
                                        </button> 
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="row mx-0 my-2">
                        <div class="col-lg-7">
                            <div class="card p-4">
                                <div class="row m-0">
                                    <div class="col-7 d-flex align-items-start">
                                        <h4 class="lh-2 mx-4">Engagement Tracker</h4>
                                    </div>
                                    <div class="col-5">
                                        <!-- <div class="drop-down-container d-flex justify-content-end align-items-center">
                                            <div class="dropdown">
                                                <button class="btn btn-sm btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                                    Semester
                                                </button>
                                                <ul class="dropdown-menu">
                                                    <li><a class="dropdown-item" href="#">Semester 1</a></li>
                                                    <li><a class="dropdown-item" href="#">Semester 2</a></li>
                                                    <li><a class="dropdown-item" href="#">Semester 3</a></li>
                                                </ul>
                                            </div>
                                        </div> -->
                                        <div class="updated-container d-flex justify-content-end align-items-center mt-2">
                                            <p class="text-secondary fw-light fs-6">All results updated </p>
                                        </div>
                                    </div>
                                </div>
                                <Bar :data="barChartData" :options="barChartOptions"/>
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="card p-4 h-100 bg-primary-subtle" >
                                <h4 class="lh-2 my-2">Status Updates</h4>
                                <div id="carouselExample" class="carousel slide">
                                    <div class="carousel-inner">
                                        <div 
                                            class="carousel-item mx-2 bg-dark card p-4 text-light" 
                                            v-for="(feedback, feedbackIndex) in dashboardData.all_feedback"
                                            :key="'feedback-' + feedbackIndex"
                                            :class="{'active': feedbackIndex === currentSlideIndex}"
                                        >
                                            <div class="text-section mx-4"> 
                                                <div class="tag row mb-4 mt-2">
                                                    <div class="col-4 p-2 rounded-2 mx-2 d-flex align-items-center" 
                                                        :style="{backgroundColor : 'var(--in-progress-bg-color)'}">
                                                        {{feedback.tag}}
                                                    </div> 
                                                </div>
                                                <h5 class="lh-2 my-2">
                                                    {{ feedback.feedback.length > 100 ? feedback.feedback.slice(0, 100) + '...' : feedback.feedback }}
                                                </h5> 
                                                <p class="text-secondary mb-4">{{ feedback.feedback_date }}</p>
                                                
                                                <div class="row m-0">
                                                    <div class="col-6 p-0 d-flex justify-content-start">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/like.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b>{{ feedback.like_count }}</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-6 p-0 d-flex justify-content-end">
                                                        <div class="like m-0 w-100">
                                                            <div class="col-2 p-0">
                                                                <img src="@/assets/comment.png" alt="" width="20">
                                                            </div>
                                                            <div class="col-10">
                                                                <b> {{ feedback.comment_count }}</b> students
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev" @click="goToPrevSlide">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Previous</span>
                                    </button>
                                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next" @click="goToNextSlide">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Next</span>
                                    </button>
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
    import { Line, Doughnut, Bar } from 'vue-chartjs';
    import {getAdminDashboard, projectReportUpload} from '@/services/appService';
    import Swal from 'sweetalert2'; 

    import {
        Chart as ChartJS, Title, Tooltip, Legend, LineElement, BarElement,
        ArcElement, CategoryScale, LinearScale, Filler, PointElement,
    } from 'chart.js';
 
    ChartJS.register( 
        Title, Tooltip, Legend, LineElement, ArcElement, 
        CategoryScale, LinearScale, Filler, PointElement, BarElement
    );

 
    export default {
        // name: 'admin-dashboard',
        components: {
            Doughnut, Line, Bar
        },
        data() {
            return {      
                user_id : null,
                role: null,
                blocked: true,    
                selectedOption: "dashboard",  
                selectedFile: null,  
                fileUploading: false,    
                currentSlideIndex: 0, 
                dashboardData: null,
                loading: false,
                barChartData: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                    datasets: [
                        {
                            label: 'Projects',
                            data: [10, 20, 30, 25, 15, 35],
                            backgroundColor: 'rgba(0, 123, 255, 0.5)',  
                            borderColor: '#007BFF',
                            borderWidth: 1,
                        },
                        {
                            label: 'Students',
                            data: [5, 10, 15, 20, 25, 30],
                            backgroundColor: 'rgba(52, 58, 64, 0.5)',  
                            borderColor: '#343A40',
                            borderWidth: 1,
                        },
                    ],
                },
                barChartOptions: {
                    responsive: true,
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Months',
                            },
                            grid: {
                                display: false,
                            },
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Numbers',
                            },
                            beginAtZero: true,
                        },
                    },
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                        },
                    },
                },
            };
        },
        computed: { 
            isLoggedIn() { 
                this.user_id = localStorage.getItem('user_id');
                return !!localStorage.getItem('user_id');
            },
            selectOption(option) {
                this.selectedOption = option;  
            },
        }, 
        methods: {
            logout() {
                localStorage.removeItem('user_id'); 
                localStorage.removeItem('access_token');  
                localStorage.removeItem('role');  
                this.$router.push('/login');  
            },
            onFileChange(event) {
                this.selectedFile = event.target.files[0];
            },
            async uploadFile() {
                if (!this.selectedFile) {
                    alert("No file selected!");
                    return;
                } 
                this.fileUploading = true;
                try {
                    const response = await projectReportUpload(this.selectedFile);
                    // console.log("Upload success:", response);
                    alert("New project created!");
                } catch (error) {
                    console.error("Upload failed:", error);
                } finally {
                    this.fileUploading = false; 
                }
            }, 
            async fetchDashboard() {
                try {
                    const response = await getAdminDashboard(this.user_id);
                    this.dashboardData = response;  
                    this.barChartData = response.progress_report;
                    console.log(response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            goToPrevSlide() {
                if (this.currentSlideIndex > 0) {
                    this.currentSlideIndex--;
                } else {
                    this.currentSlideIndex = this.dashboardData.all_feedback.length - 1;
                }
            },  
            goToNextSlide() {
                if (this.currentSlideIndex < this.dashboardData.all_feedback.length - 1) {
                    this.currentSlideIndex++;
                } else {
                    this.currentSlideIndex = 0;
                }
            },
        },
        mounted() { 
            const storedUserId = localStorage.getItem('user_id');
            const storedRole = localStorage.getItem('role');
        
            if (storedUserId && storedRole) {
                this.user_id = storedUserId;
                this.role = storedRole;

                if (this.role !== 'admin') {  
                    Swal.fire({
                        title: 'Access Denied',
                        text: "You don't have access to this page!",
                        icon: 'error',
                        confirmButtonText: 'OK',
                    });
                    console.log(this.role)


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