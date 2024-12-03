from Data_base.IDataBase import IDataBase
import json


class DataBase(IDataBase):
    def __init__(self, path=''):
        self.__path = path

    async def get_cost(self, name):
        with open(self.__path, 'r', encoding='utf-8') as file:
            ans = json.load(file)
            return ans[name]

    async def set_cost(self, name, cost):
        with open(self.__path, 'r') as file:
            ans = json.load(file)
            ans[name] = cost
            json.dump(ans, file)