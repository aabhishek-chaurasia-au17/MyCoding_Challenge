const express = require("express")
const app = express()
const mongoose = require("mongoose")
const bodyParser = require("body-parser")
require('dotenv').config()

app.use(bodyParser.urlencoded({ extended: true }));

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true }, { useUnifiedTopology: true })

const productSchema = {
    productName: String,
    productPrice: String
}

const userSchema = {
    name: String,
    email: String
}

const Product = mongoose.model("Product", productSchema)
const User = mongoose.model("User", userSchema)

app.listen(4003, function () {
    console.log("Server Running at PORT: 4003")
})

app.get("/product", function (req, res) {
    res.sendFile(__dirname + "/product.html")
})

app.post("/product", function (req, res) {
    let newProduct = new Product({
        productName: req.body.productName,
        productPrice: req.body.productPrice,
    });
    newProduct.save();
    res.redirect("/")
})

app.get("/user", function (req, res) {
    res.sendFile(__dirname + "/user.html")
})

app.post("/user", function (req, res) {
    let newUser = new User({
        name: req.body.name,
        email: req.body.email,
    });
    newUser.save();
    res.redirect("/")
})

app.get("/", (req, res) => {

    let data = []

    Product.find({}, function (err, foundData) {
        if (err) {
            console.log(err);
            res.status(500).send();
        }
        else {
            if (foundData.length == 0) {
                res.status(404).send(responseObject)
            }
            else {
                data.push(foundData)
            }
        }
    })

    User.find({}, function (err, foundData) {
        if (err) {
            console.log(err);
            res.status(500).send();
        }
        else {
            if (foundData.length == 0) {
                res.status(404).send(responseObject)
            }
            else {
                data.push(foundData)
            }
        }
    })

    setTimeout(function () { res.send(JSON.parse(JSON.stringify(data))) }, 1000);

});