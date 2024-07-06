import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import {UploadPage} from './fr1';
import {FilterPage} from './fr2';
import './App.css'


 export const App = () => {
  return (
    <Router>
      <nav>
        <Link to="/home_page">Главная</Link> | <Link to="/upld_page">Загрузка вакансий</Link> | <Link to="/fltr_page">Фильтр по вакансиям</Link>
      </nav>
      <Routes>
        <Route path="/home_page" element={<HomePage />} />
        <Route path="/upld_page" element={<UploadPage />} />
        <Route path="/fltr_page" element={<FilterPage />} />
      </Routes>
    </Router>
  );
};


const HomePage = () => {
  return <div className='mn_hdr'>Добро пожаловать на главную страницу!</div>;
};

export default App;