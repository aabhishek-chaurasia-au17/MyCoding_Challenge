const express = require("express")
const mongoose = require("mongoose")

const app = express()
app.use(express.urlencoded({extended:true}))

const db_url = `mongodb+srv://interview-form:DlcTS7Q45OPXXM0v@cluster0.7fweu.mongodb.net/form_input?retryWrites=true&w=majority`

const form_schema = new mongoose.Schema({
    name: String,
})

const form_model = mongoose.model("form", form_schema)

app.get("/",(req,res)=>{

    res.sendFile(`${__dirname}/form.html`)
})

app.post("/",async(req,res)=>{
    await mongoose.connect(db_url)
    const result = await form_model.create(req.body)

    res.send(`${req.body}`)
})

const Port = process.env.Port || 3000
app.listen(Port,()=>{
    console.log("Server Started!!");
})

// Rupam Joshi © 2021