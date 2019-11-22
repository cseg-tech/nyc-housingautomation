import React from "react";

export default class CustomPercentageTable extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		const {data, title} = this.props;
		return (
			<div className="pieDiv">
				<h3>{title}</h3>
				<div className="wrapBar">
					<div className="progressBar" style={{ width: `${data["new"]}%` }} />
				</div>
				<div className="wrapBar">
					<div className="progressBar" style={{ width: `${data["open"]}%` }} />
				</div>
				<div className="wrapBar">
					<div className="progressBar" style={{ width: `${data["closed"]}%` }} />
				</div>
			</div>
			);
	}
}