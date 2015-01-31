# -*- coding: utf-8 -*-

from abc import *


class Abstract(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = self.uppercase(name)  # self.__nameだとImplementから呼べないのは継承と同じ

    @classmethod
    @abstractmethod
    def uppercase(cls, name):  # __uppercase(cls, name):だと、Implementクラスで実装しても、Abstractクラスのメソッドが呼ばれる
        raise NotImplementedError()

    def explain(self):
        print(self.name)

    @abstractmethod
    def hello(self):
        raise NotImplementedError()