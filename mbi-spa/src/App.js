import React, { useState } from 'react';
import { Button } from 'react-bootstrap';

function App() {

  const [mbi, setMbi] = useState([])
  const [verifyMbi, setVerifyMbi] = useState()
  let textMbiInput = React.createRef()

  function generateMBI(){
    fetch("/generate").then(
      res => res.json()
    ).then(
      mbi => {
        setMbi(mbi)
      }
    )
  }

  function verifyMBI(){
    console.log(textMbiInput.current.value);
    fetch("/verify/"+textMbiInput.current.value).then(
      res => res.json()
    ).then(
      verifyMbi => {
        setVerifyMbi(verifyMbi)
        console.log(verifyMbi)
      }
    )
  }

  return (
  <div className="max-w-7xl mx-auto">
    <><Button variant="primary" onClick={generateMBI}>GENERATE MBI</Button></>
    {(typeof mbi.mbinumber === 'undefined') ? (
      <p></p>
    ) : (
      <h4>MBI: {mbi.mbinumber}</h4>
    )}
    <input ref={textMbiInput} placeholder="Type a MBI..." />
    <Button variant="success" onClick={verifyMBI}>VERIFY MBI</Button>
    {(JSON.stringify(verifyMbi) === 'true') ? (
      <h4>VALID MBI</h4>
    ) : (JSON.stringify(verifyMbi) === 'false') ? (
      <h4>INVALID MBI</h4>
    ) : (
      ''
    )}
  </div>
  )
}

export default App;
