import React from 'react';
import CardComponent from "./Card";


const Header = () => {
    return (
        <div style={{
            display:"flex",
            justifyContent:"space-around",
            height:"10%"
        }}>
            <CardComponent title={"Абитуриенты"} count={1467} percent={15} pData={[2400, 1398, 1900, 3908, 1900]} />
            <CardComponent title={"КПЦ"} count={24} percent={16} pData={[2400, 1398, 1900, 3908, 6900]}/>
            <CardComponent title={"Подано"} count={345} percent={266} pData={[2400, 1398, 1900, 3908, 4000]}/>
            <CardComponent title={"Конкурс"} count={35} percent={13} pData={[2400, 1398, 1900, 3908, 1900]}/>
            {/*<CardComponent title={"ЕГЭ"} count={23} percent={0.01} pData={[2400, 1398, 1900, 3908, 7900]}/>*/}
        </div>
    );
};

export default Header;




