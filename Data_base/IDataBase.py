from abc import ABC, abstractmethod


class IDataBase(ABC):
    @abstractmethod
    def __init__(self, path):
        '''
        Инициализатор
        :param path: Путь до базы данных
        '''
        pass

    @abstractmethod
    async def get_cost(self, name):
        '''
        Асинхронный метод получения стоимости товара
        :param name: Наименование товара
        :return:
        '''
        pass

    @abstractmethod
    async def set_cost(self, name, cost):
        '''
        Асинхронный метод изменения стоимости товара
        :param name: Наименование товара
        :param cost: Новая стоимость товара
        :return:
        '''
        pass