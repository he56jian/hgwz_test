class Language:
    def __init__(self, type):
        self.language_type = type

    def learning(self):
        print(f'学习{self.language_type}')

    def translate_to_chinese(self, mess):
        print(f"{mess}翻译成中文")


en = Language('english')
en.learning()
en.translate_to_chinese('message')
