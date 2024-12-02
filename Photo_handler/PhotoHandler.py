import asyncio
import multiprocessing as mp
import json
import os


from Neural_network.NeuralNetwork import NeuralNetwork
from Neural_network.NeuralNetwork import d_translator
from Photo_handler.IPhotoHandler import IPhotoHandler


class PhotoHandler(IPhotoHandler):
    @staticmethod
    def f(path):
        neural_network = NeuralNetwork()
        ans = neural_network.get_report(path)
        print(ans)
        with open(path.split('.')[0] + '.json', 'w') as file:
            json.dump(ans, file)
        return None

    def __init__(self, path):
        self.__p = mp.Process(target=self.f, args=(path,))
        self.__path = path

    async def start(self):
        self.__p.start()

    async def join(self):
        while self.__p.is_alive():
            await asyncio.sleep(0)

        with open(self.__path.split('.')[0] + '.json', 'r') as file:
            ans = json.load(file)
        os.remove(self.__path.split('.')[0] + '.json')
        return ans
