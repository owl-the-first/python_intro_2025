class Sender:
    flag = False

    @classmethod
    def report(cls):
        if not cls.flag:
            cls.flag = True
            print('Greetings!')
            return
        print('Get Away!')

class Asker:
    @staticmethod
    def askall(*lst):
        for item in lst:
            item.report()

lst = [Sender(), Sender(), Sender()]
asker = Asker()
print(asker.askall(*lst))
