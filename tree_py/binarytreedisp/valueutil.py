class ValueUtil:
    #
    #
    def __init__(self):
        self.__float_precision = 2

    #
    #
    def get_float_precision(self):
        return self.__float_precision

    #
    #
    def set_float_precision(self, precision: int):
        if type(precision) is not int or precision < 0:
            raise ValueError('Invalid argument: precision must be non-negative integer')

        self.__float_precision = precision

    #
    #
    def get_str(self, value):
        type_value = type(value)

        if type_value is float:
            return str(round(value, self.__float_precision))

        if type_value is str:
            return value

        return str(value)
