const fs = require('fs')
const express = require('express')
const path = require("path")
const app = express()

app.get("/", function(req, res){
    console.log("Request Received")
    fs.readFile("./count.txt", 'utf8', (err, count) => {
        if(err) throw err
        count = parseInt(count)
        count += 1
        let counter = `Number of times website was visted = ${count}`
        res.send(counter)
        console.log(counter)
        fs.writeFile("./count.txt", count.toString(), (err) => {
            if (err) throw err
        })    
    })
} )

app.get("/reset", function(req, res){
    console.log("Request Received")
    fs.readFile("./count.txt", 'utf8', (err, count) => {
        if(err) throw err
        count = parseInt(count)
        count = 0
        fs.writeFile("./count.txt", count.toString(), (err) => {
            if (err) throw err
        })    
    })
    res.sendFile(path.join(__dirname+'/index.html'))
})

app.listen(5000, function(){
    console.log("Server Started")
})