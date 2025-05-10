import { ChangeEventHandler } from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import axios from 'axios';
import './fr2.css'

interface Vacancie {
  vacancys_id: number;
  company_name: string;
  url: string;
  experience: string;
  salary: string;
  name: string;
  snippet_requirement: string;
  snippet_responsibility: string;
  vacancys_type: string;
  professional_roles: string;
}

export const FilterPage = () => {
  const [vacancys, setVacancys] = useState<Vacancie[]>([]);

  useEffect(() => {
    const fetchVacancys = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/vacancys_filter');
        setVacancys(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchVacancys();
  }, []);



const [filter, setFilter] = useState ('')

const handleChange:ChangeEventHandler<HTMLInputElement> = (event) => {setFilter(event.target.value)} 

    return (
      <div>
        <p className='kol_vac'><b>Количество найденных вакансии: {vacancys.length}</b></p>
        <p className='flt_vac'>Фильтр по названию вакансии   <input type="text" value={filter} onChange={handleChange}></input></p>
        {vacancys.filter((key) => filter !== '' ? key.name.toLowerCase().includes(filter.toLowerCase()) :  1).map((vacancie) => (
          <div key={vacancie.vacancys_id}>
            <h3>{vacancie.name}</h3>
            <p>Название компании: {vacancie.company_name}</p>
            <p>Тип вакансии: {vacancie.vacancys_type}</p>
            <p>Зарплата: {vacancie.salary.replace("'from'", ' От ').replace("'to'", ' До ').replace("'currency'", ' Валюта ').replace("'gross': False", '').replace("'RUR'", 'Руб').replace('{', '').replace('}', '').replace('None', 'Не обозначено').replace('BYR', 'Бел.руб').replace('BR', 'Бел.руб').replace("'gross': True", '').replace('KZT', 'Тенге')}</p>
            <p>Должность: {vacancie.professional_roles}</p>
            <p>Опыт работы: {vacancie.experience}</p>
            Ссылка на вакансию: <a  href={vacancie.url}>{vacancie.url}</a>
            <p>Требования: {vacancie.snippet_requirement}</p>
            <p>О вакансии: {vacancie.snippet_responsibility}</p>
          </div>
        ))}
      </div>
    );
  };
