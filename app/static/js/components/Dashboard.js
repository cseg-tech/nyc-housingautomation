import React from "react";
import { Button, Row, Col, } from "react-bootstrap";
import Cookies from 'js-cookie';
import Header from "./Header"

import CustomPieChart from "./CustomPieChart"
import CustomPercentageTable from "./CustomPercentageTable"
import ComplaintCard from "./ComplaintCard"

const COMPLAINT_SUMMARY = {
  new: 10,
  open: 50,
  closed: 30
};

const COMPLAINT_BREAKUP = [
{
  "name": "Open Complaints",
  "value": 60
},
{
  "name": "Closed Complaints",
  "value": 40
}];

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
      <React.Fragment>
      <Header logout={this.props.signOut} address={address} number={num_complaints}/>
      <div className="dash">
        <div className="complaintDiv">
            <div className="upperPortion">
              <Row>
                  <Col sm={6}>
                  <div className="centerWrapper">
                    <CustomPercentageTable data={COMPLAINT_SUMMARY} title={"Complaint Data"} />
                  </div>
                  </Col>
                  <Col sm={4}>
                  <div className="centerWrapper">
                    <CustomPieChart pieData={COMPLAINT_BREAKUP} title={"Complaint Breakup"} />
                  </div>
                  </Col>
              </Row>
            </div>
            <div className="lowerPortion">
              <Row>
                  <Col>
                    <ComplaintCard header={"Administrative"} data={open_complaints} />
                  </Col>
                  <Col>
                    <ComplaintCard header={"Environmental"} data={closed_complaints} />
                  </Col>
                  <Col>
                  <ComplaintCard header={"Safety"} data={closed_complaints} />
                  </Col>
              </Row>
            </div>
        </div>
      </div>
      </React.Fragment>
    );
  }
}
