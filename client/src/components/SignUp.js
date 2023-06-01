import React, {useState} from 'react'
import {Form, Button} from 'react-bootstrap'


const SignUp=()=>{
    const[username, setUsername]=useState('')
    const[firstName, setFirstName]=useState('')
    const[lastName, setLastName]=useState('')
    const[email, setEmail]=useState('')
    const[password, setPassword]=useState('')
    const[confirmPassword, setConfirmPassword]=useState('')

    const submitForm=()=>{
        console.log('Form submitted');
        console.log(username)
        console.log(firstName)
        console.log(lastName)
        console.log(email)
        console.log(password)
        console.log(confirmPassword)

        setUsername('')
        setFirstName('')
        setLastName('')
        setEmail('')
        setPassword('')
        setConfirmPassword('')
    }

    return (
        <div className="container">
           <div className='form'>
            <h1>Sign up and start shrinking!</h1>
            <p>Already have an account?</p>
            <br></br>
            <form>
            <Form.Group>
                <Form.Label>Username</Form.Label>
                <Form.Control type="text" 
                placeholder='Enter username...'
                value={username}
                name="username"
                onChange={(e)=>{setUsername(e.target.value)}}
                >
                </Form.Control>
            </Form.Group>
            <br></br>
            <Form.Group>
                <Form.Label>First Name</Form.Label>
                <Form.Control type="text"
                placeholder='Enter first name...'
                value={firstName}
                name="firstName"
                onChange={(e)=>{setFirstName(e.target.value)}}
                >
                </Form.Control>
            </Form.Group>
            <br></br>
            <Form.Group>
                <Form.Label>Last Name</Form.Label>
                <Form.Control type="text" 
                placeholder='Enter last name...'
                value={lastName}
                name="lastName"
                onChange={(e)=>{setLastName(e.target.value)}}
                >
                </Form.Control>
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
                <Form.Label>Confirm Password</Form.Label>
                <Form.Control type="password" 
                placeholder='Confirm password...'
                value={confirmPassword}
                name="confirmPassword"
                onChange={(e)=>{setConfirmPassword(e.target.value)}}
                >
                </Form.Control>
            </Form.Group>
            <br></br>
            <Form.Group>
                <Button  as="sub" variant="primary" onClick={submitForm}>SignUp</Button>
            </Form.Group>
            </form>
           </div>
        </div>
    )
}
export default SignUp