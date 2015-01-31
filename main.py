# -*- coding: utf-8 -*-

from Child import *
from Implement import *


if __name__ == "__main__":
    parent = Parent('Bob')
    parent.explain()  # Bob

    child = Child('Bob Jr.', 6)
    child.explain()  # Bob Jr. 6

    impl = Implement('John')
    impl.explain()  # JOHN by Impl
    impl.hello()  # Hello JOHN by Impl

    # Abstractクラスもobjectを作れる
    # Implementクラスに未実装のabstractmethodがあっても、objectを作れる
