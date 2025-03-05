from datetime import datetime, timedelta

fecha_usr = input("intoroduce una fecha con este formato DD-MM-YYYY : ")
fecha_convertida = datetime.strptime(fecha_usr,"%d-%m-%y")
print("Fecha de hoy:", fecha_usr)
nueva_fecha = fecha_convertida + timedelta(days=10)
print("Fecha sumada 10 dias: ", nueva_fecha.strptime("%d-%m-%y"))