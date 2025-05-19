import React, {useState} from 'react';
import Header from "./header";
import BasicLabel from "./label";
import StatementInPerson from "./StatementInPerson";
import StatementsCurrent from "./StatementsСurrent";


const MonitoringIndex = () => {
    const [current, setCurrent] = useState()
    const [inPerson, setInPerson] = useState()
    const [statement, setStatement] = useState({code:"", tableName:""})

    const st = (code, tableName) => {
        setStatement({code: code, tableName: tableName})
    }

    console.log(statement)

    // все данные для этой страницы будут идти отсюда
    const rows1 = [
        { id:1, percent:90, code: "38.03.01 - Экономика", places: 36, submitted: 70, enrolled: 253, zac:255, kody: 344 },
        { id:2, percent:50, code: "43.03.02 - Туризм и рыбалка", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
        { id:3, percent:40, code: "43.03.02 - Политология", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
        { id:4, percent:10, code: "43.03.02 - Спорт", places: 32, submitted: 32, enrolled: 224, zac:255, kody: 344  },
    ];

    const rows2 = [
        {id:5, code: "38.03.01 - Экономика", places: 36, submitted: 70, test1:23, test2:43},
        {id:6, code: "43.03.03 - Спорт", places: 32, submitted: 32, test1:23, test2:43},
        {id:7, code: "43.03.04 - История", places: 32, submitted: 32, test1:23, test2:43},
        {id:8, code: "43.03.05 - Менеджмент", places: 32, submitted: 32, test1:23, test2:43},
    ];


    return (
        <div style={{height: "100%"}}>
            <Header/>

            <div style={{display: "flex"}}>
                <BasicLabel label={"Заявление на бюджет"}/>
                <BasicLabel label={"Заявление вне бюджет"}/>
            </div>

            <div style={{display: "flex"}}>
                <StatementsCurrent
                    rows={rows1}
                    statement={statement}
                    title={"ЗА ТЕКУЩИЙ ДЕНЬ"}
                    tableName={"current"}
                    st={st}
                />
                <StatementInPerson
                    rows={rows2}
                    title={"ЗАЯВЛЕНИЯ МЕСТА КОНКУРС ОЧНО"}
                    statement={statement}
                    tableName={"inPerson"}
                    st={st}
                />

            </div>

            <div style={{display: "flex"}}>

                <StatementInPerson
                    rows={rows2}
                    title={"ЗАЯВЛЕНИЯ МЕСТА КОНКУРС ЗАОЧНО"}
                    statement={statement}
                    tableName={"inAbsentia"}
                    st={st}
                />
                <StatementInPerson
                    rows={rows2}
                    title={"ЗАЯВЛЕНИЯ МЕСТА КОНКУРС ОЧНО ЗАОЧНО"}
                    statement={statement}
                    tableName={"inPersonAbsentia"}
                    st={st}
                />
            </div>

        </div>
    );
};

export default MonitoringIndex;
