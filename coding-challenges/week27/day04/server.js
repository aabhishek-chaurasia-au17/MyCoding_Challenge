// Dependencies
const express = require('express')
const mongoose = require('mongoose')
const fileUpload = require('express-fileupload')  //MiddleWare to handle incoming Files

// Server
const app = express();
const port = process.env.PORT || 4000
app.use(express.static('public'))

// MiddleWare for handling Textual Data
app.use(express.urlencoded({ extended: true }))

//MiddleWare for handling File Data
app.use(fileUpload())

// Database
const dbHelper = require('./db.js')
dbHelper.dbInit()

// Schema 
const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
    imageUrl: {
        type: String,
    }
})

// Model
const UserModel = mongoose.model('user', UserSchema)

// Get SignUp Form
app.get('/signup', (req, res) => {
    res.sendFile(`${__dirname}/public/signUp.html`)
})

// Add User
app.post("/signup", async (req, res) => {
    try {
        // Textual Data
        const data = req.body

        // File Data (any type of file)
        const fileData = req.files.userImage // userImage is the "name" of our file input field.

        // Making a unique Filename using md5 and actual name of the file when uploaded.
        const fileName = `${fileData.md5}-${fileData.name}`

        // Path where the file is to be stored on the server.
        const filePath = `${__dirname}/public/userImages/${fileName}`

        // Saving the path/url of our file in text data
        data.imageUrl = `/userImages/${fileName}`

        // Inserting the Textual data in our mongodb Model
        const insertedData = await UserModel.create(data)

        // Moving the uploded file to the specified filePath
        fileData.mv(filePath)

        // Sending Textual data as a response to successful submission of data
        res.send(insertedData)
    }
    catch (err) {
        res.send({
            error: true,
            errorObj: err
        })
    }
})

// Get all Users (Textual)
app.get('/users', async (req, res) => {
    const users = await UserModel.find({})
    res.send(users)
})

// Get all Users (Visual)
app.get("/allUsers", async (req, res) => {
    res.sendFile(`${__dirname}/public/allUsers.html`)
})

// Starting the Server
app.listen(port, () => {
    console.log(`app listening on port : ${port}`);
});