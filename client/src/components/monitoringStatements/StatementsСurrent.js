import React from 'react';
import {
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow
} from "@mui/material";

const StatementsCurrent = ({ rows, st, statement, tableName, title }) => {

    return (
        <div style={{ width: "50%", margin: "1%" }}>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{padding: "3px"}}> {title} </TableCell>
                        </TableRow>
                        <TableRow>
                            <TableCell style={{ backgroundColor: "#1e1e2f", color: "white" }}>Специальность</TableCell>
                            <TableCell style={{ backgroundColor: "#1e1e2f", color: "white" }}>Абитуриенты</TableCell>
                            <TableCell style={{ backgroundColor: "#1e1e2f", color: "white" }}>Подано</TableCell>
                            <TableCell style={{ backgroundColor: "#1e1e2f", color: "white" }}>Отозвано</TableCell>
                            <TableCell style={{ backgroundColor: "#1e1e2f", color: "white" }}>Зачислено</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {rows.map((row) => (
                            <TableRow key={row.id}>
                                <TableCell
                                    sx={{ padding: "8px" }}
                                    style={{
                                        backgroundColor: "#1e1e2f",
                                        color: "white"
                                    }}
                                    onClick={() => statement.code === row.code ? st(0,"") : st(row.code, tableName )}
                                >
                                    {row.code}
                                </TableCell>
                                <TableCell
                                    sx={{ padding: "8px" }}
                                    style={{
                                        backgroundColor: "rgba(37,40,103,0.72)",
                                        color: "white",
                                        textAlign: "right"
                                    }}
                                >
                                    {row.places}
                                </TableCell>
                                <TableCell
                                    sx={{ padding: "8px" }}
                                    style={{
                                        backgroundColor: "rgba(37,40,103,0.72)",
                                        color: "white",
                                        textAlign: "right"
                                    }}
                                >
                                    {row.submitted}
                                </TableCell>
                                <TableCell
                                    sx={{ padding: "8px" }}
                                    style={{
                                        backgroundColor: "rgba(37,40,103,0.72)",
                                        color: "white",
                                        textAlign: "right"
                                    }}
                                >
                                    {row.zac}
                                </TableCell>
                                <TableCell
                                    sx={{ padding: "8px" }}
                                    style={{
                                        backgroundColor: "rgba(37,40,103,0.72)",
                                        color: "white",
                                        textAlign: "right"
                                    }}
                                >
                                    {row.enrolled}
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    );
};

export default StatementsCurrent;
