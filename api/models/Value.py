class Value:
    _distance = None
    _ldr = None

    def __init__(self):
        pass

    def set_distance(self, distance):
        self._distance = distance

    def get_distance(self):
        return self._distance

    def set_ldr(self, ldr):
        self._ldr = ldr
    
    def get_ldr(self):
        return self._ldr