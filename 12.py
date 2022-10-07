class B:
    __s = None

    def __new__(cls, *args, **kwargs):
        if B.__s is None:
            B.__s = super().__new__(cls)
        return B.__s


    def __del__(self):
        print('Удалил', self)


a = B()
del a

input()
