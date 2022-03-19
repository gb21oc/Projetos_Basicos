let errors = []

function GuardErros(){
    errors = []
}

GuardErros.prototype.isEmail = (email, message)=> {
    let regex = new RegExp(/^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/)
    if(!regex.test(email)) errors.push(message)
}

GuardErros.prototype.hasMinLength = (text, min, message)=>{
    if(text == "" || text == null) errors.push({message: "It is not possible to pursue empty data."})
    if(text.length < min) errors.push(message)
}

GuardErros.prototype.hasMaxLength = (text, max, message) => {
    if(text == "" || text == null) errors.push({message: "It is not possible to pursue empty data."})
    if(text.length > max) errors.push(message)
}

GuardErros.prototype.verifySex = (sex, message) => {
    if(sex == "" || sex == null) errors.push({message: "It is not possible to pursue empty data."})
    if(sex.toUpperCase() !== "MALE" && sex.toUpperCase() !== "FEMALE"){
        errors.push(message)
    }
}

GuardErros.prototype.isNumber = (number, message) => {
    if(!(!isNaN(parseFloat(number)) && isFinite(number))) errors.push(message)
}

GuardErros.prototype.errors = () => {
    return errors;
}

GuardErros.prototype.isValid = () => {
    if(errors.length == 0){
        return true;
    }else{
        return false;
    }
}

module.exports = GuardErros