import math


class CalcTriangle:
    def GetPointsAndType(self):
        try:
            firstSide = float(input("ВВедите размер первой стороны: "))
            secondSide = float(input("ВВедите размер второй стороны: "))
            thirdSide = float(input("ВВедите размер третье стороны: "))
            return
        except ValueError:
            return ("",[(-2,-2),(-2,-2),(-2,-2)])

    def ItExist(self,s1,s2,s3):
        if(s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
            return False
        elif(s1 <= 0 or s2 <= 0 or s3 <= 0):
            return False
        return True

    def CalcType(self, s1, s2, s3):
        if(not self.ItExist(s1,s2,s3)):
            return "Не треугольник"
        elif(s1 == s2 == s3):
            return "Равносторонний"
        elif(s1 != s2 and s2 != s3 and s1 != s3):
            return "Разносторонний"
        return "Равнобедренный"

    def CalcPoints(self, s1, s2, s3):
        if (not self.ItExist(s1, s2, s3)):
            return [(-1,-1),(-1,-1),(-1,-1)]

        a = (0,0)
        b = (s3,0)
        cos_a = (s2**2 + s3**2 - s1**2) / (2 * s2 * s3)
        cos_a = max(-1.0, min(1.0, cos_a))
        c = (s2 * cos_a, s2 * math.sqrt(1 - cos_a**2))
        return [a,b,c]

    def CanPutInSquare(self,a,b,c,size=100):


