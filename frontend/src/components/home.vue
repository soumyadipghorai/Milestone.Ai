<template>
    <div class="landing-page"  :style="{ backgroundColor: 'var(--primary-background-color)' }">
        <div class="container">
            <nav class="navbar navbar-expand-md navbar-container py-2 px-0">
                <a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a>
                <button class="navbar-toggler toggle-button-style" type="button" data-toggle="collapse" data-target="#toggleCollapse" aria-expanded="false" aria-controls="toggleCollapse"> 
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="container-xxl px-0 d-flex ">
                    <div class="collapse navbar-collapse text-center d-flex justify-content-end align-items-center" id="toggleCollapse">
                        <ul class="navbar-nav d-flex align-items-center">
                            <li class="h-100 nav-link d-flex align-items-center"> 
                                <router-link :to="isLoggedIn ? `/student-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    Stduent
                                </router-link>
                            </li>
                            <li class="h-100 nav-link d-flex align-items-center"> 
                                <router-link :to="isLoggedIn ? `/instructor-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    Instructor
                                </router-link>
                            </li>
                            <li class="h-100 nav-link d-flex align-items-center">  
                                <router-link :to="isLoggedIn ? `/admin-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    Admin
                                </router-link>
                            </li>
                            <li class="h-100 nav-link d-flex align-items-center"> 
                                <router-link :to="isLoggedIn ? `/support-dashboard/${user_id}` : '/login'" class="text-decoration-none text-reset">
                                    Support
                                </router-link> 
                            </li>
                            <li class="h-100 nav-link d-flex align-items-center">
                                <button v-if="isLoggedIn" class="btn btn-primary btn-md" @click="logout">
                                    Log Out
                                </button>
                                <router-link v-else :to="`/login`" class="btn btn-primary">
                                    log In
                                </router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <section class="hero-section vh-75 row mx-0 my-4"> 
                <div class="col-lg-6 d-flex align-items-center p-4">
                    <div class="hero-left">
                        <h1 class="lh-2 mb-3">Empowering Student Through <span :style="{ color: 'var(--primary-blue-color)' }">AI-Driven</span> Insights</h1>
                        <p class="lh-2 mb-3">Harnessing advanced tools and frameworks to enhance student progress tracking and insights.</p>
                        <div class="d-flex justify-content-start flex-wrap btn-group-wrapper p-0">
                            <a href="#features"> 
                                <button type="button" class="btn btn-primary">Features</button>
                            </a>
                            <a href="#techstack">
                                <button type="button" class="btn btn-outline-secondary">Tech Stack</button>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 d-flex justify-content-center">
                    <img src="@/assets/landing-page.gif" alt="" class="img-fluid w-75">
                </div>
            </section>

            <section class="tech-used my-4 p-4" id="techstack">
                <div class="text-section">
                    <h2 class="lh-2 mb-3 text-center">Tech Used</h2>
                    <p class="lh-2 text-center">Harnessing advanced tools and frameworks to enhance student progress tracking and insights.</p>
                </div>
                <div class="tech-img d-flex justify-content-center m-0 p-4">
                    <div class="row w-100">
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/groq-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/python-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/fastapi-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/langchain-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/vue-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                        <div class="col-md-2 py-4 d-flex justify-content-center">
                            <img src="@/assets/meta-logo.png" alt="OpenAI" class="rounded-3" height="60"/>
                        </div>
                    </div>
                </div>
            </section>
            <section class="features my-4" id="features">
                <div class="text-section">
                    <h2 class="lh-2 mb-3 text-center">Features</h2>
                    <p class="lh-2 text-center">Empowering Instructors to Monitor Student Progress Effectively</p>
                </div>
                <div class="feature-description">
                    <div class="row m-0">
                        <div class="col-lg-4 m-0 p-4">
                            <div class="img-container d-flex justify-content-center mb-4">
                                <img src="@/assets/feature1.png" alt="OpenAI" class="img-fluid rounded-2 border" width="60" />
                            </div>
                            <div class="text-area text-center">
                                <h5 class="lh-2 py-2">Real-Time Progress Tracking</h5>
                                <p class="lh-2">Monitor student project progress instantly through integrated GitHub commit histories and updates.</p>
                            </div>
                        </div>
                        <div class="col-lg-4 m-0 p-4">
                            <div class="img-container d-flex justify-content-center mb-4">
                                <img src="@/assets/feature2.png" alt="OpenAI" class="img-fluid rounded-2 border" width="60" />
                            </div>
                            <div class="text-area text-center">
                                <h5 class="lh-2 py-2">Customizable Milestones</h5>
                                <p class="lh-2">Create tailored milestones and task lists for each project, ensuring clarity and focus for students.</p>
                            </div>
                        </div>
                        <div class="col-lg-4 m-0 p-4">
                            <div class="img-container d-flex justify-content-center mb-4">
                                <img src="@/assets/feature3.png" alt="OpenAI" class="img-fluid rounded-2 border" width="60" />
                            </div>
                            <div class="text-area text-center">
                                <h5 class="lh-2 py-2">AI-Powered Insights</h5>
                                <p class="lh-2">Leverage generative AI to analyze student submissions and provide actionable feedback and performance.</p>
                            </div>
                        </div> 
                    </div>
                </div>
            </section>

            <section class="FAQ my-4"> 
                <div class="row m-0">
                    <div class="col-lg-6">
                        <div class="text-section my-4">
                            <h2 class="lh-2 mb-3 text-center">FAQ</h2>
                        </div>
                        <div class="accordion accordion-flush">
                            <div class="accordion-item" :style="{backgroundColor : 'var(--primary-background-color)' }">
                                <h2 class="accordion-header">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
                                    What is the primary purpose of this software?
                                </button>
                                </h2>
                                <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show">
                                    <div class="accordion-body">
                                        The software is designed to help instructors effectively monitor and manage student project progress throughout the semester, ensuring that students stay on track with their assignments.
                                    </div>
                                </div>
                            </div>
                            <div class="accordion-item" :style="{backgroundColor : 'var(--primary-background-color)' }">
                                <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="false" aria-controls="panelsStayOpen-collapseTwo">
                                    How does the software integrate with GitHub?
                                </button>
                                </h2>
                                <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse">
                                    <div class="accordion-body">
                                        The software integrates with GitHub to automatically pull commit histories, allowing instructors to visualize student contributions and track progress in real-time.
                                    </div>
                                </div>
                            </div>
                            <div class="accordion-item" :style="{backgroundColor : 'var(--primary-background-color)' }">
                                <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="false" aria-controls="panelsStayOpen-collapseThree">
                                    Can I customize milestones for different projects?
                                </button>
                                </h2>
                                <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse">
                                    <div class="accordion-body">
                                        Yes, instructors can create customizable milestones and task lists tailored to the specific needs of each project, providing clear expectations for students.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 d-flex justify-content-center">
                        <img src="@/assets/FAQ.png" alt="" class="img-fluid w-75">
                    </div>
                </div>
            </section>            
        </div>
        <div class="footer p-4" :style="{backgroundColor : 'var(--primary-dark-color)'}">
            <div class="row m-0 py-4 px-3">
                <div class="col-lg-6 d-flex justify-content-lg-start justify-content-center p-4">
                    <div class="footer-branding">
                        <h4 class="lh-2 text-lg-start text-center" :style="{color : 'white'}"><a class="navbar-brand" href="/">Milestone<span :style="{ color: 'var(--primary-blue-color)' }">.Ai</span></a></h4>
                        <div class="bg-light rounded-2 p-2">
                            <a href="https://github.com/22f3002024/soft-engg-project-sep-2024-se-sep-27/tree/ghorai" class="text-decoration-none text-reset" target="_blank">
                                <div class="row m-0">
                                    <div class="col-8">
                                        GitHub
                                    </div>
                                    <div class="col-4">
                                        <img src="@/assets/github-icon.png" alt="github-icon" width="20">
                                    </div>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 d-flex justify-content-lg-end justify-content-center p-4">
                    <div class="footer-contact">
                        <h4 class="lh-2 text-lg-start text-center" :style="{color : 'white'}">Contact Us</h4>
                        <div class="bg-light rounded-2 p-2">
                            <div class="row m-0">
                                <div class="col-8">
                                    WhatsApp
                                </div>
                                <div class="col-4">
                                    <img src="@/assets/whatsapp-icon.png" alt="github-icon" width="20">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="copyright text-center text-light">
                Developed with ❤️ by Team 27
            </div>
        </div>
    </div>
</template>

<script>
export default {
    // name: 'Home',
    data() {
        return {
            user_id : null,
        }
    },
    computed: { 
        isLoggedIn() { 
            this.user_id = localStorage.getItem('user_id');
            return !!localStorage.getItem('user_id');
        },
        userId() { 
            return localStorage.getItem('user_id');
        }
    }, 
    methods: {
        logout() {
            localStorage.removeItem('user_id'); // Clear user data
            localStorage.removeItem('access_token'); // Clear user data
            this.$router.push('/login'); // Redirect to login
        },
    },
}
</script>

<style scoped>
    .btn-group-wrapper {
        gap: 10px;  
        padding: 1rem;
    }

    .accordion-button:not(.collapsed), .accordion-button{
        background-color: var(--primary-background-color);
        text-decoration: none
    }
</style>