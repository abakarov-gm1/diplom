import React, {useState} from 'react';
import Header from "./header";
import BasicLabel from "./label";
import ContestTable from "./Table";

const MonitoringIndex = () => {
    const [test1, setTest1] = useState()
    const [test2, setTest2] = useState()

    // все данные для этой страницы будут идти отсюда
    const rows1 = [
        { percent:90, code: "38.03.01 - Экономика", places: 36, submitted: 70, enrolled: 253, zac:255, kody: 344 },
        { percent:50, code: "43.03.02 - Туризм и рыбалка", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
        { percent:40, code: "43.03.02 - Политология", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
        { percent:10, code: "43.03.02 - Спорт", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
    ];
    const columns1 = [
        {name:"ЗА ТЕКУЩИЙ ДЕНЬ", key:"code"},
        {name:"Абитуриенты", key:"places"},
        {name:"Подано", key:"submitted"},
        {name:"Отозванно", key:"enrolled"},
        {name:"Зачисл", key:"zac"},
    ]

    const rows2 = [
        { code: "38.03.01 - Экономика", places: 36, submitted: 70},
        { code: "43.03.02 - Туризм", places: 32, submitted: 32},
        { code: "43.03.02 - Туризм", places: 32, submitted: 32},
        { code: "43.03.02 - Туризм", places: 32, submitted: 32},
    ];

    let columns2 = [
        {name:"ЗАЯВЛЕНИЯ НА МЕСТА ОЧНАЯ", key:"code"},
        {name:"КПЦ", key:"places"},
        {name:"Абакаров", key:"submitted"}
    ]


    return (
        <div style={{height: "100%"}}>
            <Header/>

            <div style={{display: "flex"}}>
                <BasicLabel label={"Заявление на бюджет"}/>
                <BasicLabel label={"Заявление вне бюджет"}/>
            </div>

            <div style={{display: "flex"}}>
                <ContestTable
                    columns={columns1}
                    rows={rows1}
                />
                <ContestTable
                    columns={columns2}
                    rows={rows2}
                />
            </div>

            <div style={{display: "flex"}}>
                {/*<ContestTable/>*/}
                {/*<ContestTable/>*/}
            </div>

        </div>
    );
};

export default MonitoringIndex;
