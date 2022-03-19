const csurf         =  require('csurf')
const helmet        =  require("helmet")
const express       = require("express")
const config        = require("./config")
const database      = require("./database/dataBaseConnection")
const userSchema    = require("./model/UserSchema")
const createUser    = require("./router/routeCreateUser")

// Mitigating Prototype Pollution 
Object.freeze(Object.prototype);
Object.freeze(Object);

const app = express()
let csrfProtection = csurf({ cookie: true })
app.disable('x-powered-by')
app.use(helmet())
//app.use(cookieParser())
app.use(express.json())
app.use(express.urlencoded({extended:false}));

//Endpoint Create User
app.use("/user", createUser)


app.listen(80, ()=> { console.log("[*] Servidor Rodando") })