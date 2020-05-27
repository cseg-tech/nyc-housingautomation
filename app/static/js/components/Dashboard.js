import React from "react";
import { Button, Row, Col, } from "react-bootstrap";
import Cookies from 'js-cookie';
import Header from "./Header"

import CustomPieChart from "./CustomPieChart"
import CustomPercentageTable from "./CustomPercentageTable"
import ComplaintCard from "./ComplaintCard"
import CustomBarChart from "./BarChart"


const COMPLAINT_SUMMARY = [
  {name: "Complaints", environmental: 30, administrative: 40, safety: 30},
];

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
                  <div className="chart">
                    <CustomBarChart data = {COMPLAINT_SUMMARY}/>
                  </div>
                  </Col>
                  <Col sm={4}>
                  <div className="chart">
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
                    <ComplaintCard header={"Environmental"} data={open_complaints} />
                  </Col>
                  <Col>
                  <ComplaintCard header={"Safety"} data={open_complaints} />
                  </Col>
              </Row>
            </div>
        </div>
      </div>
      </React.Fragment>
    );
  }
}
