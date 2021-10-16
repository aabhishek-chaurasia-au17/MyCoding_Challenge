const express = require("express")
const app = express()
app.use(express.urlencoded({extended:true}))
app.use(express.json())


const {MongoClient, ObjectId} = require('mongodb')
const {} = require('mongodb')
const db_url = `mongodb+srv://rest_user_api_test:UFKj63sCekRS3K7R@cluster0.x5am3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
const client = new MongoClient(db_url)
let dbRef = null


async function init(){
    await client.connect()
    db = client.db('hotel_resources')
}
init()

app.post("/details",async(req,res)=>{
    console.log("comming from insomnia");
    console.log(req.body)
    const collection_ref = db.collection('details')
    const insert_result = await collection_ref.insertOne(req.body)
    res.json(insert_result)
})

app.get("/details",async(req,res)=>{
    const collection_ref = db.collection('details')
    const all_products = await collection_ref.find({}).toArray()
    res.json(all_products)
})
app.get("/details/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('details')
    const one_product = await collection_ref.findOne({_id: new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})

app.delete("/details/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('details')
    const one_product = await collection_ref.deleteOne({"_id": new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})

app.put("/details/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('details')


    const updating = await collection_ref.updateOne({_id: new ObjectId(req.params.uniqueId)},{$set:req.body})
     res.json(updating)
})

app.listen(3000,()=>{
    console.log("SERVER Chalu ho gya!!!");
})



