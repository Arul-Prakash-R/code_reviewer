const express = require('express');
const mongodb = require('mongodb');
const app = express();

mongodb.MongoClient.connect('mongodb://localhost:27017', (err, client) => {
    const db = client.db('test');
    app.get('/login', async (req, res) => {
        const user = req.query.user; // ?user[$ne]=
        const result = await db.collection('users').findOne({ username: user });
        res.send(result || "No user");
    });
    app.listen(3000);
});
ddf
