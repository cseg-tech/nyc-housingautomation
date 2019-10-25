// App.js
import React from "react";
import Cookies from 'js-cookie'

import Dashboard from "./components/Dashboard";
import HomePage from "./components/HomePage";
import Login from "./components/Login";
import SignUp from "./components/SignUp"


export default class App extends React.Component {
  constructor() {
    super();
    this.state = {
      signin : false,
      signup : false
    };
    this.signIn = this.signIn.bind(this);
    this.signUp = this.signUp.bind(this);
    this.signOut = this.signOut.bind(this);
    this.backHome = this.backHome.bind(this);
  }

  signIn() {
    console.log("Signing in");
    this.setState({signin : true});
  }

  signUp() {
    this.setState({signup : true});
  }

  signOut() {
    Cookies.remove('loginToken');
    // RELOAD DOESN'T WORK
    window.location.reload();
  }

  backHome() {
    this.setState({
      signin: false,
      signup: false
    });
  }

  render() {
    let isLoggedIn = Cookies.get('loginToken');
    if(this.state.signin) {
      return (<Login back={this.backHome} backHome={this.backHome} />)
    } else if(this.state.signup) {
      return (<SignUp back={this.backHome} backHome={this.backHome} />)
    }
    if(isLoggedIn) {
      return (<Dashboard signOut={this.signOut}/>)
    }
    return <HomePage signIn={this.signIn}  signUp={this.signUp} />
  }
}