skills = [int(x) for x in input().split()]

equipe1 = skills[0]+skills[3]
equipe2 = skills[1]+skills[2]

ans = abs(equipe1 - equipe2)

print(ans)
