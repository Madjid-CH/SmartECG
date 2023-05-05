import React from 'react'
import { Container, Row, Col, Nav } from "react-bootstrap";
import illHero from '../Assets/header-01.svg'
import styled from "styled-components";

const Header = () => {
  return (
    <div>
        <Row>
        <Col md={{ span: 6, offset: 0 }} lg={{ span: 4, offset: 1 }}>
          <h1 className='mt-5 text-light font-weight-bold'>Stay healthy with smart ECG</h1>
          <p className='text-light font-weight-light mb-6'>Stay healthy with us, by reguraly verifying your heart rate using ecg deep learning app that predicts if your ECG is normal or abnomarl, What are you waiting to try it out?</p>
          <Nav.Link href="/predict"><Button className="mt-5 p-3 h5">Make predictions</Button></Nav.Link>
        </Col>
        <Col md={{ span: 6, offset: 0}} lg={{ span: 5, offset: 1}}>
          <img src={illHero} style={{height: "30rem"}} alt="header illustration"/>
        </Col>
        </Row>
    </div>
  )
}

export default Header
const Button = styled.button`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.1rem;
  border-radius: 0.5rem;
  background-color: #FF706A;
  border: none;
  cursor: pointer;
  color: white;
`;