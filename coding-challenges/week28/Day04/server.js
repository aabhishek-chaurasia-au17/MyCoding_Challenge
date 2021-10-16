const express= require('express')
const cookie_parser = require('cookie-parser')
const mongoose = require("mongoose")
const db_helper = require("./db.js")
db_helper.init()

const app = express()

app.use(express.json())
app.use(cookie_parser())

const employee_schema = new mongoose.Schema({
    emp_name:{
        type: String,
        required:false,
    },
    job_name:{
        type: String,
        required:false,
    },
    hire_date:{
        type: String,
        required:false,
    },
    salary:{
        type: Number,
        required:false,
    }

})

const employee_model = mongoose.model("employee",employee_schema)



const sessions = {}
let counter_id = 50000


app.post("/login",async(req,res)=>{
    console.log(req.body);
    const result = await employee_model.create(req.body)

    res.send(result)
    console.log(result);           
})
// app.post('/login',async(req,res)=>{
//     const result = await employee_model.create(req.body)

//     sessions[counter_id] = {
//         user: req.body.email
//     }

//     res.send(`session created. your sesison id is `)

//     counter_id++
//     console.log(sessions);
// })

async function check_logged_in (req,res,next){

    console.log(req.cookies);
    const user_session_id = req.cookies.mySessionId
    const user_session = sessions[user_session_id]

    if (user_session){
        req.current_user = user_session.user
        next()
    }else{
        res.send(`you must logged in`)
    }
    // const result = await employee_model.find({})

}

app.get('/profile',check_logged_in,(req,res)=>{

    res.send(`hi, ${result}`)
})

app.listen(3000,()=>{
    console.log('server started!!');
})