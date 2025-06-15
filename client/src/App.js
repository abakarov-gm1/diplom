import logo from './logo.svg';
import './App.css';
import "./components/auth/AuthForm"
import AuthForm from "./components/auth/AuthForm";
import Dashboard from "./components/statements/Dashborad";
import MonitoringIndex from "./components/monitoringStatements";

function App() {
  return (
<>
      <Dashboard />
      <MonitoringIndex />
</>
  );
}

export default App;
