#The file may begin with comment lines. c
#The comment lines are followed by the "problem" line. p, varibles - clauses
#Clauses end with 0
#
def sat(entrada, variables):
    clausula = ""
    dummy = int(variables)+1

    if (len(entrada) == 1):
        return entrada[0] + " or " + str(dummy) + " or " + str(dummy*-1)

    elif (len(entrada) == 2):
        return entrada[0] + " or " + entrada[1] + " or " + str(dummy)

    elif(len(entrada)== 3):
        return entrada[0] + " or " + entrada[1] + " or " + entrada[2]

    else:
        for pos_actual in range(1,len(entrada)-1):
            #primera clausula
            if(pos_actual == 1):
                clausula += "(" + entrada[0] + " or "  + entrada[1] + " or " + str(dummy) + ") and"
            #ultima clausula
            elif(pos_actual == len(entrada) - 2):
                dummy *= -1
                clausula += " (" +  str(dummy) +" or " + entrada[len(entrada)-2] + " or " + entrada[len(entrada)-1] + ")"
            else:
                 dummy *= -1
                 clausula +=  " ("  + str(dummy) + " or " + entrada[pos_actual] + " or "
                 dummy *= -1
                 dummy += 1
                 clausula += str(dummy) + ') and'

    return clausula




datos = open("datos.txt", "r")
entrada = []
numeros = ""
for linea in datos:
    split = linea.split()
    #agrega la linea del problema
    if 'p' in split:
        variables = split[2]
        total_clauses = split[3]

    #ignora todas las lineas de comentario, solo agrega los numeros
    elif 'c' not in split:
       #removes the last 0
       linea = linea.split()
       linea.remove('0')

       cls = ""
       for i in linea:
           cls += i + " "

       print "Clausula: " + cls

       clausula = sat(linea, variables)
       print "3Sat: " +  clausula+ '\n'