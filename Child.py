# -*- coding: utf-8 -*-

from Parent import *


class Child(Parent):

    def __init__(self, name, age):
        super().__init__(name)
        self.__age = age

    def explain(self):
        print(self.name, self.__age)