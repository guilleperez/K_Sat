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
            else:
                 dummy -= 1
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

       clausula = sat(linea)
       print "3Sat:\n" +  clausula+ '\n'