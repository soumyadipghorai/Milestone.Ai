<template> 
    <div class="support-page"  :style="{ backgroundColor: 'var(--primary-background-color)' }"> 
        <div class="loading vh-100 d-flex justify-content-center align-items-center" v-if="loading">
            <!-- <dotlottie-player src="https://lottie.host/60c22126-f9b3-4a76-881a-177db0874030/dvfbPo4NAa.lottie" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player> -->
            loading...
        </div>
        <div class="done" v-else>
            <div class="row">
                <div class="col-lg-6">
                    <div class="mx-4 px-4">
                        <nav class="navbar navbar-expand-md navbar-container py-2 px-0 mb-4">
                            <a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a>
                            <button class="navbar-toggler toggle-button-style" type="button" data-toggle="collapse" data-target="#toggleCollapse" aria-expanded="false" aria-controls="toggleCollapse"> 
                                <span class="navbar-toggler-icon"></span>
                            </button>
                            <div class="container-xxl px-0">
                                <div class="collapse navbar-collapse text-center justify-content-end" id="toggleCollapse">
                                    <ul class="navbar-nav d-flex align-items-center">
                                        <li class="h-100 nav-link"> 
                                            <router-link :to="isLoggedIn ? `/support-dashboard/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
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
                        <div class="support-body my-4" :class="{ blurred: blocked }">
                            <div class="card p-4">
                                <div class="row">
                                    <div class="col-md-6">
                                        <h4 class="lh-2 mb-2 fs-4">Bug Finder</h4>
                                        <div class="info">
                                            <div class="text-section" :style="{borderBottom : '1px dotted var(--dark-border-light)'}">
                                                <h5 class="lh-2 mt-4 mb-2 fs-5">Total Bugs</h5>
                                                <p class="text-secondary fs-6">{{ dashboardData.metric.error}} total Errors</p>
                                            </div>
                                            <div class="text-section" :style="{borderBottom : '1px dotted var(--dark-border-light)'}">
                                                <h5 class="lh-2 mt-4 mb-2 fs-5">Total Warnings</h5>
                                                <p class="text-secondary fs-6">{{ dashboardData.metric.warning }} total Warnings</p>
                                            </div>
                                        </div>
    
                                    </div>
                                    <div class="col-md-6 h-100">
                                        <Doughnut :data="doughnutChartData" :options="doughnutChartOptions" class="h-100" />
                                    </div>
                                </div>
                            </div> 
                            <!-- <div class="row mt-4">
                                <div class="col-lg-6">
                                    <div class="card p-4" :style="{height: '50vh', backgroundColor: 'var(--primary-dark-color)'}">
                                        <h4 class="lh-2 mb-4 text-light">AI Suggestions</h4>
                                        <div class="suggestions-body overflow-auto">
                                            <p class="bg-warning text-light p-2 rounded-2 my-2 w-100">Pandas warning</p>
                                            <p class="bg-danger text-light p-2 rounded-2 my-2">Change API key...</p>
                                            <p class="bg-warning text-light p-2 rounded-2 my-2">Numpy warning warning</p> 
                                            <p class="bg-warning text-light p-2 rounded-2 my-2">Numpy warning warning</p> 
                                            <p class="bg-warning text-light p-2 rounded-2 my-2">Numpy warning warning</p> 
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="card p-4" :style="{height: '50vh'}">
                                    <h4 class="lh-2 mb-4">Configurations</h4>
                                    <div class="credentials-body overflow-auto"> 
                                        <form action="">
                                            <div class="mb-3">
                                                <label for="exampleFormControlInput1" class="form-label">Groq API key</label>
                                                <input type="passwords" class="form-control" placeholder="API key..." 
                                                :style="{ backgroundColor: 'var(--primary-blue-form-input-color)' }">
                                            </div>
                                            <div class="mb-3">
                                                <label for="exampleFormControlInput1" class="form-label">Groq Model name</label>
                                                <input type="passwords" class="form-control" placeholder="Model name..." 
                                                :style="{ backgroundColor: 'var(--primary-blue-form-input-color)' }">
                                            </div>
                                            <div class="mb-3">
                                                <label for="exampleFormControlInput1" class="form-label">GitHub API key</label>
                                                <input type="passwords" class="form-control" placeholder="API key..." 
                                                :style="{ backgroundColor: 'var(--primary-blue-form-input-color)' }">
                                            </div>
                                        </form>
                                    </div>
                                    </div>
                                </div>
                            </div> -->
    
                        </div>
                    </div>
                </div>
                <div class="col-lg-6" :style="{ backgroundColor: 'var(--primary-dark-color)'}" :class="{ blurred: blocked }">
                    <div class="row g-2 mx-4 my-0 py-2">
                        <div class="col-3">
                            <button class="btn btn-danger text-light">Current Logs</button>
                        </div> 
                        <div class="col-3">
                            <button class="btn btn-outline-success text-success">Current Info</button>
                        </div> 
                    </div> 
                    <div class="card p-4" :style="{backgroundColor : 'var(--primary-dark-color)', height: '100vh', border: 'none'}">
                        <div class="logs-holder overflow-auto"> 
                            <div class="log-message" v-for="(logMessage, logMessageIndex) in dashboardData.info" :key="'info-'+logMessageIndex">
                                <p class="lh-2">
                                    <span class="text-secondary">{{ logMessage.time_stamp }} - </span>
                                    <span class="text-danger">{{ logMessage.source }} - </span>
                                    <span class="text-primary">{{ logMessage.log_type }} - </span>
                                    <span class="text-light">{{ logMessage.log_message }}</span>
                                </p>
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
    import {getSupportDashboard} from '@/services/appService';

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
                dashboardData: null,
                user_id : null,
                role: null,
                blocked: true,   
                loading: true,
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
            async fetchDashboard() {
                try {
                    const response = await getSupportDashboard(this.user_id);
                    this.dashboardData = response;  
                    this.doughnutChartData.labels = response.metric.labels;  
                    this.doughnutChartData.datasets = response.metric.datasets;  
                    console.log(response)
                    console.log(this.lineChartData)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
        },
        mounted() { 
            const storedUserId = localStorage.getItem('user_id');
            const storedRole = localStorage.getItem('role');
        
            if (storedUserId && storedRole) {
                this.user_id = storedUserId;
                this.role = storedRole;

                if (this.role !== 'support') {  
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