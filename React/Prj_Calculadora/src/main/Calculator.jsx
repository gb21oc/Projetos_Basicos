import React, {Component} from "react";
import "./Calculator.css";

import Button from "../components/Button/Button";
import Display from "../components/Display/Display";

const initialState = {
    displayValue: "0",
    clearDisplay: false,
    operation: null,
    values: [0, 0],
    current: 0
}

export default class Calculator extends Component{

    state = {...initialState}

    constructor(props){
        super(props);
        this.clearMemory = this.clearMemory.bind(this)
        this.setOperation = this.setOperation.bind(this)
        this.addDigit = this.addDigit.bind(this)
    }

    clearMemory(){
        this.setState({...initialState})
    }

    setOperation(operation){
       if(this.state.current === 0){
            this.setState({operation, current: 1, clearDisplay: true});  
            // recebe a operação, mudo o estado do current com isso começo a popular na segunda posição do array
            // defino o clearDisplay como true para poder limpar o layout
       }else{
           const equals = operation === "=";
           const currentOperation = this.state.operation;
           const values = [...this.state.values];
           try{
                values[0] = eval(`${values[0]} ${currentOperation} ${values[1]}`);
           }catch(e){
                values[0] = this.state.values[0];
           }
           
           values[1] = 0;
           this.setState({
               displayValue: values[0], 
               operation: equals ? null : operation,
               current: equals ? 0 : 1,
               clearDisplay: !equals,
               values
            });
       }
    //    console.log(this.state.operation);
    //    if(this.state.operation === "="){
    //         const num1 = parseFloat(this.state.values[0]);
    //         const num2 = parseFloat(this.state.values[1]);
    //         const result = num1 + num2;
    //         this.setState({displayValue: result});
    //         console.log(result);
    //    }
    }

    addDigit(n){
       if(n === "." && this.state.displayValue.includes(".")){ // Se o 'n' for identico ao '.' e o user já tiver colocado esse ponto ele não ira deixar
            return;
       }
       const clearDisplay = this.state.displayValue === "0" || this.state.clearDisplay;  //ou ele vai limpar quando o digito for 0 ou quando o var 'clearDisplay' for true
       const currentValue = clearDisplay ? "" : this.state.displayValue;
       const displayValue = currentValue + n;
       this.setState({displayValue, clearDisplay: false});
       if(n != "."){
            const i = this.state.current;
            const newValue = parseFloat(displayValue); // fiz o casting pois o valor esta vindo com string
            const values = [...this.state.values]; //fiz um clone do array
            values[i] = newValue;  //aqui eu falo que a primeira posição do array vai receber o valor digitado
            this.setState({values});
            console.log(values);
       }
    }


    render(){
        // const addDigit = n => this.addDigit(n);  click={() => this.clearMemory()} resolvendo o problema do this
        // const setOperation = op => this.setOperation(op); click={() => this.clearMemory()} resolvendo o problema do this
        return (
            <div className="calculator">
                <Display value={this.state.displayValue}></Display>
                <Button label="AC" click={this.clearMemory} triple></Button> {/* click={() => this.clearMemory()} resolvendo o problema do this*/}
                <Button label="/" click={this.setOperation} operation></Button>
                <Button label="7" click={this.addDigit}></Button>
                <Button label="8" click={this.addDigit}></Button>
                <Button label="9" click={this.addDigit}></Button>
                <Button label="*" click={this.setOperation} operation></Button>
                <Button label="4" click={this.addDigit}></Button>
                <Button label="5" click={this.addDigit}></Button>
                <Button label="6" click={this.addDigit}></Button>
                <Button label="-" click={this.setOperation} operation></Button>
                <Button label="1" click={this.addDigit}></Button>
                <Button label="2" click={this.addDigit}></Button>
                <Button label="3" click={this.addDigit}></Button>
                <Button label="+" click={this.setOperation} operation></Button>
                <Button label="0" click={this.addDigit} double></Button>
                <Button label="." click={this.addDigit}></Button>
                <Button label="=" click={this.setOperation} operation></Button>
            </div>
        );
    }
}