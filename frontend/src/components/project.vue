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
                                <router-link :to="isLoggedIn ? `/project/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
                                    My Project
                                </router-link>
                            </li>
                            <li class="h-100 nav-link"> 
                                <router-link :to="isLoggedIn ? `/student-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
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

            <div class="project-body">
                <div class="loading" v-if="loading">
                    loading
                </div>
                <div class="container py-4" v-else>
                    <div class="row">
                        <div class="col-lg-8">
                            <div class="card p-4">
                                <h4 class="lh-2 px-4 pt-4 pb-2">{{ projectDetails.name }}</h4>
                                <p class="lh-2 text-secondary px-4">{{ projectDetails.description.length > 200 ? projectDetails.description.slice(0, 200) + '...' : projectDetails.description }}</p>
                                <!-- <div class="row" v-for="milestone in projectDetails.milestones" :key="milestone.id"> 
                                    <div class="col-auto text-center flex-column d-none d-sm-flex">
                                        <div class="row h-50">
                                            <div class="col">&nbsp;</div>
                                            <div class="col">&nbsp;</div>
                                        </div>
                                        <h5 class="m-2">
                                            <button class="btn btn-outline-primary disabled">
                                                <span class="badge rounded-pill bg-light border">&nbsp;</span>
                                            </button>
                                        </h5>
                                        <div class="row h-50">
                                            <div class="col border-end order">&nbsp;</div>
                                            <div class="col">&nbsp;</div>
                                        </div>
                                    </div> 
                                    <div class="col py-2">
                                        <div class="card p-4">
                                            <div class="card-body">
                                                <div class="row m-0">
                                                    <div class="col-8 p-0">
                                                        <h4 class="card-title text-muted">{{ milestone.name }}</h4>
                                                    </div>
                                                    <div class="col-4 p-0">
                                                        <span class="lh-1 text-secondary d-flex justify-content-end align-items-start">
                                                            <p class="rounded-4 border px-3 py-1 fs-6">{{ milestone.deadline }}</p>
                                                        </span>
                                                    </div>
                                                </div> 
                                                <p class="card-text text-secondary">{{ milestone.description }}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>  -->
                                <div class="milestone-container" v-for="milestone in projectDetails.milestones" :key="milestone.id">
                                    <div class="row">
                                        <div class="col-auto text-center flex-column d-none d-sm-flex">
                                            <div class="row h-50">
                                                <div class="col border-end">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                            <h5 class="m-2">
                                                <button class="btn btn-outline-primary"><span class="badge rounded-pill bg-success">&nbsp;</span></button>
                                            </h5>
                                            <div class="row h-50">
                                                <div class="col border-end">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                        </div>
                                        <div class="col py-2">
                                            <div class="card p-4 border-primary shadow">
                                                <div class="card-body">
                                                    <div class="row m-0">
                                                        <div class="col-8 p-0">
                                                            <h4 class="card-title text-muted">{{ milestone.name }}</h4>
                                                        </div>
                                                        <div class="col-4 p-0">
                                                            <span class="lh-1 text-secondary d-flex justify-content-end align-items-start">
                                                                <p class="rounded-4 border px-3 py-1 fs-6">{{ milestone.deadline }}</p>
                                                            </span>
                                                        </div>
                                                    </div> 
                                                    <p class="card-text text-secondary">{{ milestone.description }}</p>
    
                                                    <div class="checklist-section">
                                                        <div class="accordion accordion-flush" id="accordionFlushExample">
                                                            <div class="accordion-item" v-for="checklist in milestone.checklists" :key="checklist.id">
                                                                <h2 class="accordion-header">
                                                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#checklist-' + checklist.id " aria-expanded="false" aria-controls="checklist-1">
                                                                        {{checklist.name}}
                                                                    </button>
                                                                </h2>
                                                                <div :id="'checklist-' + checklist.id" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                                                    <div class="accordion-body">
                                                                        <p class="checklist-description text-secondary">{{ checklist.description }}.</p>
    
                                                                        <div class="upload-section">
                                                                            <form v-if="!checklist.code_required">
                                                                                <div class="mb-3"> 
                                                                                    <input type="file" id="fileInput" accept="application/pdf" class="form-control h-100" row="2">
                                                                                </div> 
                                                                                <div class="form-check my-2">
                                                                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" :style="{backgroundColor: 'transparent'}">
                                                                                    <label class="form-check-label text-secondary" for="flexCheckDefault">
                                                                                        Document will be analyzed by AI
                                                                                    </label>
                                                                                </div> 
                                                                                <div class="col-4 d-flex justify-content-start p-0">
                                                                                    <button type="submit" class="btn btn-primary mx-0">Upload</button>
                                                                                </div>  
                                                                            </form>
                                                                            <form v-else @submit.prevent="analyzeCode">
                                                                                <div class="mb-3">
                                                                                    <label for="dropdown1" class="form-label">Select Repo</label>
                                                                                    <select class="form-select" id="dropdown1" v-model="selectedRepo" @change="fecthAllBranch">
                                                                                        <option value="select repo" disabled>Select an option</option>
                                                                                        <option v-for="(option, index) in repos" :key="option" :value="option">
                                                                                        {{ option }}
                                                                                        </option>
                                                                                    </select>
                                                                                </div>
                                                                                <div class="mb-3" v-if="showBranchDropdown">
                                                                                    <label for="dropdown2" class="form-label">Choose Branch</label>
                                                                                    <select class="form-select" id="dropdown2" v-model="selectedBranch">
                                                                                        <option value="select branch" disabled>Select an option</option>
                                                                                        <option v-for="(option, index) in allBranches" :key="option" :value="option">
                                                                                        {{ option }}
                                                                                        </option>
                                                                                    </select>
                                                                                </div>
                                                                                <button type="submit" class="btn btn-outline-primary mx-0">
                                                                                    <span v-if="analyzingCode" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                                                                        Submit code
                                                                                </button> 
                                                                            </form>
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
                                <!-- <div class="row">
                                    <div class="col-auto text-center flex-column d-none d-sm-flex">
                                        <div class="row h-50">
                                            <div class="col border-end">&nbsp;</div>
                                            <div class="col">&nbsp;</div>
                                        </div>
                                        <h5 class="m-2">
                                            <span class="badge rounded-pill bg-light border">&nbsp;</span>
                                        </h5>
                                        <div class="row h-50">
                                            <div class="col">&nbsp;</div>
                                            <div class="col">&nbsp;</div>
                                        </div>
                                    </div>
                                    <div class="col py-2">
                                        <div class="card">
                                            <div class="card-body">
                                                <div class="float-end text-muted">Thu, Jan 12th 2021 11:30 AM</div>
                                                <h4 class="card-title">Day 4 Wrap-up</h4>
                                                <p>Join us for lunch in Bootsy's cafe across from the Campus Center.</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>  -->
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="card p-4 mb-3" :style="{height: '50vh'}">
                                <h4 class="lh-2">Uploaded Documents</h4>
                                <div class="file-container overflow-auto mt-4">
                                    <div class="row mx-0 my-3 p-2 rounded-2 border" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                        <div class="col-2 d-flex justify-content-center align-items-center">
                                            <img src="@/assets/pdf_icon.png" alt="" width="30">
                                        </div>
                                        <div class="col-10 d-flex justify-content-start align-items-center">
                                            semester_1.pdf
                                        </div>
                                    </div>
                                    <div class="row mx-0 my-3 p-2 rounded-2 border" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                        <div class="col-2 d-flex justify-content-center align-items-center">
                                            <img src="@/assets/pdf_icon.png" alt="" width="30">
                                        </div>
                                        <div class="col-10 d-flex justify-content-start align-items-center">
                                            semester_1.pdf
                                        </div>
                                    </div>
                                    <div class="row mx-0 my-3 p-2 rounded-2 border" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                        <div class="col-2 d-flex justify-content-center align-items-center">
                                            <img src="@/assets/pdf_icon.png" alt="" width="30">
                                        </div>
                                        <div class="col-10 d-flex justify-content-start align-items-center">
                                            semester_1.pdf
                                        </div>
                                    </div>
                                    <div class="row mx-0 my-3 p-2 rounded-2 border" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                        <div class="col-2 d-flex justify-content-center align-items-center">
                                            <img src="@/assets/pdf_icon.png" alt="" width="30">
                                        </div>
                                        <div class="col-10 d-flex justify-content-start align-items-center">
                                            semester_1.pdf
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card p-4 mb-3">
                                <h4 class="lh-2">Tips</h4>
                                <div class="tip-section mt-3">
                                    <div class="row m-0 border-bottom">
                                        <div class="col-1">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightbulb" viewBox="0 0 16 16">
                                                <path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a2 2 0 0 0-.453-.618A5.98 5.98 0 0 1 2 6m6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1"/>
                                            </svg>
                                        </div>
                                        <div class="col-11 d-flex align-items-center justify-content-start">
                                            <p class="text-secondary lh-2">Use Descriptive commit messages</p>
                                        </div>
                                    </div>
                                    <div class="row mx-0 mt-3 border-bottom">
                                        <div class="col-1">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightbulb" viewBox="0 0 16 16">
                                                <path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a2 2 0 0 0-.453-.618A5.98 5.98 0 0 1 2 6m6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1"/>
                                            </svg>
                                        </div>
                                        <div class="col-11 d-flex align-items-center justify-content-start">
                                            <p class="text-secondary lh-2">Upload docs in pdf files</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card p-4" :style="{height: '50vh'}">
                                <h4 class="lh-2">Feedback</h4>
                                <div class="accordion accordion-flush" id="accordionFlushExample">
                                    <div class="accordion-item">
                                        <h2 class="accordion-header">
                                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                                            Accordion Item #1
                                        </button>
                                        </h2>
                                        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                        <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
                                        </div>
                                    </div>
                                    <div class="accordion-item">
                                        <h2 class="accordion-header">
                                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                                            Accordion Item #2
                                        </button>
                                        </h2>
                                        <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                        <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the second item's accordion body. Let's imagine this being filled with some actual content.</div>
                                        </div>
                                    </div>
                                    <div class="accordion-item">
                                        <h2 class="accordion-header">
                                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                                            Accordion Item #3
                                        </button>
                                        </h2>
                                        <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                        <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
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
    import {getProjectDetails, getAllRepos, getAllBranches, analyzeCode} from '@/services/appService'; 

    export default {
        props: {
            project_id: {
                type: String,
                required: true,
            },
        },
        data() {
            return {      
                user_id : null,
                role: null,
                blocked: true,    
                selectedOption: "dashboard",   
                projectDetails: null,    
                loading: true,  
                repos: null,
                selectedRepo: null,
                showBranchDropdown: false,
                selectedBranch: null,
                allBranches: null,
                analyzingCode: false, 
            }
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
            async fetchProjectDetails() {
                try {
                    const response = await getProjectDetails(this.project_id);
                    this.projectDetails = response;  
                    // console.log(response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            },
            async fetchAllRepos() {
                try {
                    const response = await getAllRepos(this.user_id);
                    this.repos = response;  
                    console.log('all repos --> ',response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            }, 
            async fecthAllBranch() {
                if (this.selectedRepo) {
                    try { 
                        const response = await getAllBranches(this.user_id, this.selectedRepo);
                        this.allBranches = response;
                        this.showBranchDropdown = true;
                        console.log(response, 'all branches')
                    } catch (error) {
                        console.error('Error fetching Dropdown 2 options:', error);
                    }
                }
            }, 
            async analyzeCode() { 
                this.analyzingCode = true; 
                try { 
                    const response = await analyzeCode({
                        user_id: this.user_id,
                        repo_name: this.selectedRepo,
                        branch_name: this.selectedBranch
                    }); 
                    console.log('analysis result --> ', response)
                } catch (error) {
                    console.error('Error fetching Dropdown 2 options:', error);
                } finally{
                    this.analyzingCode = false 
                }
            }, 
            
        },
        mounted() { 
            const storedUserId = localStorage.getItem('user_id');
            const storedRole = localStorage.getItem('role');
        
            if (storedUserId && storedRole) {
                this.user_id = storedUserId;
                this.role = storedRole;

                if (this.role === 'admin' || this.role === 'support') {  
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
            this.fetchAllRepos();
        },
    };
</script>