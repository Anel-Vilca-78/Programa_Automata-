
def validarCadena(cadena):
    if len(cadena) < 12:
        print("q0 →")
        if cadena[0] == "S":
            print("q1 →")
            if cadena[1] == "A":
                print("q2 →")
                if cadena [2] == "E":
                    print("q3 →")
                    if cadena [3] == " ":
                        print("q4 →")

                      #Aqui inicia el 1er switch
                      
                      #CADENA SAE 0W-20
                        if cadena[4] =="0":
                            print("q7 →")
                            if cadena[5] == "W":
                                print("q18 →")
                                if cadena [6] == "-":
                                    print("q20 →")
                                    if cadena [7] == "2":
                                        print("q21 →")
                                        if cadena [8] == "0":
                                            print("q22")
                                            print("cadena correcta")
                                        else:
                                            print("q21 falla")
                                    else:
                                        print("q20 falla")
                                else:
                                    print("q18 falla")
                            else:
                                print("q7 falla")
                            
                        #CADENAS SAE 5W-30 ||40||50
                        elif cadena[4] =="5": 
                            print("q5 →")
                            if cadena[5] == "W":
                               print("q19 →")
                               if cadena[6] == "-":
                                   print("q23 →")
                                   #Cadena SAE 5W-30
                                   if cadena[7] == "3":
                                        print("q24 →")
                                        if cadena[8] == "0":
                                            print("q27 ")
                                            print("cadena correcta")
                                        else:
                                            print("q24 falla")
                                    #Cadena SAE 5W-40
                                   elif cadena[7] =="4":
                                        print("q25 →")
                                        if cadena[8] == "0":
                                            print("q27")
                                            print("cadena correcta")
                                        else:
                                            print("q25 falla")
                                    #Cadena SAE 5W-50
                                   elif cadena[7] =="5":
                                        print("q26 →")
                                        if cadena[8] == "0":
                                            print("q27")
                                            print("cadena correcta")
                                        else:
                                            print("q26 falla")
                                   else:
                                       print("q23 falla")
                               else:
                                   print("q19 falla")
                            else:
                                print("q5 falla")

                        #CADENAS de iniciales SAE 10W- ||  SAE 15W
                        elif cadena[4] =="1":
                            print("q6 →")
                            if cadena[5] == "0":
                                print("q9 →")
                                if cadena[6] == "W":
                                    print("q14 →")
                                    if cadena[7] == "-":
                                        print("q15 →")
                                        #Cadena SAE 10W-30
                                        if cadena[8] == "3":
                                            print("q30 →")
                                            if cadena[9] == "0":
                                                print("q33")
                                                print("cadena correcta")
                                            else:
                                                print("q30 falla")
                                        #Cadena SAE 10W-40
                                        elif cadena[8] =="4":
                                            print("q31 →")
                                            if cadena[9] == "0":
                                                print("q33")
                                                print("cadena correcta")
                                            else:
                                                print("q31 falla")
                                        #Cadena SAE 10W-50
                                        elif cadena[8] =="5":
                                            print("q32 →")
                                            if cadena[9] == "0":
                                                print("q33")
                                                print("cadena correcta")
                                            else:
                                                print("q32 falla")

                                        else:
                                            print("q15 falla")
                                    else:
                                        print("q14 falla")
                                else:
                                    print("q9 falla")

                            #CADENA SAE 15W-40
                            elif cadena[5] == "5":
                                print("q10 →")
                                if cadena[6] == "W":
                                    print("q11 →")
                                    if cadena[7] == "-":
                                        print("q13 →")
                                        if cadena[8] == "4":
                                            print("q34 →")
                                            if cadena[9] == "0":
                                                print("q35")
                                                print("cadena correcta")
                                            else:
                                                print("34 falla")
                                            print("q13 falla")
                                    else:
                                        print("q11 falla")
                                   
                                else:
                                    print("q10 falla")
                                
                            else:
                                print("q6 falla")

                        #CADENA SAE 20W-50
                        elif cadena[4] =="2":
                            print("q8 →")
                            if cadena[5] == "0":
                                print("q12 →")
                                if cadena[6] == "W":
                                    print("q16 →")
                                    if cadena[7] == "-":
                                        print("q17 →")
                                        if cadena[8] == "5":
                                            print("q28 →")
                                            if cadena[9] == "0":
                                                print("q29")
                                                print("cadena correcta")
                                            else:
                                                print("q28 falla")
                                        else:
                                            print("q17 falla")
                                    else:
                                        print("q16 falla")
                                else:
                                    print("q12 falla")
                                
                            else:
                                print("q8 falla")
                        else:
                             print("q4 falla")
                    else:
                        print("q3 falla")
                else:
                    print ("q2 falla")
            else:
                print("q1 falla")
        else:    
            print("q0 falla")
    else: 
        print("La cadena es incorrecta")


cadena = input("Por favor, ingresa una cadena: ")
validarCadena(cadena)
