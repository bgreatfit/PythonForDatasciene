import useful_func as uf

while True:
    try:
        names = input('Enter names separated by commas:')  # get and process input for a list of names
        if not names.isalpha():
            break
    except Exception as e:
        print(e)
names = names.split(',')

while True:
    try:
        assignments = input('Enter assignment counts  separated by commas:') # get and process input for a list of names
        if not assignments.isdigit():
            break
    except Exception as e:
        print(e)
assignments = assignments.split(',')
while True:
        try:
            grades = input('Enter grades separated by commas:')  # get and process input for a list of names
            if not grades.isdigit():
                break
        except Exception as e:
            print(e)
grades = grades.split(',')
for 
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

# while True:
#     try:
#         names = int(input('Enter names separated by commas:'))  # get and process input for a list of names
#         bretry:
#         names = int(input('Enter assignment counts separated by commas:')) # get and process input for a list of names
#         breakak
#     except:
#         print('Wrong input')
#     finally:
#         print('Attempted Input\n')
while True:
    number = int(input('Enter number:\n'))
    if number > 0 or number < 23:
        break
# assignments = input()  # get and process input for a list of the number of assignments
# grades = input()  # get and process input for a list of grades

# i = 0
# student_names = []
# while i < 3:
#     student_names.append(input('Pls enter Student name: '))
#     i = i + 1
# print(student_names)
