spisok = []
for _ in range(int(input())):
    x = input()
    spisok.append(x)
print(*sorted(spisok, key=lambda x: list(map(int, x.split('.')))), sep='\n')