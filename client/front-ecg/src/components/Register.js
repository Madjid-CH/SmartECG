import styled from "styled-components";
import { useNavigate, Link } from "react-router-dom";
import Logo from "../Assets/logo.svg";
import React, { useContext, useState } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const Register = () => {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmationPassword, setConfirmationPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const toastOptions = {
    position: "bottom-right",
    autoClose: 8000,
    pauseOnHover: true,
    draggable: true,
    theme: "light",
  };

  const handleValidation = () => {
    if (password !== confirmationPassword) {
      toast.error(
        "Password and confirm password should be same.",
        toastOptions
      );
      return false;
    } else if (password.length < 8) {
      toast.error(
        "Password should be equal or greater than 8 characters.",
        toastOptions
      );
      return false;
    } else if (email === "") {
      toast.error("Email is required.", toastOptions);
      return false;
    }

    return true;
  };

  
  const handleSubmit = (e) => {
    e.preventDefault();
  };

  return (

    <div>
        <FormContainer>
        <form action="" onSubmit={handleSubmit}>

          <Link to="/">
          <div className="brand">
          <img src={Logo} alt="logo" />
            <h1>SmartECG</h1>
          </div>
          </Link>

          <input
            type="email"
            placeholder="Email"
            name="email"
            className="input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Password"
            name="password"
            className="input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Confirm Password"
            name="confirmPassword"
            className="input"
            value={confirmationPassword}
            onChange={(e) => setConfirmationPassword(e.target.value)}
            required
          />

          <button type="submit">Create Account</button>
          <span>
            Already have an account ? <Link to="/login">Login.</Link>
          </span>
        </form>
        </FormContainer>
        <ToastContainer />
    </div>
  )
}

export default Register;
const FormContainer = styled.div`
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1rem;
  align-items: center;
  background-color: #FFFFF;
  .brand {
    display: flex;
    align-items: center;
    gap: 1rem;
    justify-content: center;
    padding:2rem;
    img {
      height: 5rem;
    }
    h1 {
      color: black;
      text-transform: uppercase;
    }
  }
  form {
    Link{
      decoration: none;
    }
    display: flex;
    flex-direction: column;
    gap: 1rem;
    background-color: white;
    border-radius: 2rem;
    padding: 3rem 5.5rem;
  }
  input {
    background-color: transparent;
    padding: 1rem;
    border: 0.1rem solid #2ca3fa;
    border-radius: 0.4rem;
    color: white;
    width: 100%;
    font-size: 1rem;
    &:focus {
      border: 0.1rem solid #997af0;
      outline: none;
    }
  }
  button {
    background-color: #2ca3fa;
    color: white;
    padding: 1rem 2rem;
    border: none;
    font-weight: bold;
    cursor: pointer;
    border-radius: 0.4rem;
    font-size: 1rem;
    text-transform: uppercase;
    &:hover {
      background-color: #4e0eff;
    }
  }
  span {
    margin: 1.5rem;
    color: gris;
    a {
      color: #2ca3fa;
      text-decoration: none;
      font-weight: bold;
    }
  }
`;