# # # # class Student:
# # # #     def __init__(self, name, birth, group, grades):
# # # #         self.name = name
# # # #         self.birth = birth
# # # #         self.group = group
# # # #         self.grades = grades
# # # #     def dif(self, newname):
# # # #         self.name = newname
# # # #     def dif2(self, newbirth):
# # # #         self.birth = newbirth
# # # #     def dif3(self, newgroup):
# # # #         self.group = newgroup
# # # #     def dif4(self):
# # # #         return (f"Last Name: {self.name}\n"
# # # #                 f"Date of Birth: {self.birth}\n"
# # # #                 f"Group Number: {self.group}\n"
# # # #                 f"Grades: {self.grades}")
# # # # student1 = Student("Mamentev", "17.05.2006", "643", [3,2,4,5,2])
# # # # students = [student1]
# # # # print(student1.dif4())
# # # # student1.dif("Ivanov")
# # # # student1.dif2("12.07.2006")
# # # # student1.dif3("642")
# # # # print(student1.dif4())
# # # #
# # # # list_train = []
# # # # class Train:
# # # #     def  __init__(self,Thedestination,Number,Departuretime):
# # # #         self.Thedestination = Thedestination
# # # #         self.Number = Number
# # # #         self.Departuretime = Departuretime
# # # #     def dif(self):
# # # #         return (f"Thedestination: {self.Thedestination}\n"
# # # #                 f"Number: {self.Number}\n"
# # # #                 f"Departuretime: {self.Departuretime}")
# # # # def dif2(list_train,Number):
# # # #     for i in list_train:
# # # #         if i.Number == Number:
# # # #             return i
# # # # train1 = Train("Moscow","234","04:30")
# # # # train2 = Train("Saint-Peterburg","777","19:15")
# # # # train3 = Train("Tomsk","765","02:00")
# # # #
# # # # list_train = [train1,train2,train3]
# # # #
# # # # Number = int(input("Inter the number train: "))
# # # # if Number == 234:
# # # #     print(train1.dif())
# # # # if Number == 777:
# # # #     print(train2.dif())
# # # # if Number == 765:
# # # #     print(train3.dif())
# # #
# # # class Numbers:
# # #     def __init__(self,num1,num2):
# # #         self.num1 = num1
# # #         self.num2 = num2
# # #     def dif(self):
# # #         return (f"Number1: {self.num1}\n"
# # #                 f"Number2: {self.num2}")
# # #     def dif1(self,newnum1,newnum2):
# # #         self.num1 = newnum1
# # #         self.num2 = newnum2
# # #     def dif2(self):
# # #         return self.num1 + self.num2
# # #     def dif3(self):
# # #         return max(self.num1,self.num2)
# # # num = Numbers(23,5)
# # # print(num.dif())
# # # print(num.dif2())
# # # print(num.dif3())
# # # num.dif1(54,56)
# # # print(num.dif())
# # # sumnum = num.dif2()
# # # maxnum = num.dif3()
# # # print(sumnum)
# # # print(maxnum)
# #
# # class Operations:
# #     def __init__(self,num):
# #         self.num = num
# #     def dif(self):
# #         return(f"Number: {self.num}")
# #     def dif1(self):
# #         return self.num - 1
# #     def dif2(self):
# #         return self.num + 1
# # num = int(input("Inter the number: "))
# # x = Operations(num)
# # print(x.dif())
# # print(x.dif1())
# # print(x.dif2())
#
# class String:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def dif(self):
#         return(f"Numers1: {self.num1}\n"
#                f"Number2: {self.num2}")
#     def __del__(self):
#         print("Numbers deleted")
# num = String(75564,4536)
# print(num.dif())
# del num
#
#
#
