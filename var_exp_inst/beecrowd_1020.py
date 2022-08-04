total_dias = int(input())

anos = total_dias//365
meses_dias = total_dias%365

meses = meses_dias//30
dias = meses_dias%30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
