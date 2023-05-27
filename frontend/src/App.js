import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SplashScreen from '.\splashscreen.js';
import MainPage from '.\MainPage.js';
const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={SplashScreen} />
        <Route path="/main" component={MainPage} />
      </Switch>
    </Router>
  );
};

export default App;
