class MatrixBuffer:
    '''
    Matrix buffer which stores an ASCII image.
    '''
    #
    #
    def __init__(self, width, height):
        self.width = width
        self.height = height

        cell = ' '

        self.a = [[cell] * width for i in range(height)]

    #
    #
    def fill(self, posx: int, posy: int, value: str):
        if posx < 0:
            raise ValueError('Invalid argument: posx')

        if posy >= self.height:
            raise ValueError('Invalid argument: posy')

        if type(value) is not str:
            raise ValueError('Invalid argument: value --> must be string')

        a = self.a
        len_value = len(value)

        for i in range(len_value):
            if posx + i >= self.width:
                break

            a[posy][posx + i] = value[i]

    #
    #
    def get_str(self):
        lst_rows = self.get_lst_rows()
        res = '\n'.join(lst_rows)
        return res

    #
    #
    def get_lst_rows(self):
        a = self.a
        lst_rows = [''.join(a[i]).rstrip() for i in range(self.height)]
        return lst_rows
