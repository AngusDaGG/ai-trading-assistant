
import { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [symbol, setSymbol] = useState('SOL-USDT');
  const [img, setImg] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchChart = async () => {
    setLoading(true);
    try {
      const res = await axios.get('http://localhost:8000/chart', {
        params: { symbol, bar: '1H', limit: 200 }
      });
      setImg(res.data.image);
    } catch (err) {
      alert('API error, check console');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{maxWidth:800, margin:'40px auto', textAlign:'center'}}>
      <h2>AI Trading Assistant – Kline Viewer</h2>
      <input value={symbol} onChange={e=>setSymbol(e.target.value)} style={{padding:8}}/>
      <button onClick={fetchChart} style={{marginLeft:10, padding:'8px 16px'}}>Fetch</button>
      {loading && <p>loading…</p>}
      {img && <img src={img} alt="kline" style={{width:'100%', marginTop:20}}/>}
    </div>
  )
}
