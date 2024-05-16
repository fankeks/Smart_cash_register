from abc import ABC, abstractmethod


class IPhotoHandler (ABC):
    def __init__(self, path) -> None:
        '''
        Инициализатор
        :param path: Путь к файлу для обработки
        :return None
        '''
        pass

    async def start(self):
        '''
        Асинхронный метод запуска обработки
        :return: None
        '''
        pass

    async def join(self):
        '''
        Асинхронный метод ожидания завершения обработки
        :return: Ответ нейросети
        '''
        pass