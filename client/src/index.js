import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react'
import ReactDom from 'react-dom'
import NavBar from './components/Navbar';

import {
     BrowserRouter as Router, 
     Routes,
     Route 
    } from 'react-router-dom';
// import { Switch } from 'react-router-dom';

import Home from './components/Home';
import SignUp from './components/SignUp';
import Login from './components/Login';
import Platform from './components/Platform';


const App=()=>{

    return (
        <Router>
        <div className="container">
            <NavBar/>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/register" element={<SignUp />} />
                <Route path="/login" element={<Login />} />
                <Route path="/platform" element={<Platform />} />
                {/* <Route path="/platform">
                    <PlatformPage/>
                </Route>
                <Route path="/login">
                    <LoginPage/>
                </Route>
                <Route path="/register">
                    <SignUpPage/>
                </Route>
                <Route path="/">
                    <HomePage/>
                </Route> */}
                
            </Routes>
        </div>
        </Router>
        
    )
}

ReactDom.render(<App/>, document.getElementById('root'))
