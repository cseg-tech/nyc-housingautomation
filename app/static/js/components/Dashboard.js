import React from "react";
import { Button, Row, Col } from "react-bootstrap";
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
        <Row>
          <Col sm={2}>
            <h3 style={{textAllign:"center"}}>70 Morningside drive</h3>
            <Button style={{textAllign:"center"}} variant="primary" >Change Building</Button>
            <br />
            <Button style={{textAllign:"center"}} variant="primary" >Edit Noficiations</Button>
            <br />
            <Button style={{textAllign:"center"}} variant="primary" onClick={this.props.signOut}>Logout</Button>
            <br />
            <a href="https://portal.311.nyc.gov/article/?kanumber=KA-01082" class="complain">Complain!</a>
          </Col>
          <Col sm={10}>
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
                  <Col>
                    <div className="centerWrapper">
                      <h4>Heading here</h4>
                    </div>
                  </Col>
                  <Col>
                    <div className="centerWrapper">
                      <h4>Pie chart here</h4>
                    </div>
                  </Col>
                </Row>
              </div>
              <div className="lowerPortion">
                <Row>
                  <Col>
                    <div className="centerWrapper">
                      <h4>Admin here</h4>
                    </div>
                  </Col>
                  <Col>
                    <div className="centerWrapper">
                      <h4>Env here</h4>
                    </div>
                  </Col>
                  <Col>
                    <div className="centerWrapper">
                      <h4>Safety here</h4>
                    </div>
                  </Col>
                </Row>
              </div>
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
            </div>
          </Col>
        </Row>
      </div>
    );
  }
}