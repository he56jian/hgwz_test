class Cellphone:
    def __init__(self,num):
        self.number = num

    def cell_to_phone(self,num):
        print(f'打电话，本机号码；{self.number},拨打号码：{num}')

    def send_mess(self,mess):
        print(f'发信息：{mess}')

ph = Cellphone('156186456')
ph.cell_to_phone('102315646')