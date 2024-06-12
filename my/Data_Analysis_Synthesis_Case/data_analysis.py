class Record:

    def __init__(self, Date, Id, Sales, Province):
        self.Date = Date
        self.Id = Id
        self.Sales = Sales
        self.Province = Province

    def __str__(self):
        return f'{self.Date},{self.Id},{self.Sales},{self.Province}'