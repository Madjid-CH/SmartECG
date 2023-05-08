import React from "react";
import logo from '../Assets/logo-01.svg';
import { Navbar, Nav ,Container} from 'react-bootstrap';
import styled from "styled-components";

function CustomNavbar() {
 

  return (
  <Navbar expand="md ">
  <Container>
    <Navbar.Brand className="d-flex justify-content-between" href="/">
      <img src={logo} alt="Logo" height="50" className="d-inline-block align-top" />
      <span className="text-light m-2 font-weight-bold">SmartECG</span>
    </Navbar.Brand>
    <Navbar.Toggle aria-controls="navbar-nav" />
    <Navbar.Collapse id="navbar-nav">
      <Nav className="ms-auto">
        <Nav.Link className="text-light m-3" href="/">Home</Nav.Link>
        <Nav.Link className="text-light m-3" href="/predictionsTable">Predictions</Nav.Link>
        <Button className="m-3"><Nav.Link href="/predict">Predict</Nav.Link></Button>
      </Nav>
    </Navbar.Collapse>
  </Container>
</Navbar>
  );
}

const Button = styled.button`
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.1rem;
  border-radius: 0.5rem;
  background-color: white;
  border: none;
  cursor: pointer;
  color: black;
`;
export default CustomNavbar;