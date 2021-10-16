const express = require("express")
const fileuploadmiddleware = require('express-fileupload')
const expressSession = require('express-session')
const mongoose = require ('mongoose')
const app = express()

app.use(express.static('images'))

db_url = `mongodb+srv://form_1:DhOnecPHDrvuTTBk@cluster0.k41hw.mongodb.net/entry_list?retryWrites=true&w=majority`
app.use(fileuploadmiddleware())
app.use(express.urlencoded({extended:true}))
// DhOnecPHDrvuTTBk
// entry_list
// form_1
const one_day = 3600000 * 24
app.use(expressSession({
    secret: "abcd",
    saveUninitialized: true,
    resave: false,
    name: "form_1",
    cookie:{ maxAge:one_day}
}))


const entry_form_schema = new mongoose.Schema({
    name:{
        type: String,
        required: false, 
    },
    email:{
        type: String,
        required: false,
    },
    pass:{
        type: String,
        required: false
    },imageURL:{
        type:String,
        required: false
    } 
})

const entry_form_model = mongoose.model("list",entry_form_schema)

app.get('/',(req,res)=>{
    res.sendFile(`${__dirname}/index.html`)
})


var auth_pass = false
app.post('/login', async(req,res)=>{
    const {name, email, pass} = req.body
    await mongoose.connect(db_url)


    const check_email = await entry_form_model.findOne({email:email})
    const check_pass = await entry_form_model.findOne({pass:pass})
    if ((email === check_email.email) && (pass === check_pass.pass)){
        auth_pass = true
        res.redirect('/user')
    } 
    else{
        res.send("Incorrect Email/Password")
    }
    
})


app.get('/signup',(req,res)=>{
    res.sendFile(`${__dirname}/signup.html`)
})

app.get('/signup/all', async(req,res)=>{
    await mongoose.connect(db_url)
    const insertedData = await entry_form_model.find({})
    res.send(insertedData)
})

app.post('/signup',async(req,res)=>{
    await mongoose.connect(db_url)
    const fileData = req.files.image
    console.log("file received", fileData);

    const fileName = `${fileData.md5}-${fileData.name}`
    const filePath = `${__dirname}/images/${fileName}`
    await fileData.mv(filePath)

    req.body.imageURL = fileName
    const inseredData = await entry_form_model.create(req.body)

    auth_pass = true
    res.redirect('/user')
})


function checkAuth(req,res,next){

    if (auth_pass == true){
        next()
    }
    else{
        res.redirect('/')
    }
}

app.get('/user',checkAuth,(req,res)=>{
    res.sendFile(`${__dirname}/user.html`)
})

const PORT = process.env.PORT || 3000

app.listen(PORT,()=>{
    console.log("Server start ho gya!!");
})