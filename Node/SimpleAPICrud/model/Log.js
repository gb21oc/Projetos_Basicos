const mongoose = require('mongoose');
const Schema = mongoose.Schema

const schema = new Schema({
    log:{
        type: String,
        trim: true
    },
    webBrowser:{
        type: String,
        trim: true
    },
    dateTime:{
        type: String,
        trim: true
    }
})