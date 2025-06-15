import logo from './logo.svg';
import './App.css';
import "./components/auth/AuthForm"
import AuthForm from "./components/auth/AuthForm";
import Dashboard from "./components/statements/Dashborad";
import MonitoringIndex from "./components/monitoringStatements";
import WebSocketComponent from "./components/WebSocketComponentIndex";

function App() {
  return (
<>
      <Dashboard />
      {/*<MonitoringIndex />*/}
    {/*<WebSocketComponent />*/}
</>
  );
}

export default App;
