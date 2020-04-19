import React from "react";
import { Navbar, Nav } from "react-bootstrap";

export default function Header(props) {
    return (
        <Navbar bg="light" variant="light" style={{paddingTop: "1vh", paddingBottom: "1vh", paddingRight: "0.5vw", paddingLeft: "0.5vw", height: "8vh"}}>
            <Navbar.Brand style={{marginLeft: "2vw"}}>{props.number+" complaints at " +props.address}</Navbar.Brand>
                    <Nav className="ml-auto" style={{marginRight: "2vw"}}>
                    <Nav.Link onClick={() => {
                        console.log("Popup to edit notifications")
                    }}>Edit Notifications</Nav.Link>
                    <Nav.Link href="https://portal.311.nyc.gov/">311 Portal</Nav.Link>
                    <Nav.Link onClick={() => {
                        console.log("Popup to edit address")
                    }}>Change Building</Nav.Link>
                    <Nav.Link onClick={props.logout}>Logout</Nav.Link>
                </Nav>
        </Navbar>
    );
}