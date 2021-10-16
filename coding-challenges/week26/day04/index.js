const express = require('express');
const mongoose = require('mongoose');
const app = express();
require('dotenv').config()

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true }, { useUnifiedTopology: true })
mongoose.Promise = global.Promise;

app.use(express.static('public'));
app.use(express.json());

app.use('/api', require('./routes/api'));

app.use(function (err, req, res, next) {
    res.status(422).send({ error: err.message });
});

app.listen(4000, function () {
    console.log('Listening on PORT 4000');
});