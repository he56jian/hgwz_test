from hgwz_test.hgwz_python.作业2.TongLao.TongLao import TongLao


class XuZhu(TongLao):
    def __init__(self,hp,power):
        super().__init__(hp,power)

    def read(self):
        print('罪过罪过')


if __name__ == "__main__":
    xz = XuZhu(100, 100)
    xz.read()
