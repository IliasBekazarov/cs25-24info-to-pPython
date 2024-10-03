#
# students = ['ilias', 'sara', 'adam', 'asel']
# faculties = ['IT', 'medicine', 'teacher', 'translator']
# balOrt = [109, 210, 110, 80]
# balNeedORT = [110, 160, 200, 50]
#
# ################################################################
# # for and if.
#
# input("адам")
# for i in range(len(students)):
#     if balOrt[i] >= balNeedORT[i]:
#         print(f"{students[i]} {faculties[i]} факультетине өткөн.")
#     else:
#         print(f"{students[i]} {faculties[i]} факультетине өтпөгөн.")

# ###################################################################
# #while and if
#
# index = -1
# while index < len(students):
#
#     if balOrt[index] >= balNeedORT[index]:
#
#         print(f"{students[index]} керектүү баллды топтоду")
#     else:
#         print(f"{students[index]} керектүү баллды топтогон жок")
#
#     index += 1

###################################################################
# input менен
#
# print('адамдардын аттарын жаз')
# students = [input('1-адам'),input('2-адам'),input('3-адам'),input('4-адам')]
#
# print('тандаган факултеттерин жаз')
# faculties = [input('1-адам'),input('2-адам'),input('3-адам'),input('4-адам')]
#
# print("ОРТ -дан алган балдарын жаз")
# balOrt = [input('1-адам'),input('2-адам'),input('3-адам'),input('4-адам')]
#
# print("ОРТ -га керектуу (босого) болды жаз")
# balNeedORT = [input('1-адам'),input('2-адам'),input('3-адам'),input('4-адам')]
#
################################################################
# #for and if.
#
# for i in range(len(students)):
#     if balOrt[i] >= balNeedORT[i]:
#         print(f"{students[i]} {faculties[i]} факультетине өткөн.")
#     else:
#         print(f"{students[i]} {faculties[i]} факультетине өтпөгөн.")

################################################################################

# students = ['ilias', 'sara', 'adam', 'asel']
# faculties = ['IT', 'medicine', 'teacher', 'translator']
# balOrt = [109, 210, 110, 80]
# balNeedORT = [110, 160, 200, 50]
#
# student_name = input("Студенттин атын киргизиңиз: ilias, Sara, Adam, Asel. ")
#
# if student_name in students:
#
#     a = students.index(student_name)
#
#     if balOrt[a] >= balNeedORT[a]:
#         print(f"{students[a]} {faculties[a]} факультетине өткөн.")
#     else:
#         print(f"{students[a]} {faculties[a]} факультетине өтпөгөн.")
# else:
#     print("Мындай студент тизмеде жок.")
