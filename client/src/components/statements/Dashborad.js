import React, {useEffect, useRef, useState} from "react";
import { Card } from "./Card";
import ReactVirtualizedTable from "./Tables"
import SubmissionMethodChart from "./CardStatements";
import SubmissionDynamicsChart from "./charts";
const Dashboard = () => {

    const [tableData, setTableData] = useState([]);
    const [registerData, setRegisterData] = useState([]);
    const [isConnected, setIsConnected] = useState(false);
    const ws = useRef(null);

    useEffect(() => {
        // const socketUrl = `ws://localhost:8000/ws/1/your_token_here`;
        const socketUrl = `ws://92.255.79.234:8001/ws/1/your_token_here`;
        ws.current = new WebSocket(socketUrl);

        ws.current.onopen = () => {
            console.log('WebSocket connected');
            setIsConnected(true);
        };

        ws.current.onmessage = (event) => {
            try {
                const message = JSON.parse(event.data);
                console.log('Received:', message);
                setTableData(message?.table_data);
                setRegisterData(message?.registration_data)

            } catch (e) {
                console.error('Error parsing message:', e);
            }
        };

        ws.current.onclose = () => {
            console.log('WebSocket disconnected');
            setIsConnected(false);
        };

        ws.current.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        return () => {
            if (ws.current) {
                ws.current.close();
            }
        };
    }, []);

    const countByDate = registerData.reduce((acc, item) => {
        const date = item.registration_data;
        acc[date] = (acc[date] || 0) + 1;
        return acc;
    }, {});

    const result = Object.entries(countByDate).map(([date, value]) => ({
        date,
        value
    }));


    result.sort((a, b) => new Date(a.date) - new Date(b.date));

    console.log(tableData)
    console.log(result, "RESSSSSSSSS");

    return (
        <div>
            <div style={{display:"flex"}}>

                {/* Left statements */}
                <div style={{width:"35%"}}>
                    <div style={{display: "flex", margin: "6px"}}>
                        <div style={{width: "50%"}}>
                            <Card title="Всего абитуриентов" value={tableData[0]?.all_count_entrant}></Card>
                        </div>
                        <div style={{width: "50%"}}>
                            <Card title="РФ" value={tableData[0]?.all_count_russian} size="sm"></Card>
                            <Card title="Иностранные" value={tableData[0]?.all_count_english} size="sm"></Card>
                        </div>

                    </div>
                    <div style={{marginTop:"18px"}}>
                        <ReactVirtualizedTable competitionGroup={tableData}/>
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
                        <Card value={tableData[tableData.length - 1]?.all_number_places} w="l"/>
                        <Card value={tableData[tableData.length - 1]?.all_applications} title='подано' w="l"/>
                        <Card value={tableData[tableData.length - 1]?.all_status_refusal} title='отозвано' w="l"/>
                        <Card value={tableData[tableData.length - 1]?.all_status_enrolled} w="l"/>
                    </div>

                    <div style={{height: "30%", display: "flex", justifyContent:"center", marginTop:"10px"}}>
                        <div style={{width: "100%"}}>
                            <SubmissionMethodChart data={tableData}/>
                        </div>
                        {/*<div style={{width: "25%"}}>*/}
                        {/*    <SubmissionMethodChart/>*/}
                        {/*</div>*/}
                        {/*<div style={{width: "25%"}}>*/}
                        {/*    <SubmissionMethodChart/>*/}
                        {/*</div>*/}
                        {/*<div style={{width: "25%"}}>*/}
                        {/*    <SubmissionMethodChart/>*/}
                        {/*</div>*/}
                    </div>

                    <div style={{height:"35%"}}>
                        <SubmissionDynamicsChart registerData={result} />
                    </div>

                </div>

            </div>
        </div>
    );
};

export default Dashboard;





