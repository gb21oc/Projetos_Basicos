// Express
const express = require("express")
const app = express()
// Other
const config = require("./config")
const database = require("./database/dataBaseConnection")
const userSchema = require("./model/UserSchema")

app.use(express.json())
app.use(express.urlencoded({extended:false}));
app.listen(80, ()=> { console.log("Servidor Rodando") })