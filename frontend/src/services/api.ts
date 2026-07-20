import axios from 'axios';
export const api=axios.create({baseURL:import.meta.env.VITE_API_URL ?? '/api',withCredentials:true});
api.interceptors.response.use(r=>r, e=>Promise.reject(new Error(e.response?.data?.detail || 'A network or server error occurred.')));
