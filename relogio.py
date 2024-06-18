from datetime import datetime, timedelta


hora = int(input())
minuto = int(input())
segundo = int(input())
tempo_adiado = int(input())

tempo_real = datetime(2024, 6, 13, hora, minuto, segundo)

adiada = timedelta(seconds=tempo_adiado)

hora_nova = tempo_real + adiada

print(hora_nova.hour)
print(hora_nova.minute)
print(hora_nova.second)