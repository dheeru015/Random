var app = require('express');
app = app();
var bodyParser = require('body-parser');
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.get('/form', (req,res,next) =>{
    res.status(200).render('form');
    
});
app.post('/form', (req,res,next) =>{
    res.status(200).render('form');
    console.log(req.body);
});

module.exports = app;