const express = require("express")
const app = express()

app.use(express.static('projects'))

const PORT = process.env.PORT || 3000
app.listen(PORT,()=>{
    console.log("hi");
})
