class State():
    def __init__(self, **chameleon_count):
        self.__red_count = chameleon_count['red']
        self.__green_count = chameleon_count['green']
        self.__blue_count = chameleon_count['blue']
        self.__parent = None

    @property
    def red_count(self):
        return self.__red_count

    @property
    def blue_count(self):
        return self.__blue_count

    @property
    def green_count(self):
        return self.__green_count

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, obj):
        self.__parent = obj

    def has_red_ones(self):
        return bool(self.__red_count)

    def has_only_red_ones(self):
        return self.has_red_ones() and not self.has_green_ones() and not self.has_blue_ones()

    def has_green_ones(self):
        return bool(self.__green_count)

    def has_only_green_ones(self):
        return self.has_green_ones() and not self.has_red_ones() and not self.has_blue_ones()

    def has_blue_ones(self):
        return bool(self.__blue_count)

    def has_only_blue_ones(self):
        return self.has_blue_ones() and not self.has_green_ones() and not self.has_red_ones()

    def has_only_one_color(self):
        return self.has_only_blue_ones() or self.has_only_green_ones() or self.has_only_red_ones()

    def red_met_green(self):
        if self.__red_count < 1 or self.__green_count < 1:
            raise Exception('Invalid green or red count')
        red_count = self.__red_count - 1
        green_count = self.__green_count - 1
        blue_count = self.__blue_count + 2
        new_state = State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
        new_state.parent = self
        return new_state
    def green_met_blue(self):
        if self.__blue_count < 1 or self.__green_count < 1:
            raise Exception('Invalid green or blue count')
        red_count = self.__red_count + 2
        green_count = self.__green_count - 1
        blue_count = self.__blue_count - 1
        new_state = State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
        new_state.parent = self
        return new_state
    def blue_met_red(self):
        if self.__red_count < 1 or self.__blue_count < 1:
            raise Exception('Invalid blue or red count')
        red_count = self.__red_count - 1
        green_count = self.__green_count + 2
        blue_count = self.__blue_count - 1
        new_state = State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
        new_state.parent = self
        return new_state

    def __str__(self):
        return '(red={},green={},blue={})'.format(self.red_count, self.green_count, self.blue_count)
