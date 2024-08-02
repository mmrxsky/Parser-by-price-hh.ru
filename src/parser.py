from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Класс Parser является родительским классом, который  необходимо реализовать

    Этот класс служит основой для создания различных парсеров вакансий.
    Он определяет интерфейс, который должны реализовать все подклассы.
    """
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter

    Этот класс позволяет загружать вакансии с сайта HeadHunter по заданному ключевому слову.
    """

    def __init__(self, keyword: str):
        """
        Инициализирует объект HH и задает параметры для API запросов.
        Args:
        keyword (str): Ключевое слово для поиска вакансий.
        """

        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}

    def load_vacancies(self) -> list[dict]:
        """ Загружает список вакансий.

        Выполняет GET запрос к API HeadHunter и возвращает результат в виде списка словарей.
        Returns:
            list[dict]: Список словарей, каждый из которых содержит данные о вакансии.
        """

        vacancies = []

        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            vacancies.extend(vacancies)
            self.params['page'] += 1

        return vacancies
