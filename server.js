var http = require('http');
var app = require('./app');
var port = process.env.PORT || 4007;
http.createServer(app).listen(port);
