import React from "react";
import { Button } from "react-bootstrap";


export default class Home extends React.Component {
  constructor(props) {
      super(props);
  }
  render () {
      return (
        <div>
            <h3> Welcome to the housing portal!</h3>
            <Button variant="primary" onClick={() => this.props.signIn() }>Sign In</Button>
            <Button variant="primary" onClick={()=>this.props.signUp() }>Sign Up</Button>
        </div>
      );
  }
}