import './App.css';
import { useState,useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from "./pages/LandingPage"
import Register from './components/Register';
import Predict from "./pages/predict"
import PredictionsTable from "./pages/PredictionsTable"

function App() {
  return (
    <Router>
    <Routes>
    <Route path="/" element={<LandingPage/>} />
    <Route path="register" element={<Register/>}/>
    <Route path="predict" element={<Predict/>}/>
    <Route path="predictionsTable" element={<PredictionsTable/>}/>
    </Routes>
  </Router>
  );
}

export default App;
