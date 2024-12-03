import apiClient from "@/axios";

export async function loginAdmin(data) {
    try { 
        const response = await apiClient.post("/user-login", data);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}

export async function registerAdmin(data) {
    try { 
        console.log(data)
        const response = await apiClient.post("/register-user", data);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
}
