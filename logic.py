import random
from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        zona_obitania=['везде','неизвестно','вулканы','леса','озёра и реки','']

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(200, 400)
        self.ex = randint(0, 1000)
        self.zona=random.choice(zona_obitania)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]["home"]["front_default"])
        else:
            return "https://divinebovinity.org/wp-content/uploads/2021/11/pokemon-6.jpg"

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
тренер покемона : @{self.pokemon_trainer}
здоровье покемона : {self.hp}
энергия покемона : {self.ex}
зона обитания : {self.zona}
"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img




