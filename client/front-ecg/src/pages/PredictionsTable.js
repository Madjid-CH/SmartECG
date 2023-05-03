import React, { useState } from 'react'
import { Container } from 'react-bootstrap'
import CustomNavbarDark from '../components/customNavbarDark'
import { useLocation } from 'react-router-dom';
import { Table } from 'react-bootstrap';
import styled from "styled-components";

const PredictionsTable = () => {
  const location = useLocation()
  const [results, setResult] = useState(location.state.result);
  const handleViewClick = (index) => {
    console.log(`View button clicked for Patient ${index + 1}`);
  };
  return (
    <Container>
        <CustomNavbarDark/>
        <Table striped bordered hover className='mt-3'>
        <thead>
          <tr>
            <th className="text-center">Patient</th>
            <th className="text-center">Result</th>
            <th className="text-center">ECG</th> 
          </tr>
        </thead>
        <tbody>
          {results.map((result, index) => (
            <tr key={index}>
              <td className="text-center">Patient {index + 1}</td>
              <td className={result === 'Normal' ? 'text-center text-success' : 'text-center text-danger'}>{result}</td>
              <td className="text-center">
                <Button onClick={() => handleViewClick(index)}>View</Button>
              </td>
            </tr>
          ))}
        </tbody>
        </Table>
    </Container>
  )
}
const Button = styled.button`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem;
  border-radius: 0.5rem;
  background-color: #2ca3fa;
  border: none;
  cursor: pointer;
  color: white;
  margin: 0 auto;
  font-size: 1.1rem;
`;

export default PredictionsTable