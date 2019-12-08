import React from "react";

export default class Card extends React.Component {

	constructor(props) {
		super(props);
	}

	render() {
		const {data, header} = this.props;
		return (
			<div className="centerWrapper">
				<h4>{header}</h4>
				<div className="centerWrapper card">
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
			</div>
			);
	}
}