const express = require("express")
const fileuploadmiddleware = require('express-fileupload')
const mongoose = require ('mongoose')
const jwt = require('jsonwebtoken')
const datas_routes = require('./datas/datas')

const app = express()

app.use(express.static('images'))
app.use(express.static('public'))
app.use(express.urlencoded({extended:true}))
app.use(express.json())
app.use(fileuploadmiddleware())
app.use("/details",datas_routes)

db_url = `mongodb+srv://form_1:DhOnecPHDrvuTTBk@cluster0.k41hw.mongodb.net/entry_list?retryWrites=true&w=majority`
// DhOnecPHDrvuTTBk
// entry_list
// form_1


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
app.post('/signup', async(req,res)=>{
    try {
        await mongoose.connect(db_url)
        const {name, email, pass} = req.body
        console.log('req.body',req.body);
        // validation
        if (!email || !pass){
            res.json({
                error: true,
                message: "Empty data"
            })
            return
        }
        const oldUserPresent = await entry_form_model.findOne({email:email})

        if (oldUserPresent && oldUserPresent.email === email){
            res.json({
                error: true,
                message: "user already existing"
            })
            return
        }
        const userInserted = await entry_form_model.create({email:email, pass: pass})

        res.json(userInserted)
    } catch (err) {
        res.json({
            error:true,
            errorObj:err,
            message:"Unknown Error"
        })
    }
})

app.post('/login', async (req, res) => {


    try {
        const {email, pass} = req.body
        console.log("app.post ~ req.body", req.body)

        //validations
        if (!email || !pass) {
            res.json({
                error: true,
                message: "Empty data"
            })
            return
        }

        const oldUserPresent = await entry_form_model.findOne({ email: email})
        
        if (oldUserPresent && oldUserPresent.email === email && oldUserPresent.pass === pass) {
            //

            //generate a token
            const secret = "This is my secret key"
            const jwtToken = jwt.sign({ currentUser: oldUserPresent.email }, secret, { expiresIn: '2d' })

            res.json({
                error: false,
                message: "User Logged in",
                token: jwtToken
            })
            return
        }


        res.json({
            error: true,
            message: "User credentials does not match"
        })

    
    
    } catch (err) {
        res.json({
            error: true,
            errorObj: err,
            message: "Unknown Error"
        })
    }

})

// SankalpYadav©2021

const PORT = process.env.PORT || 3000

app.listen(PORT,()=>{
    console.log("Server start ho gya!!");
})