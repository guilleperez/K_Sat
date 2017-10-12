#The file may begin with comment lines. c
#The comment lines are followed by the "problem" line. p, varibles - clauses
#Clauses end with 0
#
def sat(entrada):
    clausula = ""
    dummy = 1
    x = 0
    y = 1

    if (len(entrada) == 1):
        return entrada[0] + " " + dummy + " " + dummy-1

    elif (len(entrada) == 2):
        return entrada[0] + " " + entrada[1] + " " + dummy

    elif(len(entrada)== 3):
        return entrada[0] + " " + entrada[1] + " " + entrada[2]

    else:
        for pos_actual in range(1,len(entrada)-1):
            #primera clausula
            if(pos_actual == 1):
                clausula += entrada[0] + " "  + entrada[1] + " " + str(dummy) + "\n"
            #ultima clausula
            elif(pos_actual == len(entrada) - 2):
                dummy -= 1
                clausula += str(dummy) +" " + entrada[len(entrada)-2] + " " + entrada[len(entrada)-1]
            #clausulas 2 - n-1
            else:
                 dummy -= 1
                # y += 1
                # if(y%3 == 0):
                #     y = 0
                #     x +=1
                 clausula += str(dummy) + " " + entrada[pos_actual] + " "
                 dummy += 1
                 clausula += str(dummy) + '\n'

    return clausula




datos = open("datos.txt", "r")
entrada = []
numeros = ""
for linea in datos:
    split = linea.split()
    #agrega la linea del problema
    if 'p' in split:
        #entrada.append(split)
        variables = split[2]
        total_clauses = split[3]

    #linea = linea.split(
    #ignora todas las lineas de comentario, solo agrega los numeros
    elif 'c' not in split:
       # numeros += linea
       #print linea
       #removes the las 0
       linea = linea.split()
       linea.remove('0')
       print  linea

       clausula = sat(linea)
       print clausula + '\n'

# numeros = numeros.split()
# num = []
# for i in numeros:
#     #verifica que no sea sea, pertenece a la clausula
#     if(i != '0'):
#         num.append(i)
#     else:
#         #si es 0, cambia de clausula
#         entrada.append(num)
#         num = []
#
#
#
#
# print "Variables", variables, "Clausulas" , total_clauses
# entrada.remove(entrada[0])
#
# print entrada
# clausula = sat(entrada,  total_clauses)
# print clausula
# #clauses = []
# claus = "( "
# for i in range(int(total_clauses)):
#
#     for j in range(len(entrada[i])):
#         if(entrada[i][j] > 0 ):
#              claus += 'x'
#         else:
#             claus += '-x'
#             entrada[i][j] = int(entrada[i][j]) * -1
#
#         if(j != len(entrada[i]) - 1):
#             claus += str(entrada[i][j]) + " or "
#         else:
#             claus += str(entrada[i][j])
#
#     if (i != len(entrada) - 1):
#         claus += " or "
#
#
# claus += " ) "
#
# print claus
#
