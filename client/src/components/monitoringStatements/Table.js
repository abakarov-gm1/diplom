import React, {useState} from "react";
import {
    Box,
    LinearProgress,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Typography,
    Paper,
} from "@mui/material";


export default function ContestTable({
        size=49,
        columns,
        rows,
        setTest
        }) {

    // const [direction, setDirection] = useState()
    //
    // console.log(direction, "DIRECTION")

    return (
        <div style={{width:`${size}%`, margin:"1%"}}>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow sx={{ padding: "8px" }}>
                            {columns?.map((i) => (
                                 <TableCell style={{backgroundColor:"#1e1e2f", color:"white"}}>{i.name}</TableCell>
                            ))}
                        </TableRow>
                    </TableHead>
                    <TableBody padding={"8px"}>
                        {rows.map((row, index) => {

                            return (
                                <TableRow key={index}>
                                    {columns.map((col, colIndex) => (
                                        <TableCell
                                            key={colIndex}
                                            sx={{ padding: "8px" }}
                                            style={{
                                                backgroundColor: colIndex === 0 ? "#1e1e2f" : "rgba(37,40,103,0.72)",
                                                color: "white"
                                            }}
                                            onClick={()=>{setTest(row.code)}}
                                        >
                                            {colIndex === 0 ? (
                                                row.code // первая колонка — без "барчика"
                                            ) : (
                                                <div
                                                    style={{
                                                        width: `${row.percent}%`,
                                                        height: "100%",
                                                        backgroundColor: "#8686b1",
                                                        display: "flex",
                                                        justifyContent: "flex-end",
                                                        borderRadius: "4px"
                                                    }}

                                                >
                                                    {row[col.key]}
                                                </div>
                                            )}
                                        </TableCell>
                                    ))}
                                </TableRow>
                            );
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    );
}
