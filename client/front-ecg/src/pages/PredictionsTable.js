import React, { useState } from 'react'
import { Container, Modal } from 'react-bootstrap'
import CustomNavbarDark from '../components/customNavbarDark'
import { useLocation } from 'react-router-dom';
import { Table } from 'react-bootstrap';
import styled from "styled-components";

const PredictionsTable = () => {
  const location = useLocation()
  const [results, setResult] = useState(location.state ? location.state.result : []);
  const [showModal, setShowModal] = useState(false);
  const [selectedImage, setSelectedImage] = useState('');
  const [selectedPatientIndex, setSelectedPatientIndex] = useState(null);
  const handleViewClick = (index) => {
    setSelectedImage(`http://localhost:8000/plot/${index}`);
    setSelectedPatientIndex(index+1);
    setShowModal(true);
  };
  const handleCloseModal = () => {
    setShowModal(false);
    setSelectedImage('');
    setSelectedPatientIndex(null);
  };

  return (
    <Container>
      <CustomNavbarDark />
      {results.length > 0 ? (
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
      ) : (
        <p style={{ textAlign: 'center' }}>No predictions yet.</p>
      )}
      <Modal show={showModal} onHide={handleCloseModal} centered>
        <Modal.Header closeButton>
          <Modal.Title>Patient {selectedPatientIndex} ECG</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <img src={selectedImage} alt="ECG" style={{ maxWidth: '100%', display: 'block', margin: '0 auto' }} />
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={handleCloseModal}>Close</Button>
        </Modal.Footer>
      </Modal>
    </Container>
  );  
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