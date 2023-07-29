import React, { useState, useEffect } from 'react';

const Depth = () => {
  const [depthData, setDepthData] = useState(null);

  useEffect(() => {
    fetchDepthData();
  }, []);

  const fetchDepthData = async () => {
    try {
      const response = await fetch('https://api.example.com/depth');
      const data = await response.json();
      setDepthData(data);
    } catch (error) {
      console.error('Error fetching depth data:', error);
    }
  };

  return (
    <div>
      <h2>Depth Component</h2>
      {depthData ? (
        <ul>
          {depthData.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      ) : (
        <p>Loading depth data...</p>
      )}
    </div>
  );
};

export default Depth;
