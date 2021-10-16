const express = require ("express")
const app = express()
const {MongoClient} = require('mongodb')


app.use(express.urlencoded({extended:true}))

app.get("/",(req,res)=>{
    res.sendFile(`${__dirname}/mongodb.html`)
})
const db_url = `mongodb+srv://mongodb_learning:sankalpsid@cluster0.rh3b8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
const client = new MongoClient(db_url)

app.post('/',async(req,res)=>{
    console.log(req.body)
    await client.connect()
    const db = client.db('mongodb_form')
    const collectionRef = db.collection('mongodb_data')
    const insertResult = await collectionRef.insertOne(req.body)
    res.send(insertResult)
})
// mongodb_learning
// sankalpsid
app.listen(3000,()=>{
    console.log("Server Started !!!! Yuhuuu !!!");
})