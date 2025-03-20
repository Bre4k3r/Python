T = [-10, -8, 0, 1, 2, 5, -2, -4]
T.sort()

x = len(T)
x-=1

print(f'A menor temperatura é: {T[0]}')
print(f'A maior temperatura é: {T[x]}')
print(f'A média é: {sum(T)/len(T)}')