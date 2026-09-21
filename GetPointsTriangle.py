class CalcTriangle:
    def GetPointsAndType(self):
        FirstSide = float(input("ВВедите размер первой стороны: "))
        SecondSide = float(input("ВВедите размер второй стороны: "))
        ThirdSide = float(input("ВВедите размер третье стороны: "))
        return

    def ItExist(self,s1,s2,s3):
        if(s1 + s2 < s3):
            return False
        elif(s1 + s3 < s2):
            return False
        elif(s2 + s3 < s1):
            return False
        return True

    def CalcType(self, s1, s2, s3):
        if(not self.ItExist(s1,s2,s3)):
            return "Не треугольник"
        elif(s1 == s2 == s3):
            return "Равносторонний"
        elif(s1 != s2 & s2 != s3 & s1 != s3): # Нужно попробывать (s1 != s2 != s3)
            return "Разносторонний"
        return "Равнобедренный"

    def CalcPoints(self, s1, s2, s3):
        if (not self.ItExist(s1, s2, s3)):
            return [(-1,-1),(-1,-1),(-1,-1)]

