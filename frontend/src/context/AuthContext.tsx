import {createContext,useContext,useEffect,useState} from 'react'; import {api} from '../services/api';
export type User={id:number;first_name:string;last_name:string;email:string;student_id?:string;role:'student'|'admin'}; const C=createContext<any>(null);
export function AuthProvider({children}:{children:React.ReactNode}){const [user,setUser]=useState<User|null>(null); const [loading,setLoading]=useState(true); useEffect(()=>{api.get('/auth/me/').then(r=>setUser(r.data)).catch(()=>null).finally(()=>setLoading(false))},[]); return <C.Provider value={{user,setUser,loading}}>{children}</C.Provider>}
export const useAuth=()=>useContext(C);
