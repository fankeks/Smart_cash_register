from abc import ABC, abstractmethod


class INeuralNetwork(ABC):
    @abstractmethod
    def __init__(self):
        '''
        Инициализатор
        '''
        pass

    @abstractmethod
    def get_report(self, path) -> list:
        '''
        Получить ответ от нейросети.
        Обработанное изображение перезаписывается.
        :param path Путь до изображения с продуктами
        :return: Возвращает список продуктов на изображении (Название продукта, количество). Если продуктов нет - возвращает пустой список
        '''

        return []