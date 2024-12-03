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
                            <li class="h-100 nav-link"> 
                                <router-link :to="isLoggedIn ? `/project/${projectID}/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    My Project
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
                            <div class="card p-4 h-100" :style="{backgroundColor : 'var(--primary-dark-color)'}">
                                <h4 class="lh-2 my-2 text-light">Leader Board</h4>
                                <div class="leader-board-item">
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
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3">
                            <div class="card mx-2 p-4">
                                <h4 class="lh-2 my-2">Language Coverage</h4>
                                <p class="lh-1">Showing for  project-1</p>
                                <div class="fit-content">
                                    <Doughnut :data="doughnutChartData" :options="doughnutChartOptions" class="h-100" />
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3">
                            <div class="card mb-3 p-4 text-light text-end d-flex justify-content-center bg-danger" :style="{height: '47.5%'}">
                                <div class="metric-container">
                                    <h2 class="lh-2">Total Reports</h2>
                                    <p class="lh-1">26 pdfs</p>
                                </div>
                            </div>
                            <div class="card mb-3 p-4 text-light text-end d-flex justify-content-center bg-warning" :style="{height: '47.5%'}">
                                <div class="metric-container">
                                    <h2 class="lh-2">Total Commits</h2>
                                    <p class="lh-1">35 commits</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row mx-0 my-2">
                        <div class="col-lg-7">
                            <div class="card p-4">
                                <div class="row m-0">
                                    <div class="col-6 d-flex align-items-start">
                                        <h4 class="lh-2 mx-4">Project Tracker</h4>
                                    </div>
                                    <div class="col-6">
                                        <div class="drop-down-container d-flex justify-content-end align-items-center">
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
    
                                        </div>
                                        <div class="updated-container d-flex justify-content-end align-items-center mt-2">
                                            <p class="text-secondary">Last updated <span>26 mins ago</span></p>
                                        </div>
                                    </div>
                                </div>
                                <Line :data="lineChartData" :options="lineChartOptions" />
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="card p-4 h-100 bg-dark-subtle">
                                <h4 class="lh-2 my-2">Give Feedback</h4>
                                <p class="lh-2 text-secondary">What do you think about current your project and instructor?</p>
                                <form action="">
                                    <div class="mb-3"> 
                                        <textarea class="form-control text-secondary form-text-area border-secondary" id="exampleFormControlTextarea1" placeholder="Type your comment..." rows="5" :style="{backgroundColor: 'transparent'}"></textarea>
                                    </div>
                                    <div class="form-check my-2">
                                        <input class="form-check-input border-secondary" type="checkbox" value="" id="flexCheckDefault" :style="{backgroundColor: 'transparent'}">
                                        <label class="form-check-label text-secondary" for="flexCheckDefault">
                                            It will be sent to the admin for evaluation
                                        </label>
                                    </div>
                                    <button class="btn btn-md text-light" :style="{backgroundColor : 'var(--primary-dark-color)'}">Comment</button>
                                </form>
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
                                <div class="card h-100 p-2">
                                    <div class="card-header">
                                        <p class="text-secondary m-0">Deadline : {{project.deadline}}</p>
                                    </div>
                                    <div class="card-body">
                                        <h5 class="card-title">{{ project.name }}</h5>
                                        <p class="card-text">{{ project.description.length > 200 ? project.description.slice(0, 200) + '...' : project.description  }}</p>
                                        <button class="btn btn-primary px-4" @click="enrollInProject(project.id)">Enroll</button>
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
    import { Line, Doughnut } from 'vue-chartjs';
    import Swal from 'sweetalert2'; 
    import {getStudentDashboard, projectEnroll} from '@/services/appService'
    import {
        Chart as ChartJS, Title, Tooltip, Legend, LineElement, 
        ArcElement, CategoryScale, LinearScale, Filler, PointElement,
    } from 'chart.js';

    // Register required Chart.js components
    ChartJS.register( 
        Title, Tooltip, Legend, LineElement, ArcElement, 
        CategoryScale, LinearScale, Filler, PointElement
    );
 
    export default { 
        // name: 'DonutChart',
        components: {
            Doughnut, Line
        },
        data() {
            return { 
                user_id : null,
                role: null,
                blocked: true, 
                dashboardData: null,
                loading: true,
                projectID: null,
                selectedOption: "dashboard",                 
                doughnutChartData: {
                    labels: ['Python', 'Js', 'HTML', 'Others'],  
                    datasets: [
                    {
                        label: 'Language Used',
                        data: [300, 50, 100, 75],   
                        backgroundColor: ['#007BFF', 'rgba(0, 123, 255, 0.8)', 'rgba(0, 123, 255, 0.65)', 'rgba(0, 123, 255, 0.25)'],
                        borderColor: '#ffffff',  
                        borderWidth: 2,
                    },
                    ],
                },
                doughnutChartOptions: {
                    responsive: true, 
                    plugins: {
                        legend: {
                            display: false,
                        },
                    },
                    cutout: '60%', 
                },
                lineChartData: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                    datasets: [
                        {
                            label: 'Commits',
                            data: [10, 20, 30, 25, 15, 35],
                            borderColor: '#007BFF',
                            backgroundColor: 'rgba(76, 175, 80, 0)',
                            fill: true,
                            tension: 0.4,
                        },
                        {
                            label: 'Reports Uploaded',
                            data: [5, 10, 15, 20, 25, 30],
                            borderColor: '#343A40',
                            backgroundColor: 'rgba(33, 150, 243, 0)',
                            fill: true,
                            tension: 0.4,
                        },
                    ],
                },
                lineChartOptions: {
                    responsive: true, 
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Months',
                            },
                            grid: {
                                display: false
                            }
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
        }, 
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
                    const response = await getStudentDashboard(this.user_id);
                    this.dashboardData = response;  
                    this.projectID = response.status.project_id; 
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            async enrollInProject(projectId) {
                try {
                    const response = await projectEnroll({
                        user_id: this.user_id, 
                        role: this.role, 
                        project_id: projectId
                    }); 
                    this.dashboardData.status.registered = true;
                    this.projectID = projectId;
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

                if (this.role === 'support' || this.role === 'admin') { 
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