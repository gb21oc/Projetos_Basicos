const mongoose = require("mongoose")
const User = mongoose.model("UsersApi")

exports.authenticate = async(body) => {
    const userLogon = await User.findOne({
        email: body.email,
        passwd: body.passwd
    })
    return userLogon
}