import axios from 'axios';
import React from 'react';
import {useState} from 'react';
import './fr1.css'

export const UploadPage = () => {
  const [text, setText] = useState('Учитель');
  const [salary, setsalary] = useState(100000);


  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/vacancys_post', { text });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form className='designe_number_two' onSubmit={handleSubmit}>
      <p className='disigne'><b>Название вакансии</b></p><p className='Zp'><b>Зарплата</b></p>
      <div className='block'>
      <input type="text" value={text} onChange={(e) => setText(e.target.value)} />
      <input type="number" value={salary} onChange={(e) => setsalary(Number(e.target.value))} />
      </div>
      <button className='butt' type="submit">Загрузка вакансий</button>
    </form>
  );
};

