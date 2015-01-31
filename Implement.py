# -*- coding: utf-8 -*-

from Abstract import *


class Implement(Abstract):

    @classmethod
    def uppercase(cls, name):
        return name.upper() + ' by Impl'

    def hello(self):
        print('Hello ' + self.name)