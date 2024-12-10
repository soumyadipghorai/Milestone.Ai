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
                                <router-link :to="isLoggedIn ? `/instructor-dashboard/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
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
                <div class="dashboard-body my-4" :class="{ blurred: blocked }" v-if="dashboardData.status.registered">
                    <div class="row mx-0 my-4">
                        <div class="col-lg-6">
                            <div class="card p-4" :style="{backgroundColor : 'var(--primary-dark-color)', height: '50vh'}">
                                <h4 class="lh-2 my-2 text-light">Leader Board</h4>
                                <div class="leader-board-item overflow-auto">
                                    <div 
                                        class="row m-0" 
                                        :style="{borderBottom : '1px dotted var(--primary-background-color)'}" 
                                        v-for="(studentDetails, studentDetailsIndex) in dashboardData.status.leader_board"
                                        :key="'leaderboard-details-'+ studentDetailsIndex"
                                    >
                                        <div class="col-3 h-100 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp4.png" alt="" width="40">
                                        </div>
                                        <div class="col-6 d-flex justify-content-start text-light align-items-center">
                                            {{studentDetails.name}} 
                                        </div>
                                        <div class="col-3 d-flex justify-content-start text-light align-items-center">
                                            {{ studentDetails.max_commit }} commits 
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="card p-4" :style="{height: '50vh'}">
                                <h4 class="lh-2 my-2 p-2">Student details</h4>
                                <div class="student-info overflow-auto">
                                    <div
                                        v-for="(row, rowIndex) in formattedEnrolledStudentList"
                                        :key="'row-' + rowIndex"
                                        class="row my-2"
                                    >
                                        <div
                                            v-for="(item, colIndex) in row"
                                            :key="'col-' + colIndex"
                                            class="col-lg-6"
                                        >
                                        <div
                                            class="card p-0"
                                            :style="{ backgroundColor: 'var(--primary-background-color)' }"
                                            style="cursor: pointer"
                                            @click="navigateToProject(item.project_id, item.id)"
                                        >
                                        <div class="row m-0">
                                            <div class="col-2 my-2 d-flex justify-content-start align-items-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30" />
                                            </div>
                                            <div class="col-7 my-2 d-flex justify-content-start align-items-center">
                                            {{ item.name }}
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
                                    <div 
                                        class="row my-3" 
                                        v-for="(studentDetails, studentDetailsIndex) in dashboardData.status.student_progress"
                                        :key = "'student-progress-'+studentDetailsIndex"
                                    >
                                        <div class="col-1 d-flex justify-content-center">
                                            <img src="@/assets/pfp2.png" alt="" width="30">
                                        </div>
                                        <div class="col-11">
                                            <div class="progress my-2" role="progressbar" aria-label="Default striped example" :aria-valuenow="studentDetails.percentage" aria-valuemin="0" aria-valuemax="100">
                                                <div class="progress-bar progress-bar-striped progress-bar-animated" :style="{width: `${studentDetails.percentage}%`}"></div>
                                            </div> 
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-5">
                            <div class="card p-4 h-100 text-light bg-primary-subtle text-dark">
                                <h4 class="lh-2 my-2">Status Updates</h4>
                                <div id="carouselExample" class="carousel slide">
                                    <div class="carousel-inner">
                                        <div 
                                            class="carousel-item mx-2 bg-dark card p-4 text-light" 
                                            v-for="(feedback, feedbackIndex) in dashboardData.status.all_feedback"
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
                loading: true,  
                currentSlideIndex: 0,
            };
        },
        computed: { 
            isLoggedIn() { 
                this.user_id = localStorage.getItem('user_id');
                return !!localStorage.getItem('user_id');
            },
            formattedEnrolledStudentList() {
                const { enrolled_student_list } = this.dashboardData.status;
                const rows = [];
                for (let i = 0; i < enrolled_student_list.length; i += 2) {
                    rows.push(enrolled_student_list.slice(i, i + 2));
                }
                return rows;
            },
            itemClass(projectId) {
                return projectId.includes("fcbc")
                ? "bg-warning rounded-circle"
                : "bg-success rounded-circle";
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
                    this.$router.push(`/instructor-dashboard/${projectId}`);
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            navigateToProject(projectId, id) {
                this.$router.push(`/project/${projectId}/${id}`);
            },
            goToPrevSlide() {
                if (this.currentSlideIndex > 0) {
                    this.currentSlideIndex--;
                } else {
                    this.currentSlideIndex = this.dashboardData.status.all_feedback.length - 1;
                }
            },  
            goToNextSlide() {
                if (this.currentSlideIndex < this.dashboardData.status.all_feedback.length - 1) {
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