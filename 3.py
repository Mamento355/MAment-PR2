# class Worker:
#     def __init__(self,name,surname,rate,days):
#         self.name = name
#         self.surname = surname
#         self.rate = rate
#         self.days = days
#     def dif(self):
#         return (f"Name: {self.name}\n"
#                 f"Surname: {self.surname}\n"
#                 f"Rate: {self.rate}\n"
#                 f"Days: {self.days}")
#     def GetSalary(self):
#         return self.rate * self.days
# x = Worker("Kirill","Mamentev",100000,7)
# y = x.GetSalary()
# print(x.dif())
# print(y)

# class Worker:
#     def __init__(self,name,surname,rate,days):
#         self._name = name
#         self._surname = surname
#         self._rate = rate
#         self._days = days
#     def get_name(self):
#         return self._name
#     def get_surname(self):
#         return self._surname
#     def get_rate(self):
#         return self._rate
#     def get_days(self):
#         return self._days
#     def GetSalary(self):
#         return self._rate * self._days
# x = Worker("Kirill","Mamentev",100000,7)
# print(f"Name: {x._name}\n"
#       f"Surname: {x._surname}\n"
#       f"Rate: {x._rate}\n"
#       f"Days:{x._days}")
# print(f"Salary: {x.GetSalary()}")

# class Calculation:
#     def __init__(self,calculationLine = ""):
#         self.calculationLine = calculationLine
#     def set_CalculationLine(self,calculation_Line):
#         self.calculationLine = str(calculation_Line)
#     def SetLastSymbolCalculationLine(self,x):
#         self.calculationLine += str(x)
#     def get_calculationLine(self):
#         return self.calculationLine
#     def get_LastSymbol(self):
#         return self.calculationLine[-1]
#     def DeleteLastSymbol(self):
#         self.calculationLine = self.calculationLine[:-1]
# x = Calculation()
# x.set_CalculationLine(4555555)
# x.SetLastSymbolCalculationLine(42324)
# print(x.get_calculationLine())
# print(x.get_LastSymbol())
# x.DeleteLastSymbol()
# print(x.get_calculationLine())



