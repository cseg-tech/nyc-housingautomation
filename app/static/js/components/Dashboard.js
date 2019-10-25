import React from "react";
import { Button } from "react-bootstrap";

export default class Dashboard extends React.Component {
  constructor(props) {
    super(props);
  }
  render () {
    return (
      <div>
        <h3>Dashboard here</h3>
        <Button variant="primary" onClick={this.props.signOut}>Logout</Button>
      </div>
    );
  }
}