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
                                    <!-- <li v-if="!notifications.length">
                                        <span class="dropdown-item">No new notifications</span>
                                    </li>
                                    <li v-for="(notification, index) in notifications" :key="index">
                                        <a class="dropdown-item" href="#" @click="markAsRead(index)">
                                        {{ notification.message }}
                                        </a>
                                    </li> -->
                                        <li>No New notifications</li>
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
            <div class="loading" v-if="loading">
                loading
            </div>
            <div class="done" v-else> 
                <div class="container mt-5">
                    <h4 class="lh-2 my-2">Edit Project Details</h4>
                    <p class="text-secondary lh-2">Once you finalize the details the project will be up and running...</p>
                    <div class="row m-0 pb-4">
                        <div class="col-md-6 card p-4">
                            <div class="mb-3">
                                <label for="projectName" class="form-label">Project Name</label>
                                <input type="text" class="form-control" id="projectName" v-model="projectDetails.name">
                            </div>
         
                            <div class="mb-3">
                                <label for="projectDescription" class="form-label">Project Description</label>
                                <textarea class="form-control" id="projectDescription" rows="6" v-model="projectDetails.description"></textarea>
                            </div>
         
                            <div class="mb-3">
                                <label for="projectDeadline" class="form-label">Project Deadline</label>
                                <input type="date" class="form-control" id="projectDeadline" v-model="projectDetails.deadline">
                            </div>
                            <div class="btn-container w-50">
                                <button type="button" class="btn btn-primary" @click="saveProjectDetails">Save Project Details</button>
                            </div>
                        </div>
                        <div class="col-md-6 my-4 my-lg-0 px-md-4 px-0">
                            <div class="accordion accordion-flush" id="milestonesAccordion">
                                <div 
                                    v-for="(milestone, milestoneIndex) in projectDetails.milestones" 
                                    :key="milestone.id" 
                                    class="accordion-item"
                                >
                                    <h2 class="accordion-header" :id="'heading' + milestone.id">
                                        <button 
                                            class="accordion-button collapsed" 
                                            type="button" 
                                            data-bs-toggle="collapse" 
                                            :data-bs-target="'#collapse' + milestone.id" 
                                            aria-expanded="true" 
                                            :aria-controls="'collapse' + milestone.id"
                                        > 
                                            <input 
                                                type="text" 
                                                class="form-control" 
                                                v-model="projectDetails.milestones[milestoneIndex].name" 
                                                placeholder="Enter Milestone Name"
                                            />
                                        </button>
                                    </h2>
                                    <div 
                                        :id="'collapse' + milestone.id" 
                                        class="accordion-collapse collapse" 
                                        :aria-labelledby="'heading' + milestone.id" 
                                        data-bs-parent="#milestonesAccordion"
                                    >
                                        <div class="accordion-body"> 
                                            <div class="mb-3">
                                                <label class="form-label">Milestone Description</label>
                                                <textarea 
                                                    class="form-control" 
                                                    v-model="projectDetails.milestones[milestoneIndex].description" 
                                                    rows="3"
                                                ></textarea>
                                            </div>
                                            <div class="accordion" id="checklistsAccordion">
                                                <div 
                                                    v-for="(checklist, checklistIndex) in milestone.checklists" 
                                                    :key="checklist.id" 
                                                    class="accordion-item"
                                                >
                                                    <h2 class="accordion-header" :id="'headingChecklist' + checklist.id">
                                                        <button 
                                                            class="accordion-button" 
                                                            type="button" 
                                                            data-bs-toggle="collapse" 
                                                            :data-bs-target="'#collapseChecklist' + checklist.id" 
                                                            aria-expanded="true" 
                                                            :aria-controls="'collapseChecklist' + checklist.id"
                                                        >
                                                            <input 
                                                                type="text" 
                                                                class="form-control" 
                                                                v-model="projectDetails.milestones[milestoneIndex].checklists[checklistIndex].name" 
                                                                placeholder="Enter Checklist Name"
                                                            />
                                                        </button>
                                                    </h2>
                                                    <div 
                                                        :id="'collapseChecklist' + checklist.id" 
                                                        class="accordion-collapse collapse" 
                                                        :aria-labelledby="'headingChecklist' + checklist.id" 
                                                        data-bs-parent="#checklistsAccordion"
                                                    >
                                                        <div class="accordion-body"> 
                                                            <div class="mb-3">
                                                                <label class="form-label">Checklist Description</label>
                                                                <textarea 
                                                                    class="form-control" 
                                                                    v-model="projectDetails.milestones[milestoneIndex].checklists[checklistIndex].description" 
                                                                    rows="2"
                                                                ></textarea>
                                                            </div>

                                                            <div class="mb-3 form-check">
                                                                <input 
                                                                    type="checkbox" 
                                                                    class="form-check-input" 
                                                                    v-model="projectDetails.milestones[milestoneIndex].checklists[checklistIndex].code_required"
                                                                />
                                                                <label class="form-check-label">Code Required</label>
                                                            </div>

                                                            <div class="mb-3">
                                                                <label class="form-label">Checklist Deadline in days</label>
                                                                <input 
                                                                    type="number" 
                                                                    class="form-control" 
                                                                    v-model="projectDetails.milestones[milestoneIndex].checklists[checklistIndex].deadline"
                                                                />
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
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
    import {getProjectDetails, updateProjectDetails, projectEnroll} from '@/services/appService';
    export default { 
        props: {
            project_id: {
                type: String,
                required: true,
            },
        },

        data() {
            return {  
                notifications:[]    ,          
                user_id : null,
                role: null,
                blocked: true, 
                selectedOption: "dashboard",     
                projectDetails: null,  
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
            async fetchProjectDetails() {
                try {
                    const response = await getProjectDetails(this.project_id);
                    this.projectDetails = response;  
                    this.notifications=response.notifications;
                    console.log(response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            saveProjectDetails() {
                const updatedProjectDetails = this.projectDetails;  
                console.log("Updated Project Details:", JSON.stringify(updatedProjectDetails));

                // updatedProjectDetails.milestones.forEach((milestone) => {
                //     console.log("Milestone:", milestone);

                //     milestone.checklists.forEach((checklist) => {
                //         console.log("Checklist:", checklist);
                //     });
                // });

                this.updateProjectApi(updatedProjectDetails);
            },
            async updateProjectApi(updatedDetails) {
                try { 
                    const response = await updateProjectDetails(updatedDetails); 
                    this.$router.push(`/instructor-dashboard/${this.user_id}`);  
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
            this.fetchProjectDetails();
        },
    };
</script>