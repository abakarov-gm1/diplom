import React from 'react';
import { Card, CardContent, Typography } from "@mui/material";
import { ChartContainer } from '@mui/x-charts/ChartContainer';
import {
    LinePlot,
    MarkPlot,
    lineElementClasses,
    markElementClasses,
} from '@mui/x-charts/LineChart';

const pData = [2400, 1398, 1900, 3908, 5900];
const xLabels = [
    'Page A',
    'Page B',
    'Page C',
    'Page D',
    'Page E',
];



const CardComponent = ({title, count, pData}) => {

    const last = pData[pData.length - 1];
    const prev = pData[pData.length - 2];
    const percentChange = ((last - prev) / prev) * 100;

    const direction = percentChange > 0 ? '↑' : percentChange < 0 ? '↓' : '';
    const display = `${direction} ${Math.abs(percentChange).toFixed(2)}%`;

    return (
        <Card sx={{ bgcolor: '#1e1e2f', color: 'white', width: "100%", margin:"5px", display:"flex" }}>
            <CardContent>
                <Typography variant="subtitle2" color="gray">{title}</Typography>
                <Typography variant="h4">{count}</Typography>
                <Typography variant="body2" color={ percentChange >= 0 ? "yellow" : "error"} >
                    {display}
                </Typography>
            </CardContent>

            <ChartContainer
                width={200}
                height={100}
                series={[{ type: 'line', data: pData }]}
                xAxis={[{ scaleType: 'point', data: xLabels, position: 'none' }]}
                yAxis={[{ position: 'none' }]}
                sx={{
                    [`& .${lineElementClasses.root}`]: {
                        stroke: '#a90d00',
                        strokeWidth: 2,
                    },
                    [`& .${markElementClasses.root}`]: {
                        stroke: '#3fab22',
                        r: 4, // Modify the circle radius
                        fill: '#3fab22',
                        strokeWidth: 2,
                    },
                }}
                disableAxisListener
            >
                <LinePlot />
                <MarkPlot />
            </ChartContainer>

        </Card>
    );
};

export default CardComponent;
