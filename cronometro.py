import datetime
import time

hora_actual = datetime.datetime.now()

time.sleep(3)

hora_fin = datetime.datetime.now() - hora_actual

print(hora_fin)