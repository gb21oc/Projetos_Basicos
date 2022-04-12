const util          = require("../util/createHash")
const validation    = require("../util/validateUser")
const repository    = require("../repository/RepoLogin")
const auth          = require("../services/auth-service")

exports.post = async(req, res, next) => {
    try{
        if(Object.keys(req.body).length === 0) return res.status(400).send({message: "It is not possible to complete the action without sending the data."})
        const {email, passwd} = req.body
        let validate = new validation()
        validate.hasMaxLength(passwd, 16, "The password has exceeded the allowed size.")
        validate.hasMinLength(passwd, 8, "The password has to have at least 8 characters.")
        validate.isEmail(email, "Email is not valid format!")
        if(!validate.isValid()){
            let errors = validate.errors()
            return res.status(400).send({message: errors})
        }
        let passwdHash = util.createHash(passwd)
        const user = await repository.authenticate({
            email: email,
            passwd: passwdHash
        })
        if(!user) {
            return res.status(404).send({message: "Invalid User and Password"})
        }
        
        const token = await auth.generateToken({
            email: user.email,
            name: user.name
        })

        res.status(200).send({
            token: token,
            data: {
                id: user._id,
                email: user.email,
                name: user.name
            }
        })
        
    }catch(err){
        console.log("Deu erro: " + err)
        if(err.message.indexOf("E11000") != -1) return res.status(500).send({message: "This e-mail has already registered"})
        if(err.message.indexOf("10000ms") != -1) return res.status(500).send({message: "Timeout, try again"})
        return res.status(500).send({message: "Failure to process the request"})
    }
}