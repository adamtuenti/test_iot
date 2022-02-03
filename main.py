import functions as fn


fileName = input('Input file name: ')
if(fileName != ''):
    dict_schedule = fn.getEmployeesSchedule(fileName)
else:
    dict_schedule = fn.getEmployeesSchedule()


intersectionScheduleList = fn.getScheduleIntersection(dict_schedule)
fn.writeEmployeeIntersectionTable(intersectionScheduleList)


#
# listaEmpleados = list(d.keys())
# copia = list(d.keys())
# print(d['ASTRID'], d['RENE'])
# f2 = open('eresBonito.txt', 'w')
# for empleado in copia:
#     listaEmpleados.remove(empleado)
#     horario = d[empleado]
#     for empleado2 in listaEmpleados:
#         horario2 = d[empleado2]
#         comun = horario & horario2
#         if(len(comun) > 0):
#             f2.write(empleado + '-' + empleado2 + ':' + str(len(comun)) + '\n')
#
# listaEmpleados = list(d.keys())
# copia = list(d.keys())
# nombresCantidad = len(listaEmpleados)
# #for empleado in lista
# # nombresCantidad = len(listaEmpleados)
# for actual in range(0, nombresCantidad - 1):
#     empleado1 = listaEmpleados[actual]
#     h1 = d[empleado1]
#     for siguiente in range(actual + 1, nombresCantidad):
#         empleado2 = listaEmpleados[siguiente]
#         h2 = d[empleado2]
#         comun = h1 & h2
#         if (len(comun) > 0):
#             f2.write(empleado1 + '-' + empleado2 + ':' + str(len(comun)) + '\n')
#
#
#
# f.close()
# f2.close()
# # OUTPUT:
# # ASTRID-RENE: 2
# # ASTRID-ANDRES: 3
# # RENE-ANDRES: 2