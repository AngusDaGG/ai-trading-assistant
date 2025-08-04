import { useState } from 'react'
import axios from 'axios'
export default function App(){
  const [symbol,setSymbol]=useState('SOL-USDT');
  const [img,setImg]=useState(null);
  const go=async()=>{
    const res=await axios.get('https://ai-trading-assistant-5vws.onrender.com',{params:{symbol,bar:'1H',limit:200}});
    setImg(res.data.image);
  };
  return(
    <div style={{maxWidth:800,margin:'40px auto',textAlign:'center'}}>
      <h3>K-line Viewer</h3>
      <input value={symbol} onChange={e=>setSymbol(e.target.value)}/>
      <button onClick={go}>Fetch</button>
      {img && <img src={img} style={{width:'100%',marginTop:20}} />}
    </div>
  )
}
