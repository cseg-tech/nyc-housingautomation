import React from "react";
import { Button, Form } from "react-bootstrap";


export default class SignUp extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: "",
            password: "",
            buildingno:0,
            street:"",
            borough:""
        }
        this.setEmail = this.setEmail.bind(this);
        this.setPassword = this.setPassword.bind(this);
        this.validateForm = this.validateForm.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleSubmit() {
      let {email, password, buildingno, street, borough} = this.state;
      let payload = {
          email,
          password,
          building: buildingno,
          street,
          borough
      };

      fetch('http://localhost:5000/loginUser', {method: 'post', body:JSON.stringify(payload)})
        .then(function(response) {return response.json();})
        .then(function(data) {
            console.log(data);
            status = data['status']
            valid = data['valid']
            if(!valid) {
                console.log(status)
                //Handle invalid here
            } else {
                this.props.backHome();
                console.log("ERROR"+statusCode);//Handle error and display
            }
        });
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

    render () {
        return(
            <div className="SignUp" style={{marginLeft:"10vw", marginRight:"10vw"}}>
                <Form.Group controlId="email" >
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                    autoFocus
                    type="email"
                    value={this.state.email}
                    onChange={e => this.setEmail(e.target.value)}
                    />
                </Form.Group>
                <Form.Group controlId="password" >
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                    value={this.state.password}
                    onChange={e => this.setPassword(e.target.value)}
                    type="password"
                    />
                </Form.Group>
                <Form.Group controlId="number" >
                    <Form.Label>Building Number</Form.Label>
                    <Form.Control
                    value={this.state.buildingno}
                    onChange={e => this.setState({buildingno: e.target.value})}
                    type="number"
                    />
                </Form.Group>
                <Form.Group controlId="street" >
                    <Form.Label>Street</Form.Label>
                    <Form.Control
                    value={this.state.street}
                    onChange={e => this.setState({street: e.target.value})}
                    type="text"
                    />
                </Form.Group>
                <Form.Group controlId="exampleForm.ControlSelect1">
                    <Form.Label>Example select</Form.Label>
                    <Form.Control as="select"
                    onChange={e => this.setState({borough: e.target.value})}>
                    <option>Manhattan</option>
                    <option>Brooklyn</option>
                    <option>Bronx</option>
                    <option>Queens</option>
                    </Form.Control>
                </Form.Group>
                <Button disabled={!this.validateForm} onClick={this.handleSubmit}>Login</Button>
                <Button onClick={this.props.back}>Back</Button>
            </div>
          );
    }
}