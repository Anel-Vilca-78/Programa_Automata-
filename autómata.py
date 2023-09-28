from flask import Flask, render_template, request

app = Flask(__name__)


def validarCadena(cadena):
    array = []
    try:
        if len(cadena) < 12:
            array.append("→ q0 → ")
            if cadena[0] == "S":
                array.append("q1 → ")
                if cadena[1] == "A":
                    array.append("q2 → ")
                    if cadena [2] == "E":
                        array.append("q3 → ")
                        if cadena [3] == " ":
                            array.append("q4 → ")

                        #Aqui inicia el 1er switch
                        
                        #CADENA SAE 0W-20
                            if cadena[4] =="0":
                                array.append("q7 → ")
                                if cadena[5] == "W":
                                    array.append("q18 → ")
                                    if cadena [6] == "-":
                                        array.append("q20 → ")
                                        if cadena [7] == "2":
                                            array.append("q21 → ")
                                            if cadena [8] == "0":
                                                array.append("q22")
                                                array.append("cadena correcta")
                                            else:
                                                array.append("q21 falla")
                                        else:
                                            array.append("q20 falla")
                                    else:
                                        array.append("q18 falla")
                                else:
                                    array.append("q7 falla")
                                
                            #CADENAS SAE 5W-30 ||40||50
                            elif cadena[4] =="5": 
                                array.append("q5 → ")
                                if cadena[5] == "W":
                                    array.append("q19 → ")
                                    if cadena[6] == "-":
                                        array.append("q23 → ")
                                        #Cadena SAE 5W-30
                                        if cadena[7] == "3":
                                                array.append("q24 → ")
                                                if cadena[8] == "0":
                                                    array.append("q27 ")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q24 falla")
                                            #Cadena SAE 5W-40
                                        elif cadena[7] =="4":
                                                array.append("q25 → ")
                                                if cadena[8] == "0":
                                                    array.append("q27")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q25 falla")
                                            #Cadena SAE 5W-50
                                        elif cadena[7] =="5":
                                                array.append("q26 → ")
                                                if cadena[8] == "0":
                                                    array.append("q27")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q26 falla")
                                        else:
                                            array.append("q23 falla")
                                    else:
                                        array.append("q19 falla")
                                else:
                                    array.append("q5 falla")

                            #CADENAS de iniciales SAE 10W- ||  SAE 15W
                            elif cadena[4] =="1":
                                array.append("q6 → ")
                                if cadena[5] == "0":
                                    array.append("q9 → ")
                                    if cadena[6] == "W":
                                        array.append("q14 → ")
                                        if cadena[7] == "-":
                                            array.append("q15 → ")
                                            #Cadena SAE 10W-30
                                            if cadena[8] == "3":
                                                array.append("q30 → ")
                                                if cadena[9] == "0":
                                                    array.append("q33")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q30 falla")
                                            #Cadena SAE 10W-40
                                            elif cadena[8] =="4":
                                                array.append("q31 → ")
                                                if cadena[9] == "0":
                                                    array.append("q33")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q31 falla")
                                            #Cadena SAE 10W-50
                                            elif cadena[8] =="5":
                                                array.append("q32 → ")
                                                if cadena[9] == "0":
                                                    array.append("q33")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q32 falla")

                                            else:
                                                array.append("q15 falla")
                                        else:
                                            array.append("q14 falla")
                                    else:
                                        array.append("q9 falla")

                                #CADENA SAE 15W-40
                                elif cadena[5] == "5":
                                    array.append("q10 → ")
                                    if cadena[6] == "W":
                                        array.append("q11 → ")
                                        if cadena[7] == "-":
                                            array.append("q13 → ")
                                            if cadena[8] == "4":
                                                array.append("q34 → ")
                                                if cadena[9] == "0":
                                                    array.append("q35")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("34 falla")
                                                array.append("q13 falla")
                                        else:
                                            array.append("q11 falla")
                                    
                                    else:
                                        array.append("q10 falla")
                                    
                                else:
                                    array.append("q6 falla")

                            #CADENA SAE 20W-50
                            elif cadena[4] =="2":
                                array.append("q8 → ")
                                if cadena[5] == "0":
                                    array.append("q12 → ")
                                    if cadena[6] == "W":
                                        array.append("q16 → ")
                                        if cadena[7] == "-":
                                            array.append("q17 → ")
                                            if cadena[8] == "5":
                                                array.append("q28 → ")
                                                if cadena[9] == "0":
                                                    array.append("q29")
                                                    array.append("cadena correcta")
                                                else:
                                                    array.append("q28 falla")
                                            else:
                                                array.append("q17 falla")
                                        else:
                                            array.append("q16 falla")
                                    else:
                                        array.append("q12 falla")
                                    
                                else:
                                    array.append("q8 falla")
                            else:
                                array.append("q4 falla")
                        else:
                            array.append("q3 falla")
                    else:
                        array.append ("q2 falla")
                else:
                    array.append("q1 falla")
            else:    
                array.append("q0 falla")
        else: 
            array.append("La cadena es muy larga")
        return array
    except:
        array.append("La cadena es incorrecta")
        return array

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    cadena = ""
    if request.method == 'POST':
        cadena = request.form['cadena']
        resultado = validarCadena(cadena)
        if "falla" in resultado [-1]:
            resultado.append("La cadena es incorrecta")

    return render_template('index.html', resultado=resultado, cadena=cadena)

if __name__ == '__main__':
    app.run(debug=True)