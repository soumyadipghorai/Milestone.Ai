// src/axios.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "https://milestone-ai.onrender.com/v1", 
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
