const express = require("express")
const {MongoClient, ObjectId} = require('mongodb')
const jwt = require('jsonwebtoken')
const {Router} = require ("express")

const datas_routes = Router()

datas_routes.use(express.urlencoded({extended:true}))
datas_routes.use(express.json())



const db_url = `mongodb+srv://rest_user_api_test:UFKj63sCekRS3K7R@cluster0.x5am3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
const client = new MongoClient(db_url)
let dbRef = null


async function init(){
    await client.connect()
    db = client.db('Employers')
}
init()




function checkJWTtoken(req,res,next){
    try {
        const authtokendata = jwt.verify(req.query.authtoken,"this is my secret key")
        console.log(authtokendata)
        next()
    } catch (error) {
        res.json({
            error:true,
            errorObj: error,
            message: "Invalid Token"
        })
    }
}

datas_routes.use(checkJWTtoken)

datas_routes.post("/",async(req,res)=>{
    console.log("comming from insomnia");
    console.log(req.body)
    const collection_ref = db.collection('employee')
    const insert_result = await collection_ref.insertOne(req.body)
    res.json(insert_result)
})

datas_routes.get("/",async(req,res)=>{
    const collection_ref = db.collection('employee')
    const all_products = await collection_ref.find({}).toArray()
    res.json(all_products)
})
datas_routes.get("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('employee')
    const one_product = await collection_ref.findOne({_id: new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})
// SankalpYadav©2021
datas_routes.delete("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('employee')
    const one_product = await collection_ref.deleteOne({"_id": new ObjectId(req.params.uniqueId)})
    res.json(one_product)
})
// SankalpYadav©2021
datas_routes.put("/:uniqueId",async(req,res)=>{
    const collection_ref = db.collection('employee')
    const updating = await collection_ref.updateOne({_id: new ObjectId(req.params.uniqueId)},{$set:req.body})
     res.json(updating)
})

module.exports = datas_routes


