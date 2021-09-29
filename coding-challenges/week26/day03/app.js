// Call Express Api.
const express = require('express')
// Call express Session Api.
const session = require('express-session')
const app = express();

// Session Setup
app.use(
    session({

        // It holds the secret key for session
        secret: "secret",

        // Forces the session to be saved
        // back to the session store
        resave: true,

        // Forces a session that is "uninitialized"
        // to be saved to the store
        saveUninitialized: false,
        cookie: {
        }
    })
);

// The server object listens on port 3000.
app.listen(3000, function () {
    console.log("Express Started on Port 3000");
});

// Get function in which send session as routes.
app.get('/', function (req, res, next) {

    if (req.session.views) {

        // Increment the number of views.
        req.session.views++

        // Print the views.
        res.write('<p> No. of views: '
            + req.session.views + '</p>')
        res.end()
    } else {
        req.session.views = 1
        res.write('<p> No. of views: '
            + req.session.views + '</p>')
        res.end()
    }
})

app.get('/reset', function (req, res, next) {
    req.session.views = 0;
    return res.end('<h1>Reset successful</h1>');
})


