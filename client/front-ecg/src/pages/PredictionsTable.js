import React, { useState } from 'react'
import { Container } from 'react-bootstrap'
import CustomNavbarDark from '../components/customNavbarDark'
import { useLocation } from 'react-router-dom';

const PredictionsTable = () => {
  const location = useLocation()
  const [result, setResult] = useState(location.state.result);
  return (
    <Container>
        <CustomNavbarDark/>
        {result}
    </Container>
  )
}

export default PredictionsTable