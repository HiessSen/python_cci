from datetime import datetime, date
now = datetime.now()
print(f"Date et heure actuelles : {now.strftime("%d/%m/%Y %H:%M:%S")}")
print(f"Date actuelle, annéee et mois : {now.strftime("%m/%Y")}")
date1 = date(2022, 3, 27)
date2 = date(2018, 12, 1)
print(date1)
print(date2)