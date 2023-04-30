import React, { useState } from 'react'
import {MdCloudUpload, MdDelete} from 'react-icons/md';
import { AiFillFileImage } from 'react-icons/ai'
import './Upload.css'
const Upload = () => {

  const [file, setFile] =useState(null)
  const [fileName, setFileName] = useState("No selected file")

  const handleFileChange = ({target: {files}}) => {
    files[0] && setFileName(files[0].name)
    if(files){
      setFile(URL.createObjectURL(files[0]))
    }
  };

  return (
    <main className='d-flex flex-column align-items-center justify-content-center form-upload' >
        <form className='d-flex flex-column align-items-center justify-content-center form-upload'
        onClick={() => document.querySelector('.input-field').click()}
        >
          
          <div className='container-upload d-flex flex-column align-items-center justify-content-center'>
            <input type="file" accept="application/vnd.ms-excel,text/csv,application/csv,text/x-csv" 
            className='input-field' hidden
            onChange={handleFileChange} />

          <div class="d-flex flex-column justify-content-center align-items-center">
            <MdCloudUpload color='#2ca3fa' size={120}/>
            <p class="text-center">Browse files to upload</p>
          </div>
          </div>   
        </form>

        <section>
          <AiFillFileImage color='#2ca3fa'/>
          <span>
            {fileName}
            <MdDelete 
            color='#2ca3fa'
            onClick={() => {
              setFileName("No file selected")
              setFile(null)
            }}/>
          </span>
        </section> 
    </main>
  )
}

export default Upload