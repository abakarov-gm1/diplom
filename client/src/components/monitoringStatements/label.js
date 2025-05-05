import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

export default function BasicLabel({label}) {
    return (
         <div style={{width:"50%"}}>
            <BarChart
                height={300}
                xAxis={[
                    {
                        data: [
                            'Бакалавриат',
                            'Магистр',
                            'Специалитет',
                            'СПО',
                            'СОО',
                            'Аспирантура',
                            'Орденатура'
                        ],
                        scaleType: 'band', // <--- ОБЯЗАТЕЛЬНО!
                    },
                ]}
                yAxis={[{ width: 50 }]}
                series={[
                    {
                        data: [2400, 1398, 9800, 1440, 1455, 4224, 6543, 1222],
                        label: label,
                    },
                ]}

            />
         </div>

    );
}
