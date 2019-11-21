import React from "react";
import {PieChart, Pie, Cell} from "recharts";

const PIECOLOR = "#8884d8"
const COLORS = ['#0088FE', '#00C49F'];
const TITLES = ["Open", "Closed"];

const RADIAN = Math.PI / 180;
const renderLabel = ({
	cx, cy, midAngle, innerRadius, outerRadius, percent, index,
}) => {
	const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
	const x = cx + radius * Math.cos(-midAngle * RADIAN);
	const y = cy + radius * Math.sin(-midAngle * RADIAN);

	return (
	  <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
	    {TITLES[index]}
	  </text>
	);
};

export default class CustomPieChart extends React.Component {
	constructor(props) {
		super(props);
	}
	render() {
		const {pieData, title} = this.props;
		return (
			<div className="pieDiv">
				<h3>{title}</h3>
				<PieChart width={730} height={250}>
					<Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={90} fill={PIECOLOR} labelLine={false} label={renderLabel}>
						{
					      pieData.map((entry, index) => (
					        <Cell key={`cell-${index}`} fill={COLORS[index]}/>
					      ))
					    }
					</Pie>
				</PieChart>
			</div>
			);
	}
}