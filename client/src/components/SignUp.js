    import React, {useState} from 'react'
    import {Form, Button} from 'react-bootstrap'
    import {Link} from 'react-router-dom'
    import {useForm} from 'react-hook-form'


    const SignUp=()=>{
        // const[username, setUsername]=useState('')
        // const[firstName, setFirstName]=useState('')
        // const[lastName, setLastName]=useState('')
        // const[email, setEmail]=useState('')
        // const[password, setPassword]=useState('')
        // const[confirmPassword, setConfirmPassword]=useState('')

        const {register, watch, handleSubmit, reset, formState: { errors } } =useForm();

        const submitForm = (data)=>{

            console.log(data)

            reset()

            // console.log('Form submitted');
            // console.log(username)
            // console.log(firstName)
            // console.log(lastName)
            // console.log(email)
            // console.log(password)
            // console.log(confirmPassword)

            // setUsername('')
            // setFirstName('')
            // setLastName('')
            // setEmail('')
            // setPassword('')
            // setConfirmPassword('')
        }



        console.log(watch("username"));
        console.log(watch("firstName"));
        console.log(watch("lastName"));
        console.log(watch("email"));
        console.log(watch("password"));
        console.log(watch("confirmPassword"))

        return (
            <div className="container">
            <div className='form'>
            
                <form>
                <Form.Group>
                    <center>
                    <h1>Sign up and start shrinking!</h1>
                    <small>Already have an account? <Link to='/login'>Login</Link></small>
                    </center>
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="text" 
                    placeholder='Enter username...'
                    {...register("username", {required:true, maxLength:25})}
                    // value={username}
                    // name="username"
                    // onChange={(e)=>{setUsername(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.username && <p style={{color:"red"}}><small>Username is required</small></p>}
                    {errors.username?.type==="maxLength" && <p style={{color:"red"}}><small>Exceeded required character</small></p>}
                </Form.Group>
                
                <br></br>
                <Form.Group>
                    <Form.Label>First Name</Form.Label>
                    <Form.Control type="text"
                    placeholder='Enter first name...'
                    {...register("firstName", {required:true, maxLength:50})}
                    // value={firstName}
                    // name="firstName"
                    // onChange={(e)=>{setFirstName(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.firstName && <p style={{color:"red"}}><small>First Name is required</small></p>}
                    {errors.firstName?.type==="maxLength" && <p style={{color:"red"}}><small>Exceeded required character</small></p>}
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Form.Label>Last Name</Form.Label>
                    <Form.Control type="text" 
                    placeholder='Enter last name...'
                    {...register ("lastName", {required:true, maxLength:50})}
                    // value={lastName}
                    // name="lastName"
                    // onChange={(e)=>{setLastName(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.lastName && <p style={{color:"red"}}><small>Last Name is required</small></p>}
                    {errors.lastName?.type==="maxLength" && <p style={{color:"red"}}>E<small>xceeded required character</small></p>}
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Form.Label>Email</Form.Label>
                    <Form.Control type="email" 
                    placeholder='Enter email address...'
                    {...register("email",{required:true, maxLength:100})}
                    // value={email}
                    // name="email"
                    // onChange={(e)=>{setEmail(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.email && <p style={{color:"red"}}><small>Email is required</small></p>}
                    {errors.email?.type==="maxLength" && <p style={{color:"red"}}><small>Exceeded required character</small></p>}
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" 
                    placeholder='Enter password...'
                    {...register("password", {required:true, minLength:6})}
                    // value={password}
                    // name="password"
                    // onChange={(e)=>{setPassword(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.password && <p style={{color:"red"}}><small>Password is required</small></p>}
                    {errors.password?.type==="minLength" && <p style={{color:"red"}}><small>Password is required</small></p>}
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Form.Label>Confirm Password</Form.Label>
                    <Form.Control type="password" 
                    placeholder='Confirm password...'
                    {...register("confirmPassword", {required:true, minLength:6})}
                    // value={confirmPassword}
                    // name="confirmPassword"
                    // onChange={(e)=>{setConfirmPassword(e.target.value)}}
                    >
                    </Form.Control>
                    {errors.confirmPassword && <p style={{color:"red"}}><small>Confirm Password </small></p>}
                    {errors.confirmPassword?.type==="minLength" && <p style={{color:"red"}}><small>Min character should be 6</small></p>}
                </Form.Group>
                <br></br>
                <Form.Group>
                    <Button  as="sub" variant="primary" onClick={handleSubmit(submitForm)}>SignUp</Button>
                    {/* <button type="button" onClick={handleReset}>Reset</button> */}
                </Form.Group>
                <br></br>
                <br></br>
                </form>
            </div>
            </div>
        )
    }
    export default SignUp