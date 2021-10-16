const mongoose = require('mongoose')
let userName = 'DBAdmin'
let password = 'lhmGNLpqObqGLp66'
let dbName = 'user_database'
let dbUrl = `mongodb+srv://${userName}:${password}@cluster0.p2fbb.mongodb.net/${dbName}?retryWrites=true&w=majority`

async function dbInit(){
    await mongoose.connect(dbUrl)
}

module.exports = {
    dbInit
}