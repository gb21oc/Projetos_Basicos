const express = require("express")
const router = express.Router();
const login = require("../controllers/UserLogin")

router.post("/login", login.post)

module.exports = router