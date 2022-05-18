class SuperToBase():

    def __init__(self, common_allowances):
        self.ta = common_allowances['ta']
        self.da = common_allowances['da']
        self.hra = common_allowances['hra']

class Base(SuperToBase):

    def __init__(self, basic, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.basic = basic
        # self.common_allwances= self.

    def calculate_pay(self):
        gross= self.basic+ self.da+ self.ta+ self.hra
        print(gross)

def main():
    run = Base(456, {'ta':45, 'da':55, 'hra':556})
    run.calculate_pay()

if __name__ == '__main__':
    main()