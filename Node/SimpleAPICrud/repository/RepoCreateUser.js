const mongoose = require('mongoose');
const User = mongoose.model("UsersApi")

exports.create = async(body) => {
    const user = new User(body)
    await user.save()
}

exports.verifyEmail = async(email) => {
    const user = await User.findOne({email:email})
    if(user != null) return true
    return false
}

