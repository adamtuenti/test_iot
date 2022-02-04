import os
import functions as fn


fileName = input('Input file name: ')
if fileName == '':
    print('File default: ./files/schedule.txt')
    dict_schedule = fn.getEmployeesSchedule()
else:
    while not os.path.exists(fileName):
        print('File not found!')
        fileName = input('Input a correct file name: ')
    dict_schedule = fn.getEmployeesSchedule(fileName)


intersectionScheduleList = fn.getScheduleIntersection(dict_schedule)
fn.writeEmployeeIntersectionTable(intersectionScheduleList)
