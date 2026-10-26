class Converter:
    @staticmethod
    def do(x):
        if x >= 100.7:
            return 1000
        elif x > 0:
            return int(x)
        elif x == 0:
            raise ValueError("X не может быть 0")
        elif x >= -30.4:
            return int(x) - 5
        return -2000