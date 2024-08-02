import json
import os.path
from abc import ABC, abstractmethod

from src.parser import HH

class FileWork(ABC):
    """
    Абстрактный класс, определяющий обязательные методы для классов-потомков.

    Этот класс служит основой для создания различных классов для работы с файлами.
    """

    def __init__(self):
        """
        Инициализирует объект FileWork.

        Конструктор не имеет параметров и может быть переопределен в подклассах.
        """

        pass

    @abstractmethod
    def read_file(self):
        """
        Чтение файла.

        Этот метод должен быть реализован в подклассах.

        Returns:
        Данные, прочитанные из файла.
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Запись данных в файл.
        Этот метод должен быть реализован в подклассах.
        Args:
        data: Данные, которые нужно сохранить в файл.
        """
        pass

    @abstractmethod
    def delete_file(self):
        """
        Удаление файла.

        Этот метод должен быть реализован в подклассах.

        Raises:
            FileNotFoundError: Если файл не найден по указанному пути.
            PermissionError: Если у программы нет прав на удаление файла.
        """
        pass


class WorkWithJson(ABC):
    """
    Класс для работы с JSON файлами.

    Этот класс наследуется от FileWork и реализует методы для загрузки, сохранения и удаления данных в формате JSON.
    """

    def __init__(self):
     """
     Инициализирует объект WorkWithJson и задает путь к файлу JSON.

     По умолчанию, файл будет находиться в директории "data" и называться "vacancies.json".
     """

     self.file_name = ""
     self.abs_path = os.path.abspath("data/vacancies.json")

    def read_file(self) -> None:
        """
        Запись данных в файл.
        Этот метод должен быть реализован в подклассах.
        Args:
        data: Данные, которые нужно сохранить в файл.
        """

        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data: list[dict]) -> None:
        """
        Сохраняет данные в JSON файл.

        Args:
        data (list[dict]): Данные, которые нужно сохранить.
        """
        with open(self.abs_path, "w", encoding="utf-8") as file:
            """res = json.load(file)
            res.append(data)"""
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        """
        Удаляет файл по указанному пути.

        Этот метод должен быть реализован в подклассах.

        Raises:
        FileNotFoundError: Если файл не найден по указанному пути.
        PermissionError: Если у программы нет прав на удаление файла.
        """

        return os.remove(self.abs_path)
