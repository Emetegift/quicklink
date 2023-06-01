import React, {useState} from 'react'
import {Form, Button} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import {useForm} from 'react-hook-form'

const Login=()=>{

    const[email, setEmail]=useState('')
    const[password, setPassword]=useState('')
    

    const loginUser=()=>{
        // console.log('Form submitted');
        console.log(email)
        console.log(password)
    
        setEmail('')
        setPassword('')
        
    }

    return (
    <div className="container">
           <div className='form'>
            
           
            <form>
            <Form.Group>
                <h1>Start shrinking!</h1>
                <small>Do not have an account? <Link to='/register'>Create an account</Link></small>
            </Form.Group>
                   
                <br></br>
            <Form.Group>
                <Form.Label>Email</Form.Label>
                <Form.Control type="email" 
                placeholder='Enter email address...'
                value={email}
                name="email"
                onChange={(e)=>{setEmail(e.target.value)}}
                >
                </Form.Control>
            </Form.Group>
            <br></br>
            <Form.Group>
                <Form.Label>Password</Form.Label>
                <Form.Control type="password" 
                placeholder='Enter password...'
                value={password}
                name="password"
                onChange={(e)=>{setPassword(e.target.value)}}
                >
                </Form.Control>
            </Form.Group>
            <br></br>
            <Form.Group>
                <Button  as="sub" variant="primary" onClick={loginUser}>Login</Button>
            </Form.Group>
            <br></br>
            </form>
           </div>
        </div>
    )
}
export default Login