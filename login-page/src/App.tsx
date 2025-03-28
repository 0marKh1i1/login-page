import { useNavigate } from 'react-router-dom'; 
import { useEffect, useState } from 'react'
import Cookies from 'js-cookie';
import axios from 'axios';
import './App.css' 

const csrfToken = Cookies.get('csrftoken');
const client = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true, 
});

function App() {
  const [currentUser , setCurrentUser] = useState<boolean>(false);
  const [loading , setLoading] = useState<boolean>(true);
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errorStr , setErrorStr] = useState<string>('');
  const navigate = useNavigate();

   useEffect(() => {
        client.get("/api/user/", {
            headers: {
                'X-CSRFToken': csrfToken,
            }
        })
        .then(function() {
          setCurrentUser(true);
        })
        .catch(function() {
          setCurrentUser(false);
        })
        .finally(() => {
          setLoading(false);
        })
      }, []);

  async function submitLogin(event: React.FormEvent<HTMLFormElement>){
    event.preventDefault();
    try{
      const res = await client.post(
        '/api/login/',
        {
          username,
          password,
        },
        {
          headers:{
            'X-CSRFToken': csrfToken,
          }
        }
      );
      setCurrentUser(res.data.user);
      if(res.data.user){/* navigate('/home'); */console.log('loged in '+currentUser);} 
    } catch(error){
      setErrorStr('Login failed. Please check your username and password.');
    } finally {
        setLoading(false);
    }

  }

  if(loading){return(<> <div className='loading'> LOADING... </div> </>);}
  if(currentUser){/* navigate('/home'); */ console.log('loged in '+currentUser);
  } 

  return (
    <>
       <div className="loginback">
        <div className="login">
            <h1 className="loginText">سجل الدخول</h1>
            <form className="loginForm" onSubmit={e => submitLogin(e)}>

                    <input 
                    type="text" 
                    id="username" 
                    value={username}
                    placeholder="اسم المستخدم" 
                    className="logininput"
                    onChange={(e) => setUsername(e.target.value)}
                    required
                    />
                    
                    <input 
                    type="password" 
                    id="password"
                    value={password}
                    placeholder="كلمة المرور"
                    className="logininput" 
                    onChange={(e) => setPassword(e.target.value)}                    
                    required
                    />

                    <button type="submit" className="loginbutton">ادخل</button>
                
            </form>
            {errorStr && <p className="error">{errorStr}</p>}
        </div>
        </div>
    </>
  )
}

export default App
