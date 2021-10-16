const express = require ('express')
const app = express ()
app.use(express.urlencoded({extended:true}))
app.use(express.json())

const {MongoClient, ObjectId} = require('mongodb')
const db_url = `mongodb+srv://heroku_app:TmAvV0gXrIDWJQqx@cluster0.i1wiv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
const client = new MongoClient(db_url)
let dbRef = null

async function init(){
    await client.connect()
    db = client.db('heroku')
}
init()

app.post("/",async(req,res)=>{
    console.log("comming from insomnia");
    console.log(req.body)
    const collection_ref = db.collection('book_details')
    const insert_result = await collection_ref.insertOne(req.body)
    res.json(insert_result)
})

app.get("/",async(req,res)=>{
    const collection_ref = db.collection('book_details')
    const all_products = await collection_ref.find({}).toArray()
    res.json(all_products)
})

app.get("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('book_details')
    const one_product = await collection_ref.findOne({_id: new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})

app.delete("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('book_details')
    const one_product = await collection_ref.deleteOne({"_id": new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})

app.put("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('book_details')
    const updating = await collection_ref.updateOne({_id: new ObjectId(req.params.uniqueId)},{$set:req.body})
     res.json(updating)
})

console.log(`heroku port is ${process.env.PORT}`);
const PORT = process.env.PORT || 3000

app.listen(PORT,()=>{
    console.log(`Server Started at ${PORT} port`);
})


// https://heroku-exaple-app.herokuapp.com/