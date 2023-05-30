import React, {useEffect,useState} from 'react'
import ReactDom from 'react-dom'



const App=()=>{

    useEffect(
        ()=>{
            fetch('/user')
            .then(response=>response.json())
            .then(data=>{console.log(data)
                setMessage(data.message)
            })
            .catch(err=>console.log(err))
            
        },[]
    )
    const[message,setMessage]=useState('')
    return(
        <div className="app">
            {message}
        </div>
    )
}

ReactDom.render(<App/>, document.getElementById('root'));
