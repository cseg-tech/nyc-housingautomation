import React from "react";
import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from "recharts";

export default class CustomBarChart extends React.Component {
    constructor(props){
        super(props);
    }
    render() {
        const {data} = this.props;
        return (
            <div className="pieDiv">
                <BarChart width={500} height={250} data={data}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#c4c0c0"/>
                    <XAxis dataKey="Complaints" label={{ value: "Complaint type"}}/>
                    <YAxis label={{ value: "Break up", angle: -90, position: 'insideLeft' }}/>
                    <Tooltip/>
                    <Legend/>
                    <Bar dataKey="environmental" fill="#77DD77" />
                    <Bar dataKey="administrative" fill="#779ECB" />
                    <Bar dataKey="safety" fill="#FE6B64" />
                </BarChart>
            </div>
        );
    }
}