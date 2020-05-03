import React from "react";

export default class CustomPercentageTable extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		const {data, title} = this.props;
		return (
			<div className="pieDiv" bg="light">
				<h3>{title}</h3>
				<div className = "pTable">
				<h4>Administrative</h4>
				<div className="wrapBar">
					<div className="progressBarA" style={{ width: `${data["new"]}%` }} />
				</div>
				<h4>Environmental</h4>
				<div className="wrapBar">
					<div className="progressBarE" style={{ width: `${data["open"]}%` }} />
				</div>
				<h4>Safety</h4>
				<div className="wrapBar">
					<div className="progressBarS" style={{ width: `${data["closed"]}%` }} />
				</div>
				</div>
			</div>
			);
	}
}