import React from "react";
import { Button, Row, Col } from "react-bootstrap";
import Cookies from 'js-cookie';

import CustomPieChart from "./CustomPieChart"
import CustomPercentageTable from "./CustomPercentageTable"
import Card from "./Card"

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
      <div>
        <Row>
          <Col sm={2} className="leftSection">
            <h3 style={{textAllign:"center"}}>70 Morningside drive</h3>
            <Button style={{textAllign:"center"}} variant="primary" >Change Building</Button>
            <br />
            <Button style={{textAllign:"center"}} variant="primary" >Edit Noficiations</Button>
            <br />
            <Button style={{textAllign:"center"}} variant="primary" onClick={this.props.signOut}>Logout</Button>
            <br />
            <a href="https://portal.311.nyc.gov/article/?kanumber=KA-01082" class="complain">Complain!</a>
          </Col>
          <Col sm={10} className="rightSection">
            <div className="headerDiv">
              <div className="headerLeft">
                <h3>{num_complaints} Complaints</h3>
                <h4>{address}</h4>
              </div>
              <Button className="accountButton">Account</Button>
            </div>
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
                  <Col sm={4}>
                    <Card header="Administrative" data={closed_complaints} />
                  </Col>
                  <Col sm={4}>
                    <Card header="Environmental" data={closed_complaints} />
                  </Col>
                  <Col sm={4}>
                    <Card header="Safety" data={closed_complaints} />
                  </Col>
                </Row>
              </div>
            </div>
          </Col>
        </Row>
      </div>
    );
  }
}