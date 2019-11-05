import React from "react";
import { Button } from "react-bootstrap";
import LazyHero from 'react-lazy-hero';


export default class Home extends React.Component {
  constructor(props) {
      super(props);
  }
  
  render () {
      return (
        <div>
          <div className="hero">
            <div className="heroContent">
              <div className="heroTop">
                <a href="http://www.columbiaseg.org/cseg-tech" className="heroURL">CSEG Tech</a>
                <a href="https://github.com/cseg-tech/nyc-housingautomation" className="heroURL">Github</a>
              </div>
              <p className="heroTitle">NYCAutomation</p>
              <p className="heroText">We allow you to track your landlord's housing complaints, allowing you to monitor the number of complaints lodged against them. Keep your friends close, but your landlords closer!</p>
              <br />
              <div className="buttonContent">
                <Button className="splashButton" variant="primary" onClick={() => this.props.signIn() } style={{marginRight:"0.5vw"}}>Login</Button>
                <Button className="splashButton" variant="primary" onClick={()=>this.props.signUp() } style={{marginLeft:"0.5vw"}}>Sign Up</Button>
              </div>
              <div className="arrow" />
            </div>
          </div>
        </div>
      );
  }
}