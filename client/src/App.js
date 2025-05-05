import logo from './logo.svg';
import './App.css';
import "./components/auth/AuthForm"
import AuthForm from "./components/auth/AuthForm";
import Dashboard from "./components/statements/Dashborad";
import MonitoringIndex from "./components/monitoringStatements";

function App() {
  return (
      // <h1 className="text-2xl font-bold underline text-red-500">
      //     Hello world!
      // </h1>
      // <AuthForm />
<>
      <Dashboard />

      <MonitoringIndex />
</>
  );
}

export default App;
