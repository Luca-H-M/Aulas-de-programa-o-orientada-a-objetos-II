#Lista InfoWeb – POO – Lista 03 – Construtores e ToString
#1. Um Retângulo
import math
import random

class Retagnulo:
    def __init__(self):
        self.__base = 0
        self.__height = 0
    def set_base(self, b):
        if b > 0: self.__base = b
        else: raise ValueError()
    def set_height(self, h):
        if h > 0: self.__height = h
        else: raise ValueError()

    def get_base(self):
        return self.__base
    def get_height(self):
        return self.__height
    
    def CalcArea(self):
        return self.__height*self.__base
    def CalcDiagonal(self):
        return math.sqrt(self.__height**2 + self.__base**2)
    
    def __str__(self):
        return f"Base = {self.__base} - Altura = {self.__height}"
    
Retangulo = Retagnulo()
