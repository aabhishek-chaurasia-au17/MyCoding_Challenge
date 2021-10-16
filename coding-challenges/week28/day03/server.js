const express = require("express")
const mongoose = require("mongoose")
const redis = require('redis')

const redis_port = process.env.redis_port || 6379
const redis_client = redis.createClient(redis_port)

const {promisify} = require('util')
const getRedisAsync = promisify(redis_client.get).bind(redis_client)

const app = express()
app.use(express.urlencoded({extended:true}))

const db_helper = require("./db.js")
db_helper.init()

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



app.post("/",async(req,res)=>{
        console.log(req.body);
        const result = await employee_model.create(req.body)
    
        res.send(result)
        console.log(result);           
})
// get all datas
app.get("/datas",async(req,res)=>{
    const result = await employee_model.find({})
    res.send(result)
})

// get unique datas
app.get('/datas/:uniqueId',async(req,res)=>{
    try{
        const data = await getRedisAsync(req.params.uniqueId)
        if (data){
            const details_obj = JSON.parse(data)
            return res.json(details_obj)
        }
        console.log(data)
        const details = await employee_model.findById(req.params.uniqueId)
        redis_client.set(req.params.uniqueId,JSON.stringify(details))
        res.json(details)

    } catch(error){
        res.send({
            error:true,
            errorObj: error
        })
    }
})

const Port = process.env.Port || 3000
app.listen(Port,()=>{
    console.log("Server Started!!");
})

// Sankalp Yadav © 2021