const mongoose = require('mongoose');
const User = mongoose.model("UsersApi")

exports.create = async(body) => {
    let user = new User(body)
    await user.save()
}

