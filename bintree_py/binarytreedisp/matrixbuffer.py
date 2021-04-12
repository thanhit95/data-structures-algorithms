class MatrixBuffer:
    '''
    Matrix buffer which stores an ASCII image.
    '''
    #
    #
    def __init__(self, width: int, height: int):
        if type(width) is not int or width < 1:
            raise ValueError('width must be a positive integer')

        if type(height) is not int or height < 1:
            raise ValueError('height must be a positive integer')

        self.__width = width
        self.__height = height

        self.__a = [[' '] * width for _ in range(height)]

    #
    #
    def width(self):
        return self.__width

    #
    #
    def height(self):
        return self.__height

    #
    #
    def fill(self, posx: int, posy: int, value: str):
        if type(value) is not str:
            raise ValueError('Invalid argument: value must be a string')

        if posx < 0 or posx >= self.__width:
            raise ValueError('Invalid argument: posx')

        if posy < 0 or posy >= self.__height:
            raise ValueError('Invalid argument: posy')

        a = self.__a
        posx_start = posx
        len_value = len(value)

        for i in range(len_value):
            posx = posx_start + i

            if posx >= self.__width:
                break

            a[posy][posx] = value[i]

    #
    #
    def fill_line(self, character: str, y: int, startx: int, endx: int):
        for x in range(startx, endx + 1):
            self.__a[y][x] = character

    #
    #
    def get_str(self) -> str:
        lst_rows = self.get_lst_rows()
        res = '\n'.join(lst_rows)
        return res

    #
    #
    def get_lst_rows(self) -> list:
        lst_rows = [''.join(row).rstrip() for row in self.__a]
        return lst_rows
