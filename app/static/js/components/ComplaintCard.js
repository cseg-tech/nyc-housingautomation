import React from "react";
import {Card} from 'react-bootstrap'

export default class ComplaintCard extends React.Component {

	constructor(props) {
		super(props);
	}

	render() {
		const {data, header} = this.props;
		return (
			<Card bg="light" style={{textAlign: "center"}}>
			  <Card.Body>
			    <Card.Title>{header}</Card.Title>
			    	<div className="comp">
					{
		                data.map((complaint) => (
		                	<React.Fragment>
		                	<p>Date Created: {complaint.Date_Created}</p>
		                	<p>Description: {complaint.Description}</p>
		                	<p>Last Update: {complaint.Updated_On}</p>
		                	<hr />
		                	</React.Fragment>
		                ))
		              }
					</div>
			  </Card.Body>
			</Card>
			);
	}
}