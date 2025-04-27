import * as React from "react";
import { BarChart } from "@mui/x-charts/BarChart";

const SubmissionDynamicsChart = () => {
    const data = [
        { date: "2022-07-1", value: 196 },
        { date: "2022-07-2", value: 351 },
        { date: "2022-07-3", value: 352 },
        { date: "2022-07-4", value: 30 },
        { date: "2022-07-5", value: 166 },
        { date: "2022-07-6", value: 8 },
        { date: "2022-07-9", value: 803 },
        { date: "2022-07-10", value: 70 },
        { date: "2022-07-11", value: 31 },
        { date: "2022-07-13", value: 33 },
        { date: "2022-07-15", value: 39 },
        { date: "2022-07-16", value: 15 },
        { date: "2022-07-17", value: 41 },
        { date: "2022-07-18", value: 1 },
        { date: "2022-07-19", value: 57 },
        { date: "2022-07-23", value: 661 },
        { date: "2022-07-24", value: 21 },
        { date: "2022-07-25", value: 17 },
        { date: "2022-07-26", value: 25 },
        { date: "2022-07-29", value: 52 },
        { date: "2022-07-31", value: 33 },
    ];

    return (
        <div style={{ width: "100%", marginTop:"15px" }}>
            <h3>Динамика подачи заявлений</h3>
            <BarChart
                xAxis={[
                    {
                        dataKey: "date",
                        scaleType: "band",
                        label: "Дата",
                    },
                ]}
                series={[
                    {
                        dataKey: "value",

                        color: "#00bfff",
                    },
                ]}
                dataset={data}
                height={320}
                grid={{ horizontal: true }}
            />
        </div>
    );
};

export default SubmissionDynamicsChart;




