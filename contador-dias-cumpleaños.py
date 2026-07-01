#Importar modulos
import datetime, bday_messages
#Crear objetos
today = datetime.date.today()
next_birthday = datetime.date(2026,12,2)
#restar fechas
days_away= (next_birthday - today).days
#
if next_birthday == today:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')

