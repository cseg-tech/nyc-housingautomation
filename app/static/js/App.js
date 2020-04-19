// App.js
import React from "react";
import Cookies from 'js-cookie'

import Dashboard from "./components/Dashboard";
import HomePage from "./components/HomePage";

import 'react-notifications/lib/notifications.css';
import {NotificationContainer} from 'react-notifications';

import "./styles/Master.css"


export default class App extends React.Component {
  constructor() {
    super();
  }
  render() {
    return (
    	<React.Fragment>
    		<HomePage />
    		<NotificationContainer/>
    	</React.Fragment>
    	)
  }
}