import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';

const SplashScreen = () => {
  const history = useHistory();

  useEffect(() => {
    // Simulate loading or any other tasks you want to perform
    const timer = setTimeout(() => {
      history.push('/main');
    }, 2000);

    // Clean up the timer when the component unmounts
    return () => clearTimeout(timer);
  }, [history]);

  return (
    <div>
      <h1>Splash Screen</h1>
      <p>Loading...</p>
    </div>
  );
};

export default SplashScreen;
