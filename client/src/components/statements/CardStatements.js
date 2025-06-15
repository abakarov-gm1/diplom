import React from "react";

const SubmissionMethodChart = () => {
    const data = [
        { label: "Лично", value: 46.07, color: "#8b5cf6" },      // фиолетовый
                // сине-зеленый
        { label: "Суперсервис", value: 18.87, color: "#312e81" }, // темно-синий
    ];

    return (
        <div
            style={{
                maxWidth: "98%",
                padding: "10px",
                backgroundColor: "#ffffff",
                borderRadius: "8px",
                boxShadow: "0 2px 8px rgba(0, 0, 0, 0.1)",
                margin: "5px"
            }}
        >
            <h2 style={{ fontSize: "18px", fontWeight: "600", marginBottom: "16px" }}>
                Способ подачи
            </h2>
            <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
                {data.map((item, index) => (
                    <div key={index}>
                        <div
                            style={{
                                display: "flex",
                                justifyContent: "space-between",
                                alignItems: "center",
                                marginBottom: "4px",
                            }}
                        >
                            <span style={{ fontSize: "14px" }}>{item.label}</span>
                            <span style={{ fontSize: "14px" }}>{item.value.toFixed(2)}%</span>
                        </div>
                        <div
                            style={{
                                width: "100%",
                                backgroundColor: "#e5e7eb",
                                borderRadius: "9999px",
                                height: "16px",
                            }}
                        >
                            <div
                                style={{
                                    width: `${item.value}%`,
                                    backgroundColor: item.color,
                                    height: "16px",
                                    borderRadius: "9999px",
                                }}
                            ></div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SubmissionMethodChart;
