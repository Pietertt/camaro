class Activity:
    _year = None
    _month = None
    _day = None
    _hour = None
    _minute = None
    _second = None
    _valid = None

    def __init__(self, valid):
        self._valid = valid

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def set_month(self, month):
        self._month = month
    
    def get_month(self):
        return self._month

    def set_day(self, day):
        self._day = day

    def get_day(self):
        return self._day