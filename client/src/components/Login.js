import React, {useState} from 'react'
import {Form, Button} from 'react-bootstrap'

const Login=()=>{

    const[email, setEmail]=useState('')
    const[password, setPassword]=useState('')
    

    const submitForm=()=>{
        console.log('Form submitted');
        console.log(email)
        console.log(password)
        

    
        setEmail('')
        setPassword('')
        
    }

    return (
    <div className="container">
           <div className='form'>
            <h1>Start shrinking!</h1>
            <p>Dont't have an account?</p>
            <br></br>
            <form>
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
                <Button  as="sub" variant="primary" onClick={submitForm}>Login</Button>
            </Form.Group>
            </form>
           </div>
        </div>
    )
}
export default Login