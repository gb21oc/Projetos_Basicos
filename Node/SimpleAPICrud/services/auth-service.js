const jwt = require("jsonwebtoken")
const config = require("../config")

exports.generateToken = async(data) => {
    return jwt.sign(data, config.SALTKEY, {expiresIn: '300000'})
}

exports.decodeToken = async(jwtToken) => {
    const data = await jwt.verify(jwtToken, config.SALTKEY)
    return data
}

exports.authorize = (req, res, next) => {
    const token = req.headers['x-access-token']
    if(!token){
        res.status(401).send({
            message: "[-] Not Authorized."
        })
    }else{
        jwt.verify(token, config.SALTKEY, (error, decoded)=>{
            if(error) res.status(401).send({message:"[-] Invalid Token, re-login again."})
            else next()
        })
    }
}