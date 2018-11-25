class Compositor():
    has_children = True
    def __init__(self, data):
        self.__data = data
        self.__leafs = []

    def add_leaf(self, leaf):
        self.__leafs.append(leaf)

class Leaf():
    has_children = False
    def __init__(self, data):
        self.__data = data
