const express = require ('express')
const app = express ()
app.use(express.urlencoded({extended:true}))


app.get('/',(req,res)=>{
    console.log("hi")
    res.sendFile(`${__dirname}/queue_heroku.html`)
})

app.get('/queue_heroku.js',(req,res)=>{
    res.sendFile(`${__dirname}/queue_heroku.js`)
})

const PORT = process.env.PORT || 3000

app.listen(PORT,()=>{
    console.log('Server started');
})
// https://queue-by-heroku.herokuapp.com/