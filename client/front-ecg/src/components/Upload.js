import React, { useState } from 'react'
import {MdCloudUpload, MdDelete} from 'react-icons/md';
import { AiFillFileImage } from 'react-icons/ai'
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import './Upload.css'

const Upload = () => {
  const [file, setFile] = useState(null)
  const [fileName, setFileName] = useState("No selected file")
  const [result, setResult] = useState(null);
  const navigate = useNavigate(); 

  const handleFileChange = ({target: {files}}) => {
    files[0] && setFileName(files[0].name)
    if(files){
      setFile(URL.createObjectURL(files[0]))
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    try {
      const response = await axios.post("http://127.0.0.1:8000/predict", formData, {
        headers: {
          Accept: "application/json",
          "Content-Type": "multipart/form-data",
        },
      });
      console.log(response.data.Labels)
      setResult(response.data.Labels)
      navigate('/predictionsTable', { state: { result: response.data.Labels} });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <main className='d-flex flex-column align-items-center justify-content-center form-upload' >
        <form onSubmit={handleSubmit} className='d-flex flex-column align-items-center justify-content-center form-upload'>
          <div onClick={() => document.querySelector('.input-field').click()}>
          <div className='container-upload d-flex flex-column align-items-center justify-content-center'>
            <input 
            type="file"
            accept="application/vnd.ms-excel,text/csv,application/csv,text/x-csv"
            className="input-field"
            hidden
            name="file"
            onChange={handleFileChange} />

          <div className="d-flex flex-column justify-content-center align-items-center">
            <MdCloudUpload color='#2ca3fa' size={120}/>
            <p className="text-center">Browse files to upload</p>
          </div>
          </div>   
          </div>
          <button className="mt-2 p-3 h5" style={{backgroundColor: "#2ca3fa", border: "none", borderRadius:"10px", color:"white",width: "32em"}} type="submit">Predict</button>
        </form>
        
        <section>
          <AiFillFileImage color='#2ca3fa' className='m-3'/>
          <span style={{fontSize:"1em" }}>
            {fileName}
            <MdDelete 
            color='#2ca3fa'
            onClick={() => {
              setFileName("No file selected")
              setFile(null)
            }}
            className='m-3'/>
          </span>
        </section> 
    </main>
  )
}

export default Upload