from datetime import datetime
import pandas as pd
import json

filePath = 'RIPS SEPTIEMBRE.xlsx'
index = 0
consecutivo = 1

# df = pd.read_excel(filePath, sheet_name='Hoja 1')
df = pd.read_excel(filePath, sheet_name='US')
df = df.fillna(" ")

df2 = pd.read_excel(filePath, sheet_name='AP')
df2 = df2.fillna(" ")

# result = df.to_json(orient="split")

# -- User Attributes --#
fName = df.PRIMERNOMBRE
sName = df.SEGUNDONOMBRE
fApellido = df.PRIMERAPELLIDO
sApellido = df.SEGUNDOAPELLIDO
identify = df.NUMERODEIDENTIFICACION
typeIdentify = df.TIPODEIDENTIFICACION
age = df.EDAD
typeAge = df.UNIDADDEMEDIDAD
genere = df.SEXO
typeUsers = df.TIPODEUSUARIO
entity = df.CODIGOENTIDAD
departament = df.CODIGODELDEPARTAMENTO
municipio = df.CODIGODELMUNICIPIO
residencia = df.ZONADERESIDENCIA
# --    --   --#

# -- process Attributes --#
indentifyUser = df2.IDENTIFICACION
numAutorizacion = df2.NUMEROAUTORIZACION
ipsCode = df2.CODIGOIPS
fecha = df2.FECHAPROCEDIMIENTO
processId = df2.CODIGOPROCEDIMIENTO
ambitProcess = df2.AMBITOPROCEDIMIENTO
finalidad = df2.FINALIDAD
staff = df2.PERSONAL
diagnosis = df2.DIAGNOSTICO
diagnosisRalace = df2.DIAGNOSTICORELACIONADO
compilacion = df2.COMPLICACION
actoQuirurgico = df2.ACTOQUIRURGICO
processValue = df2.VALORPROCEDIMIENTO
# --    --   --#

content = []
rows = len(df.axes[0])
rows2 = len(df2.axes[0])

for i in range(rows):
    list = {"Tipo de identificacion": typeIdentify[i], "Identificacion": int(identify[i]), "Codigo Entidad": entity[i],
            "Tipo de Usuario": int(typeUsers[i]), "Primer Apellido": fApellido[i], "Segundo Apellido": sApellido[i],
            "Primer Nombre": fName[i], "Segundo Nombre": sName[i], "Edad": int(age[i]),
            "Unidad Medida": int(typeAge[i]),
            "Genero": genere[i], "Codigo Departamento": int(departament[i]), "Codigo Municipio": int(municipio[i]),
            "Zona Residencia": residencia[i], "Consecutivo": consecutivo, "Procedimientos": 0}
    content.append(list)
    consecutivo += 1
for k in range(rows2):
    x = int(indentifyUser[k])
    for j in range(len(content)):
        if x in content[j].values():
            content[j]["Procedimientos"] = {"Codigo IPS": str(ipsCode[k]),
                                            "Fecha procedimiento": fecha[k].to_pydatetime().strftime("%m/%d/%Y"),
                                            "Numero de Autorizacion": int(numAutorizacion[k]),
                                            "Identificador procedimiento": int(processId[k]),
                                            "Ambito de Procedimiento": int(ambitProcess[k]),
                                            "Finalidad del Procedimiento": int(finalidad[k]),
                                            "Personal": int(staff[k]),
                                            "Diagnostico": diagnosis[k],
                                            "Diagnostico Relacionado": diagnosisRalace[k],
                                            "Compilacion": compilacion[k],
                                            "Acto Quirurgico": int(actoQuirurgico[k]),
                                            "Valor Procedimiento":int(processValue[k])
                                            }
            break

with open('data.json', 'w') as file:
    json.dump(content, file, indent=4)
