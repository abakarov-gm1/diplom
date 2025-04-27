import React from "react";
import { Card } from "./Card";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
// import StickyHeadTable from "../components/Tables"
import ReactVirtualizedTable from "./Tables"
import SubmissionMethodChart from "./CardStatements";
import SubmissionDynamicsChart from "./charts";
const Dashboard = () => {
    return (
        <div>
            <div style={{display:"flex"}}>

                {/* Left statements */}
                <div style={{width:"35%"}}>
                    <div style={{display: "flex", margin: "6px"}}>
                        <div style={{width: "50%"}}>
                            <Card title="Всего абитуриентов" value="5922"></Card>
                        </div>
                        <div style={{width: "50%"}}>
                            <Card title="РФ" value="2902" size="sm"></Card>
                            <Card title="Иностранные" value="1444" size="sm"></Card>
                        </div>

                    </div>
                    <div style={{marginTop:"18px"}}>
                        <ReactVirtualizedTable/>
                    </div>
                </div>

                {/* Right statements */}
                <div style={{width: "65%"}}>

                    <div style={{height:"5%", display:"flex"}}> {/* Header */}
                        <div style={{display:"flex", width:"25%", justifyContent:"center", alignItems:"center"}}>
                            КПЦ
                        </div>
                        <div style={{display:"flex", width:"50%", justifyContent:"center", alignItems:"center"}}>
                            ЗАЯВЛЕНИЯ
                        </div>
                        <div style={{display:"flex", width:"25%", justifyContent:"center", alignItems:"center"}}>
                            ЗАЧИСЛЕННО
                        </div>
                    </div>

                    <div style={{display:"flex", height:"15%"}}>
                        <Card value="302" w="l"/>
                        <Card value="42322" title='подано' w="l"/>
                        <Card value="402" title='отозвано' w="l"/>
                        <Card value="26" w="l"/>
                    </div>

                    <div style={{height: "30%", display: "flex", justifyContent:"center", marginTop:"10px"}}>
                        <div style={{width: "25%"}}>
                            <SubmissionMethodChart/>
                        </div>
                        <div style={{width: "25%"}}>
                            <SubmissionMethodChart/>
                        </div>
                        <div style={{width: "25%"}}>
                            <SubmissionMethodChart/>
                        </div>
                        <div style={{width: "25%"}}>
                            <SubmissionMethodChart/>
                        </div>
                    </div>

                    <div style={{height:"35%"}}>
                        <SubmissionDynamicsChart />
                    </div>

                </div>

            </div>
        </div>
    );
};

export default Dashboard;





