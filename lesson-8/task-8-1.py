class Data:
    def __init__(self, data):
        for i in range(0,3):
            Data.check_num(self.get_num_from_date(data,i),i)
        self.__data = data

    def __str__(self):
        return self.__data

    @classmethod
    def get_num_from_date(cls, data, position):
        try:
            return int(data.split("-")[position])
        except:
            print("Incorrect string")
            return 0

    @staticmethod
    def check_num(data, position):
        if position == 0 and data <= 31 or position == 1 and data <= 12 or position == 2 and 1900 < data < 2100:
            return True
        else:
            print("Incorrect Data")



d = Data("01-11-2012")
print(d)