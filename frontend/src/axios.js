// src/axios.js
import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:8000/v1", 
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
