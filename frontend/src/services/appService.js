import apiClient from "@/axios";

export async function projectReportUpload(file) {
    try { 
        const formData = new FormData();
        formData.append("file", file); // Append the file to FormData

        const response = await apiClient.post("/generate-milestone", formData, {
            headers: {
                "Content-Type": "multipart/form-data", // Ensure the correct content type
            },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
}

export async function studentReportUpload(formData) {
    try { 
        const response = await apiClient.post("/analyze-student-report", formData, {
            headers: {
                "Content-Type": "multipart/form-data", 
            },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
}


export async function getInstructorDashboard(user_id) {
    try { 
        const response = await apiClient.get("/get-instructor-dashboard", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getSupportDashboard(user_id) {
    try { 
        const response = await apiClient.get("/get-support-dashboard", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getAdminDashboard(user_id) {
    try { 
        const response = await apiClient.get("/get-admin-dashboard", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getStudentDashboard(user_id) {
    try { 
        const response = await apiClient.get("/get-student-dashboard", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getProjectDetails(project_id) {
    try { 
        const response = await apiClient.get("/get-project-details", {
            params: { project_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getStudentProjectDetails(user_id) {
    try { 
        const response = await apiClient.get("/get-student-project-details", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getAllRepos(user_id) {
    try { 
        const response = await apiClient.get("/get-all-repo", {
            params: { user_id },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function getAllBranches(user_id, repo_name) {
    try { 
        const response = await apiClient.get("/get-all-branches", {
            params: { user_id, repo_name },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function analyzeCode(data) {
    try { 
        const response = await apiClient.post("/analyze-code", data);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function submitStudentFeedback(data) {
    try { 
        const response = await apiClient.post("/submit-feedback", data);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function projectEnroll(data) {
    try { 
        const response = await apiClient.put("/project-enroll", data);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function updateProjectDetails(data) {
    try { 
        const response = await apiClient.put("/update-project", data, {
            headers: {
                'Content-Type': 'application/json',
            },
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}