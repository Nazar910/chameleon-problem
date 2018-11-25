class State():
    def __init__(self, **chameleon_count):
        self.__red_count = chameleon_count['red']
        self.__green_count = chameleon_count['green']
        self.__blue_count = chameleon_count['blue']

    def get_red_count(self):
        return self.__red_count

    def get_blue_count(self):
        return self.__blue_count

    def get_green_count(self):
        return self.__green_count

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
        green_count = self.__red_count - 1
        blue_count = self.__blue_count + 2
        return State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
    def green_met_blue(self):
        if self.__blue_count < 1 or self.__green_count < 1:
            raise Exception('Invalid green or red count')
        red_count = self.__red_count + 2
        green_count = self.__red_count - 1
        blue_count = self.__blue_count - 1
        return State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
    def blue_met_red(self):
        if self.__red_count < 1 or self.__blue_count < 1:
            raise Exception('Invalid green or red count')
        red_count = self.__red_count - 1
        green_count = self.__green_count + 2
        blue_count = self.__blue_count - 1
        return State(
            red=red_count,
            green=green_count,
            blue=blue_count
        )
