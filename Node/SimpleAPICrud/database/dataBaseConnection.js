const config = require("../config")
const mongoose = require('mongoose')


const connectingDatabase = async() => {
    await mongoose.connect(config.connectionString,{useUnifiedTopology:true})
    .then(() => {
        console.log("[*] Success when connection to the database")
    }).catch((err) => {
        console.log("[-] An error occurred while connecting to the database: " + err)
    })


}
connectingDatabase()