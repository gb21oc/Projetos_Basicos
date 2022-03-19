const crypto = require('crypto')
const config = require("../config")

exports.createHash = (hash) => {
    const sha256Hasher = crypto.createHmac("sha256", config.SALTKEY)
    let hashpass = sha256Hasher.update(hash).digest("hex")
    return hashpass
}