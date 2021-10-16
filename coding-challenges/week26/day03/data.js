const express = require("express")

const app = express()
app.use(express.urlencoded({extended:true}))

const {MongoClient} = require('mongodb')
const db_url = `mongodb+srv://products_app:24uLpByPAGO7Iiya@cluster0.kopiz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
const client = new MongoClient(db_url)


let db = null
let collectionRef1 = null
let collectionRef2 = null

async function init(){
    await client.connect()
    db = client.db('collections')
    collectionRef1 = db.collection('products')
    collectionRef2 = db.collection("names")

}
init()

app.get("/product_details", (req,res)=>{
    res.sendFile(`${__dirname}/product_details.html`)
})

app.post('/product_details',async(req,res)=>{
    console.log(req.body)
    let insertResult = await collectionRef1.insertOne(req.body)
    res.send(insertResult)
})

app.get('/product_datas',async(req,res)=>{
    let data = await collectionRef1.find({}).toArray()
     res.send(data)
})

app.get("/", (req,res)=>{
    res.sendFile(`${__dirname}/user_details.html`)
})

app.post('/',async(req,res)=>{
    console.log(req.body)
    let insertResult = await collectionRef2.insertOne(req.body)
    res.send(insertResult)
})

app.get('/user_datas',async(req,res)=>{
    let data = await collectionRef2.find({}).toArray()
     res.send(data)
 })


// products_app
// 24uLpByPAGO7Iiya

app.listen(3000,()=>{
    console.log("Server Started!!!")
})