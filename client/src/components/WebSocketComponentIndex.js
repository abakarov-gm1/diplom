// import React, { useState, useEffect, useRef } from 'react';
//
// const WebSocketComponent = () => {
//     const [messages, setMessages] = useState([]);
//     const [isConnected, setIsConnected] = useState(false);
//     const [chatId, setChatId] = useState(1); // ID чата по умолчанию
//     const [token, setToken] = useState('your_token_here'); // Ваш токен
//     const ws = useRef(null);
//
//     // Функция подключения к WebSocket
//     const connectWebSocket = () => {
//         if (ws.current) {
//             ws.current.close();
//         }
//
//         const socketUrl = `ws://localhost:8000/ws/${chatId}/${token}`;
//         ws.current = new WebSocket(socketUrl);
//
//         ws.current.onopen = () => {
//             console.log('Connected to WebSocket');
//             setIsConnected(true);
//         };
//
//         ws.current.onmessage = (event) => {
//             const message = event.data;
//             console.log('Received message:', message);
//             setMessages(prev => [...prev, message]);
//         };
//
//         ws.current.onclose = () => {
//             console.log('Disconnected from WebSocket');
//             setIsConnected(false);
//         };
//
//         ws.current.onerror = (error) => {
//             console.error('WebSocket error:', error);
//         };
//     };
//
//     // Функция отправки сообщения
//     const sendMessage = () => {
//         if (ws.current && ws.current.readyState === WebSocket.OPEN) {
//             const message = 'Hello from React!';
//             ws.current.send(message);
//             console.log('Message sent:', message);
//         }
//     };
//
//     // Подключаемся при монтировании компонента
//     useEffect(() => {
//         connectWebSocket();
//
//         return () => {
//             if (ws.current) {
//                 ws.current.close();
//             }
//         };
//     }, [chatId, token]); // Переподключаемся при изменении chatId или token
//
//     return (
//         <div>
//             <h2>WebSocket Connection</h2>
//
//             <div>
//                 <label>
//                     Chat ID:
//                     <input
//                         type="number"
//                         value={chatId}
//                         onChange={(e) => setChatId(parseInt(e.target.value))}
//                     />
//                 </label>
//             </div>
//
//             <div>
//                 <label>
//                     Token:
//                     <input
//                         type="text"
//                         value={token}
//                         onChange={(e) => setToken(e.target.value)}
//                     />
//                 </label>
//             </div>
//
//             <button onClick={connectWebSocket} disabled={isConnected}>
//                 {isConnected ? 'Connected' : 'Connect'}
//             </button>
//
//             <button onClick={sendMessage} disabled={!isConnected}>
//                 Send Message
//             </button>
//
//             <h3>Connection Status: {isConnected ? 'Connected' : 'Disconnected'}</h3>
//
//             <h3>Received Messages:</h3>
//             <ul>
//                 {messages.map((msg, index) => (
//                     <li key={index}>{msg}</li>
//                 ))}
//             </ul>
//         </div>
//     );
// };
//
// export default WebSocketComponent;