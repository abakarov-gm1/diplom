import * as React from "react";
import { BarChart } from "@mui/x-charts/BarChart";

const SubmissionDynamicsChart = ({registerData}) => {

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
                dataset={registerData}
                height={320}
                grid={{ horizontal: true }}
            />
        </div>
    );
};

export default SubmissionDynamicsChart;




