import React from "react";
import { Button } from "react-bootstrap";
import Cookies from 'js-cookie'

export default class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open_complaints: [],
      closed_complaints: [],
      num_complaints: 0,
      address: ""
    }
  }

  componentDidMount() {
    let UID = Cookies.get('loginToken');
    console.log("Fetching complaints for:"+UID);
    let payload = {UID};
    let that = this;
    fetch('/getBBLDetails', {method: 'post', body:JSON.stringify(payload)})
        .then(function(response) {return response.json();})
        .then(function(data) {
            console.log(data);
            let addressFetch = data["address"]
            let openFetch = data["open_complaints"]
            let closedFetch = data["closed_complaints"]
            let number = data["number"]
            that.setState({
              address:addressFetch,
              open_complaints: openFetch,
              closed_complaints: closedFetch,
              num_complaints: number
            })
        });
  }

  render () {
    console.log(this.state);
    let {open_complaints, closed_complaints, address, num_complaints} = this.state;
    return (
      <div>
        <h3>Complaints for: {address} are: {num_complaints}</h3>
        <h4>Open Complaints</h4>
        {
          open_complaints.map((complaint) => (
            <p>{JSON.stringify(complaint)}</p>
          ))
        }
        <h4>Closed Complaints</h4>
        {
          closed_complaints.map((complaint) => (
            <p>{JSON.stringify(complaint)}</p>
          ))
        }
        <Button variant="primary" >Change Building</Button>
        <Button variant="primary" >Edit Noficiations</Button>
        <Button variant="primary" onClick={this.props.back}>Back</Button>
        <Button variant="primary" onClick={this.props.signOut}>Logout</Button>
      </div>
    );
  }
}