const express = require("express")
const router = express.Router();
const createUser = require("../controllers/CreateUser")

router.post("/create", createUser.post)

module.exports = router