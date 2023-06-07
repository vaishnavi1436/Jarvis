# #example of String
# Name = "Pranav"
# Name2 = 'Pannu'
# num1 = "@"
# number = 12
# print(Name)
# print(Name2)
# print(num1)
# print(type(num1))
# print(number)
# print(type(number))

# String has index which starts from 0 and eds with -1
# -9   .  .   .   .  . . -4   -3   -2   -1
# V  a  i  s  h  n  a  v  i
# 0  1  2  3  4  5  6  7  8
#
# Name = "Vaihsnavi"
# print(Name[-1])
# print(Name[-2])
# print(Name[-3])
# print(Name[-4])
# print(Name[-5])

# String Slicing Operations
# Name1 = "Vaishnavi Kulkarni"
# print(Name1[0])
# print(Name1[1])
# print(Name1[2])
# print(Name1[3])
# print(Name1[4])
# print(Name1[5])
# print(Name1[6])
# print(Name1[7])
# print(Name1[8])
# # print(Name1[9])
# print(Name1[10])
# print(Name1[11])
# print(Name1[12])
# print(Name1[13])
# print(Name1[14])
# print(Name1[15])
# print(Name1[16])
# print(Name1[17])

# str = "Welcome to Python"
# print(str)  #Welcome to Python
# print(str[0]) #W
# print(str[2:9]) #lcome t       slicing = [start_index:end_index-1]
# print(str[4:]) #ome to Python if we dont specifiy anything as end index in slicing then it will print whole string
# print(str*3) #l
# print(str+'Programming') #Welcome to PythonProgramming
# print(str[-1]) #n

# string1 = "9 Feb 2023 Time is 20:02"
# # output = 9 Feb 2023
# print(string1[0:10])
# # output = 9 Feb 20:02
# print(string1[0:5],string1[-5:])
# # output = Time 20:02
# print(string1[11:15],string1[-5:])


#             0         1   2
# list1 = ["Vaihsnavi",67,90.56]
# print(type(list1))

# list1 = [15,25,3.34,"Ravi",14526320014,124E-2,"Jammu",0.14356]
# list2 = [145,"Chandrika"]
# print(list1)    #[15,25,3.34,"Ravi",14526320014,124E-2,"Jammu",0.14356]
# print(list1[0]) #15
# print(list1[1:3]) #[25,3.34]
# print(list1[2:]) #[3.34,"Ravi",14526320014,124E-2,"Jammu",0.14356]
# print(list2*2) #[145,"Chandrika",145,"Chandrika"]
# print(list1+list2) #[15,25,3.34,"Ravi",14526320014,124E-2,"Jammu",0.14356,145,"Chandrika"]
# print(list1[-1]) #0.14356