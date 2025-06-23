import React from "react";

const SubmissionMethodChart = ({ data }) => {
    // Проверка и преобразование данных
    const chartData = data.reduce((acc, item) => {
        const personalCount = Number(item?.count_not_egpy || 0);
        const serviceCount = Number(item?.count_egpy || 0);

        return [
            ...acc,
            {
                label: "Лично",
                value: personalCount,
                color: "#8b5cf6",
                percent: (personalCount / (personalCount + serviceCount || 1)) * 100
            },
            {
                label: "Суперсервис",
                value: serviceCount,
                color: "#312e81",
                percent: (serviceCount / (personalCount + serviceCount || 1)) * 100
            }
        ];
    }, []);

    // Группируем данные по типу (Лично/Суперсервис)
    const groupedData = chartData.reduce((acc, item) => {
        const existing = acc.find(i => i.label === item.label);
        if (existing) {
            existing.value += item.value;
            existing.percent += item.percent;
        } else {
            acc.push({ ...item });
        }
        return acc;
    }, []);

    // Нормализуем проценты
    const totalPercent = groupedData.reduce((sum, item) => sum + item.percent, 0);
    const normalizedData = groupedData.map(item => ({
        ...item,
        percent: totalPercent > 0 ? (item.percent / totalPercent) * 100 : 50
    }));

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
                {normalizedData.map((item, index) => (
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
                            <span style={{ fontSize: "14px" }}>
                {item.percent.toFixed(2)}%
              </span>
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
                                    width: `${item.percent}%`,
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
