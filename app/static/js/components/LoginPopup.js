import React from "react";
import Popup from "reactjs-popup";
import { Button, Form } from "react-bootstrap";
import Cookies from 'js-cookie'

export default class LoginPopup extends React.Component {

  constructor(props) {
      super(props);
      this.state = {
          email: "",
          password: ""
      }
      this.setEmail = this.setEmail.bind(this);
      this.setPassword = this.setPassword.bind(this);
      this.validateForm = this.validateForm.bind(this);
  }

  validateForm() {
    return true;
  }

  setEmail(target) {
    this.setState({email:target});
  }

  setPassword(target) {
    this.setState({password:target});
  }

  render() {
    return (
        <Popup trigger={<Button className="splashButton" variant="primary" style={{marginRight:"0.5vw"}}>Login</Button>} modal closeOnDocumentClick>
        {close => (
              <div className="Login" style={{marginLeft:"10vw", marginRight:"10vw"}}>
              <Form.Group controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control value={this.state.email} onChange={e => this.setEmail(e.target.value)} type="email" placeholder="Enter email" />
                  <Form.Text className="text-muted">
                  We'll never share your email with anyone else.
                  </Form.Text>
              </Form.Group>

              <Form.Group value={this.state.password} onChange={e => this.setPassword(e.target.value)} controlId="formBasicPassword">
                  <Form.Label>Password</Form.Label>
                  <Form.Control type="password" placeholder="Password" />
              </Form.Group>
              <Button variant="primary" disabled={!this.validateForm} onClick={() => {
                let {email, password} = this.state;
                let payload = {
                  email, password
                };
                var that = this;
                fetch('/loginUser', {method: 'post', body:JSON.stringify(payload)})
                    .then(function(response) {return response.json();})
                    .then(function(data) {
                        console.log(data);
                        const uniqueID = data['id']
                        const statusCode = data['status']
                        if(statusCode == 0) {
                          console.log("Logging in...")
                          Cookies.set('loginToken', uniqueID);
                          that.props.triggerLogin();
                          close();
                        } else {
                          console.log("ERROR"+statusCode);//Handle error and display
                        }
                    });
              }}>Login</Button>
            </div>
          )}
        </Popup>
      );
  }
}