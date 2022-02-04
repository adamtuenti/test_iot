import datetime

def getEmployeesSchedule(file_name = './files/schedule.txt'):
    '''This function recive a file name and return a dictionary, keys: the name of the employee
    and the value is another dictionary, key is the day and the value a tuple (entrance, out)'''
    file = open(file_name, 'r')
    dict_schedule = {}
    for line in file:
        line = line.strip()
        name, schedule = line.split('=')
        list_schedule = schedule.split(',')
        dict_schedule[name] = {}
        for item in list_schedule:
            day = item[:2]
            item = item[2:].split('-')
            entrance = item[0]
            output = item[1]
            dict_schedule[name][day] = (entrance, output)
    file.close()
    return dict_schedule


def getMinutes(time):
    '''This function recive a string hh:mm and return the total of minutes'''
    datem = datetime.datetime.strptime(time, "%H:%M")
    total_minutes = datem.hour * 60 + datem.minute
    return total_minutes

def getTimeIntersection(tuple1, tuple2):
    '''This function recive two tuples, entrance and out of the employees
    return 1 or 0, depends if they met in the office'''
    input1, output1 = tuple1
    input1 = getMinutes(input1)
    output1 = getMinutes(output1)
    input2, output2 = tuple2
    input2 = getMinutes(input2)
    output2 = getMinutes(output2)
    cond1 = (input1 >= input2) and (output1 <= output2)
    cond2 = (input1 <= input2) and (output1 >= output2)
    cond3 = (input1 >= input2) and (output1 >= output2) and (output2 >= input1)
    cond4 = (input1 <= input2) and (output1 <= output2) and (output1 >= input2)
    total = cond1 + cond2 + cond3 + cond4
    return total


def getScheduleIntersection(scheduleDict):
    listEmployees = list(scheduleDict.keys())
    count = len(listEmployees)
    intersectionScheduleList = []
    for actual in range(0, count - 1):
        employee1 = listEmployees[actual]
        dictSchedule1 = scheduleDict[employee1]
        for next in range(actual + 1, count):
            employee2 = listEmployees[next]
            dictSchedule2 = scheduleDict[employee2]
            counter = 0
            for dayItem in dictSchedule2.keys():
                if dayItem in dictSchedule1:
                    tuple1 = dictSchedule1[dayItem]
                    tuple2 = dictSchedule2[dayItem]
                    numberIntersection = getTimeIntersection(tuple1, tuple2)
                    if numberIntersection > 0:
                        counter += 1
            if counter > 0:
                item = '{};{};{}\n'.format(employee1, employee2, str(counter))
                intersectionScheduleList.append(item)
    return intersectionScheduleList

def writeEmployeeIntersectionTable(intersectionScheduleList):
    '''Input a list with the string of each coincidence employees,
    write in a file csv each line'''
    file = open('./files/scheduleIntersection.csv', 'w')
    file.write('Employee 1;Employee 2;Counter\n')
    for item in intersectionScheduleList:
        if item == intersectionScheduleList[-1]:
            item = item[:-1]
        file.write(item)
    print('File created! scheduleIntersection.csv')
    file.close()
