import React from 'react';

export const Card = ({ title, value, size = "md", w = null }) => {
    const sizeHeight = {
        sm: "48%",
        md: "100%",
    };

    const sizeWith = {
        l: "25%",
        xl: "50%",
        xxl: "100%",

    };

    return (
        <div style={{
            // border:"solid 1px #000000ad",
            height:sizeHeight[size],
            display:"flex",
            justifyContent:"center",
            alignItems:"center",
            flexDirection:"column",
            margin: "5px",
            width: sizeWith[w],
            backgroundColor: "#ffffff",
            borderRadius: "8px",
            boxShadow: "0 2px 8px rgba(0 4 8 / 19%)",
        }}>
            <div className="text-gray-500 text-sm mb-1">{title}</div>
            <div className="text-3xl font-semibold text-gray-900">{value}</div>
        </div>
    );
};
