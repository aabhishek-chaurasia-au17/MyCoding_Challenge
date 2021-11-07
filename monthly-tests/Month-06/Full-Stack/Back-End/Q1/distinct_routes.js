const express = require("express");
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const { MongoClient, ObjectId } = require("mongodb");

const database_url = `mongodb+srv://abhishekc838:8i9ULznFrUuwjlxW@cluster0.itoag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`;
const clients = new MongoClient(database_url);

async function init() {
  await clients.connect();
  db = clients.db("resources");
}


init();

app.post("/details", async (req, res) => {
  console.log("comming from postman");

  const collection_reference = db.collection("details");
  const result = await collection_reference.insertOne(req.body);
  res.json(result);

  const data = {
    timestamp: new Date(),
    method_name: "post",
    route_path: "/details",
    ip_add: req.ip,
  };
  console.log(data);
});

app.get("/details", async (req, res) => {
  const collection_ref = db.collection("details");
  const all_products = await collection_ref.find({}).toArray();
  res.json(all_products);
  const data = {
    timestamp: new Date(),
    method_name: "get",
    route_path: "/details",
    ip_add: req.ip,
  };
  console.log(data);
});
app.get("/details/:uniqueId", async (req, res) => {
  const collection_ref = db.collection("details");
  const one_product = await collection_ref.findOne({
    _id: new ObjectId(req.params.uniqueId),
  });
  res.json(one_product);
  const data = {
    timestamp: new Date(),
    method_name: "get",
    route_path: "/details/:uniqueId",
    ip_add: req.ip,
  };
  console.log(data);
});

app.delete("/details/:uniqueId", async (req, res) => {
  const collection_ref = db.collection("details");
  const one_product = await collection_ref.deleteOne({
    _id: new ObjectId(req.params.uniqueId),
  });
  res.json(one_product);
  const data = {
    timestamp: new Date(),
    method_name: "delete",
    route_path: "/details/:uniqueId",
    ip_add: req.ip,
  };
  console.log(data);
});

app.put("/details/:uniqueId", async (req, res) => {
  const collection_ref = db.collection("details");
  const updating = await collection_ref.updateOne(
    { _id: new ObjectId(req.params.uniqueId) },
    { $set: req.body }
  );
  res.json(updating);
  const data = {
    timestamp: new Date(),
    method_name: "put",
    route_path: "/details/:uniqueId",
    ip_add: req.ip,
  };
  console.log(data);
});

app.listen(5000, () => {
  console.log("Server is ready!!!");
});

// abhishekc838
// 8i9ULznFrUuwjlxW