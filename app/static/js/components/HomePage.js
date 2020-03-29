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
      this.scrollDown = this.scrollDown.bind(this);
      this.scrollUp = this.scrollUp.bind(this);
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

  scrollDown() {
    let pageHeight = window.innerHeight;
    window.scrollBy(0, pageHeight);
  }

  scrollUp() {
    let pageHeight = window.innerHeight * -1;
    window.scrollBy(0, pageHeight);
  }
  
  render () {
      if(this.state.renderDashboard) {
        return <Dashboard signOut={this.signOut} back={this.goBack}/>
      }
      return (
        <div>
        <div className="heroTop" style={{zIndex: "100"}}>
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
          <div className="hero">
            <div className="heroContent">
              <p className="heroTitle">NYCAutomation</p>
              <p className="heroText">We allow you to track your landlord's housing complaints, allowing you to monitor the number of complaints lodged against them. Keep your friends close, but your landlords closer!</p>
              <br />
              <div className="buttonContent">
                <LoginPopup triggerLogin={this.enableLogin}/>
                <SignUpPopup />
              </div>
              <div className="arrow" onClick={this.scrollDown}/>
            </div>
          </div>

          <div className="hero2">
            <div className="heroContent">
              <div className="arrowTop" onClick={this.scrollUp}/>
              <div className="leftContent">
              <p className="heroTitle">Addressing your housing issues, before you need to</p>
              <p className="heroText">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
              <br />
              </div>
              <div className="arrow" onClick={this.scrollDown}/>
            </div>
          </div>

          <div className="hero3">
            <div className="heroContent">
            <div className="arrowTop" onClick={this.scrollUp}/>
              <div className="rightContent">
              <p className="heroTitle">Built by CSEG Tech</p>
              <p className="heroText">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
              <br />
              </div>
            </div>
          </div>

        </div>
      );
  }
}