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
                                <router-link :to="isLoggedIn ? `/project/${currentProjectID}/${user_id}` : '/login'" class="text-decoration-none selected-role text-primary">
                                    My Project
                                </router-link>
                            </li>
                            <li class="h-100 nav-link" v-if="role === 'student'"> 
                                <router-link :to="isLoggedIn ? `/student-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    Dashboard
                                </router-link>
                            </li> 
                            <li v-if="role == 'student'">
                                <div class="dropdown h-100 nav-link d-flex align-items-center py-0">
                                    <a class=" dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        <img src="@/assets/notification.png" alt="" width="30">
                                        <span class="position-absolute top-10 start-90 translate-middle p-2 bg-danger border border-light rounded-circle">
                                            <span class="visually-hidden">New alerts</span>
                                        </span>
                                    </a>

                                    <ul class="dropdown-menu">
                                    <li v-if="!notifications.length">
                                        <span class="dropdown-item">No new notifications</span>
                                    </li>
                                    <li v-for="(notification, index) in notifications" :key="index">
                                        <a class="dropdown-item" href="#" @click="markAsRead(index)">
                                        {{ notification.message }}
                                        </a>
                                    </li>
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
                                <h4 class="lh-2 px-4 pt-4 pb-2">{{ projectDashboardDetails.project_details.name }}</h4>
                                <p class="lh-2 text-secondary px-4">{{ projectDashboardDetails.project_details.description.length > 200 ? projectDashboardDetails.project_details.description.slice(0, 200) + '...' : projectDashboardDetails.project_details.description }}</p>
                                <div class="milestone-container" v-for="milestone in projectDashboardDetails.project_details.milestones" :key="milestone.id">
                                    
                                    <div class="row" v-if="milestone.index === 'past'">
                                        <div class="col-auto text-center flex-column d-none d-sm-flex">
                                            <div class="row h-50">
                                                <div class="col">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                            <h5 class="m-2">
                                                <button class="btn btn-outline-secondary disabled">
                                                    <span class="badge rounded-pill bg-light border">&nbsp;</span>
                                                </button>
                                            </h5>
                                            <div class="row h-50">
                                                <div class="col border-end order">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                        </div>
                                        <div class="col py-2">
                                            <div class="card p-4 border">
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
                                    </div>
                                    <div class="row" v-else>
                                        <div class="col-auto text-center flex-column d-none d-sm-flex">
                                            <div class="row h-50">
                                                <div class="col border-end">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                            <h5 class="m-2">
                                                <button 
                                                    class="btn" 
                                                    :class="milestone.index === 'current' ? 'btn-outline-primary' : 'btn-outline-secondary'"
                                                >
                                                    <span 
                                                        class="badge rounded-pill" 
                                                        :class="milestone.index === 'current' ? 'bg-primary' : 'bg-light'"
                                                    >&nbsp; </span>
                                                </button>
                                            </h5>
                                            <div class="row h-50">
                                                <div class="col border-end">&nbsp;</div>
                                                <div class="col">&nbsp;</div>
                                            </div>
                                        </div>
                                        <div class="col py-2">
                                            <div 
                                                class="card p-4"
                                                :class="milestone.index === 'current' ? 'border-primary shadow' : ''"
                                            >
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
    
                                                                        <div class="upload-section" v-if="role === 'student'">
                                                                            <form v-if="!checklist.code_required" @submit.prevent="analyzeStudentReport">
                                                                                <div class="mb-3"> 
                                                                                    <input type="hidden" name="checklist_id" :value="checklist.id" id="uploadingChecklistId"/>
                                                                                    <input type="file" id="fileInput" accept="application/pdf" class="form-control h-100" row="2" required>
                                                                                </div> 
                                                                                <div class="form-check my-2">
                                                                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" :style="{backgroundColor: 'transparent'}" required>
                                                                                    <label class="form-check-label text-secondary" for="flexCheckDefault">
                                                                                        Document will be analyzed by AI
                                                                                    </label>
                                                                                </div> 
                                                                                <div class="col-4 d-flex justify-content-start p-0">
                                                                                    <button type="submit" class="btn btn-outline-primary mx-0">
                                                                                        <span v-if="fileUploading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                                                                        Upload
                                                                                    </button>
                                                                                </div>  
                                                                            </form>
                                                                            <form v-else @submit.prevent="analyzeCode">
                                                                                <div class="mb-3">
                                                                                    <input type="hidden" name="checklist_id" :value="checklist.id" id="uploadingCodeChecklistId"/>
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
                                                                                <div class="form-check my-2">
                                                                                    <input class="form-check-input" type="checkbox" value="" id="flexcodeCheckDefault" :style="{backgroundColor: 'transparent', color: 'black'}" required>
                                                                                    <label class="form-check-label text-secondary" for="flexcodeCheckDefault">
                                                                                        Codes will be analyzed by AI
                                                                                    </label>
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
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="card p-4 mb-3" :style="{height: '60vh'}" v-if="role === 'student'">
                                <h4 class="lh-2">Uploaded Documents</h4>
                                <div class="file-container overflow-auto mt-4">
                                    <div class="accordion accordion-flush" id="accordionFlushExample">
                                        <div class="accordion-item" v-for="(uploadedPdf, uploadedPdfIndex) in projectDashboardDetails.uploaded_docs" :key="uploadedPdf.id">
                                            <h2 class="accordion-header">
                                                <button class="accordion-button collapsed rounded-2 border my-2" type="button" data-bs-toggle="collapse" :data-bs-target="'#stduent-docs-' + uploadedPdf.id " aria-expanded="false" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                    {{uploadedPdf.name}}
                                                </button>
                                            </h2>
                                            <div :id="'stduent-docs-' + uploadedPdf.id" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body">
                                                    <ul class="list-group list-group-flush">
                                                       <li v-for="(reconmmendation, reconmmendationIndex) in uploadedPdf.ai_response.recommendations" class="list-group-item">
                                                            {{ reconmmendation }}
                                                       </li> 
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="card p-4 mb-3" :style="{height: '50vh'}" v-if="role === 'instructor'">
                                <h4 class="lh-2">Document Analysis</h4>
                                <div class="file-container overflow-auto mt-4">
                                    <div class="accordion accordion-flush" id="accordionFlushExample">
                                        <div class="accordion-item" v-for="(uploadedPdf, uploadedPdfIndex) in projectDashboardDetails.uploaded_docs" :key="uploadedPdf.id">
                                            <h2 class="accordion-header">
                                                <button class="accordion-button collapsed rounded-2 border my-2" type="button" data-bs-toggle="collapse" :data-bs-target="'#instructor-docs-' + uploadedPdf.id " aria-expanded="false" :style="{backgroundColor: 'var(--primary-background-color)'}">
                                                    {{uploadedPdf.name}}
                                                </button>
                                            </h2>
                                            <div :id="'instructor-docs-' + uploadedPdf.id" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body">
                                                    <h6 class="lh-2">Summary : </h6>
                                                    <p class="text-secondary lh-2">{{ uploadedPdf.ai_response.summary }}</p>

                                                    <h6 class="lh-2">Additional Notes : </h6>
                                                    <p class="text-secondary lh-2">{{ uploadedPdf.ai_response.additional_notes }}</p>

                                                    <h6 class="lh-2">Conclusions : </h6>
                                                    <p class="text-secondary lh-2" v-for="(conclusion, conclusionIndex) in uploadedPdf.ai_response.conclusions" :key="conclusionIndex">{{ conclusion }}</p>
                                                    
                                                    <h6 class="lh-2">Key Insights : </h6>
                                                    <p class="text-secondary lh-2" v-for="(insight, insightIndex) in uploadedPdf.ai_response.key_insights" :key="insightIndex">{{ insight }}</p> 
                                                    
                                                    <div class="tags d-flex">
                                                        <div class="rounded-2 p-2 border m-2" :style="{backgroundColor: 'var(--primary-background-color)'}" v-for="(tag, tagIndex) in uploadedPdf.ai_response.tags" :key="tagIndex">{{ tag }}</div>
                                                    </div>

                                                    <button class="btn btn-outline-primary">
                                                        <a class="text-decoration-none" :href="uploadedPdf.file_path" :download="uploadedPdf.name">
                                                            Download 
                                                        </a>
                                                    </button>
                                                </div>
                                            </div>
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
                            <div class="card p-4" :style="{height: '70vh'}">
                                <h4 class="lh-2">Feedback</h4>
                                <div class="file-container overflow-auto mt-4">
                                    <div class="accordion accordion-flush" id="accordionFlushExample">
                                        <div class="accordion-item" v-for="(codeFeedback, codeFeedbackIndex) in projectDashboardDetails.code_feedback" :key="codeFeedback.id">
                                            <h2 class="accordion-header">
                                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#code-feedback-student-' + codeFeedback.id " aria-expanded="false">
                                                    {{codeFeedback.name}}
                                                </button>
                                            </h2>
                                            <div :id="'code-feedback-student-' + codeFeedback.id" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                                                <div class="accordion-body">
                                                    <div class="student-feedback mb-3">
                                                        <h5 class="lh-2 my-3">Code Quality Check:</h5>
                                                        <div class="testcase m-2 border-bottom" v-for="(result, testCase, testCaseIndex) in codeFeedback.overall_summary" :key="testCaseIndex">
                                                            <h6 class="text-dark">{{ testCase }} : </h6>
                                                            <p class="p-0" :class="{ 'text-success': result.result === 'passed', 'text-danger': result.result !== 'passed' }">{{ result.result }}</p>
                                                            <p class="text-secondary p-0">{{result.feedback.description}}</p>
                                                        </div>
                                                    </div>
                                                    <div class="instructor-feedback mb-3" v-if="role !== 'student'">
                                                        <h5 class="lh-2 my-3">Overall Feedback</h5>
                                                        <div class="testcase m-2 border-bottom" v-for="(keyPoint, keyPointIndex) in codeFeedback.instructor_feedback.key_points" :key="keyPointIndex">
                                                            <h6 class="text-dark">{{ keyPoint.title }} : </h6> 
                                                            <p class="text-secondary p-0">{{keyPoint.description}}</p>
                                                        </div>
                                                        <h5 class="lh-2 my-3">Commit Summary</h5>
                                                        <div class="testcase m-2 border-bottom" v-for="(keyPoint, keyPointIndex) in codeFeedback.commit_summary.key_points" :key="keyPointIndex">
                                                            <h6 class="text-dark">{{ keyPoint.title }} : </h6> 
                                                            <p class="text-secondary p-0">{{keyPoint.description}}</p>
                                                        </div>

                                                        <a :href="codeFeedback.project_url" class="btn btn-outline-primary" target="_blank">Check Repo</a>
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
    import {getStudentProjectDetails, getAllRepos, getAllBranches, analyzeCode, studentReportUpload} from '@/services/appService'; 

    export default {
        props: {
            project_id: {
                type: String,
                required: true,
            },
            stduent_id: {
                type: String,
                required: true,
            },
        },
        data() {
            return {      
                notifications:[],
                user_id : null,
                role: null,
                blocked: true,    
                selectedOption: "dashboard",   
                projectDashboardDetails: null,    
                loading: true,  
                repos: null,
                selectedRepo: null,
                showBranchDropdown: false,
                selectedBranch: null,
                allBranches: null,
                analyzingCode: false, 
                currentProjectID: null, 
                fileUploading: false,
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
                    console.log(this.stduent_id, this.project_id);
                    const response = await getStudentProjectDetails(this.stduent_id);
                    this.projectDashboardDetails = response;  
                    this.currentProjectID = response.project_details.id;
                    this.notifications=response.notifications;
                    console.log(response)
                } catch (error) {
                    this.error = "Failed to fetch dashboard data. Please try again later.";
                    console.error("API error:", error);
                } finally {
                    this.loading = false;  
                }
            },
            async fetchAllRepos() {
                try {
                    const response = await getAllRepos(this.stduent_id);
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
                        const response = await getAllBranches(this.stduent_id, this.selectedRepo);
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
                        branch_name: this.selectedBranch, 
                        checklist_id: document.getElementById("uploadingCodeChecklistId").value 
                    }); 
                    console.log('analysis result --> ', response)
                } catch (error) {
                    console.error('Error fetching Dropdown 2 options:', error);
                } finally{
                    this.analyzingCode = false; 
                    this.fetchProjectDetails();
                }
            }, 
            async analyzeStudentReport() {
                this.fileUploading = true;
                const fileInput = document.getElementById("fileInput");
                const checklistID = document.getElementById("uploadingChecklistId").value; 
                const file = fileInput.files[0]; 
                if (!file) {
                    alert("Please select a file!");
                    return;
                }

                const formData = new FormData();
                formData.append("file", file);
                formData.append("checklist_id", checklistID);
                formData.append("user_id", this.user_id);

                // for (const [key, value] of formData.entries()) {
                //     console.log(`${key}:`, value);
                // }
                
                try { 
                    const response = await studentReportUpload(formData); 
                    // this.$router.push(`/project/${this.currentProjectID}/${this.user_id}`);  
                } catch (error) {
                    console.error('Error fetching Dropdown 2 options:', error);
                } finally {
                    this.fileUploading = false;
                    this.fetchProjectDetails();
                    fileInput.value = null;
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