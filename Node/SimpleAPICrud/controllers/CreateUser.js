const util          = require("../util/createHash")
const validation    = require("../util/validateUser")
const createHash    = require("../util/createHash")
const repository    = require("../repository/RepoCreateUser")

exports.post = async(req, res, next) => {
    try{
        if(Object.keys(req.body).length === 0) return res.status(400).send({message: "It is not possible to complete the action without sending the data."})
        const {name, email, passwd, age, sex} = req.body
        let validate = new validation()
        validate.hasMaxLength(passwd, 16, "The password has exceeded the allowed size.")
        validate.hasMinLength(passwd, 8, "The password has to have at least 8 characters.")
        validate.isEmail(email, "Email is not valid format!")
        validate.verifySex(sex, "It is only allowed to choose between \"Male\" or \"Female\" ")
        validate.isNumber(age, "In this field only numbers are allowed.")
        if(!validate.isValid()){
            let errors = validate.errors()
            return res.status(400).send({message: errors})
        }
        let passwdHash = util.createHash(passwd)
        await repository.create({
            name: name,
            email: email,
            passwd: passwdHash,
            age: age,
            sex: sex
        })
        return res.status(200).send({message: "User registration in the system successfully!"})
    }catch(err){
        console.log("Deu erro: " + err)
        return res.status(500).send({message: err.message})
    }
}