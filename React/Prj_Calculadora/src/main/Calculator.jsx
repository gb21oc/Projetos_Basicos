import React, {Component} from "react";
import "./Calculator.css";

import Button from "../components/Button/Button";
import Display from "../components/Display/Display";

export default class Calculator extends Component{
    render(){
        return (
            <div className="calculator">
                <Display value={100}></Display>
                <Button label="AC"></Button>
                <Button label="/"></Button>
                <Button label="7"></Button>
                <Button label="8"></Button>
                <Button label="9"></Button>
                <Button label="*"></Button>
                <Button label="4"></Button>
                <Button label="5"></Button>
                <Button label="6"></Button>
                <Button label="-"></Button>
                <Button label="1"></Button>
                <Button label="2"></Button>
                <Button label="3"></Button>
                <Button label="+"></Button>
                <Button label="0"></Button>
                <Button label="."></Button>
                <Button label="="></Button>
            </div>
        );
    }
}