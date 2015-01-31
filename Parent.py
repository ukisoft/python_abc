# -*- coding: utf-8 -*-


class Parent(object):

    def __init__(self, name):
        self.name = name  # self.__nameだとChildから呼べない

    def explain(self):
        print(self.name)