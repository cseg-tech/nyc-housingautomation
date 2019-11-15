import React from "react";
import LazyHero from 'react-lazy-hero';
import LoginPopup from './LoginPopup';
import SignUpPopup from "./SignUpPopup";
import Dashboard from "./Dashboard";
import Cookies from 'js-cookie'

export default class Home extends React.Component {
  constructor() {
      super();
      this.state = {
        loginEnable: false,
        renderDashboard: false
      }
      this.activateDash = this.activateDash.bind(this);
      this.enableLogin = this.enableLogin.bind(this);
      this.signOut = this.signOut.bind(this);
      this.goBack = this.goBack.bind(this);
  }

  enableLogin() {
    this.setState({
      loginEnable:true
    });
  }

  signOut() {
    Cookies.remove('loginToken');
    this.setState({
      loginEnable: false,
      renderDashboard: false
    });
  }

  goBack() {
    this.setState({
      renderDashboard: false
    })
  }

  activateDash() {
    this.setState({renderDashboard: true});
  }
  
  render () {
      if(this.state.renderDashboard) {
        return <Dashboard signOut={this.signOut} back={this.goBack}/>
      }
      return (
        <div>
          <div className="hero">
            <div className="heroContent">
              <div className="heroTop">
                {
                  this.state.loginEnable? (
                      <a href="#" onClick={this.activateDash} className="heroURL">My Dashboard</a>
                    ): (
                    <span></span>
                    )
                }
                <a href="http://www.columbiaseg.org/cseg-tech" className="heroURL">CSEG Tech</a>
                <a href="https://github.com/cseg-tech/nyc-housingautomation" className="heroURL">Github</a>
              </div>
              <p className="heroTitle">NYCAutomation</p>
              <p className="heroText">We allow you to track your landlord's housing complaints, allowing you to monitor the number of complaints lodged against them. Keep your friends close, but your landlords closer!</p>
              <br />
              <div className="buttonContent">
                <LoginPopup triggerLogin={this.enableLogin}/>
                <SignUpPopup />
              </div>
              <div className="arrow" />
            </div>
          </div>
        </div>
      );
  }
}