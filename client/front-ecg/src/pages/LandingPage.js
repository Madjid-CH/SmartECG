import React from 'react'
import CustomNavbar from '../components/customNavbar'
import Header from '../components/Header'
import { Container } from 'react-bootstrap'

const LandingPage = () => {
  return (
    <div>
    <Container style={{ background: 'linear-gradient(to top, #00c6ff, #0072ff)'}}>
    <CustomNavbar/>
    <Header/>
    </Container>
    </div>
  )
}

export default LandingPage