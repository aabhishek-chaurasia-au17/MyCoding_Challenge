const mongoose = require("mongoose")
const db_url = `mongodb+srv://Employers_app:hAw0Rr1xhGumYpqV@cluster0.ziojd.mongodb.net/Employers_list?retryWrites=true&w=majority`

async function init(){
    await mongoose.connect(db_url)
}

module.exports = {
    init
}
// Sankalp Yadav © 2021
