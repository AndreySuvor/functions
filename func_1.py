n = int(input())
spisok = []
result = []
for i in range(n):
    x = input()
    spisok.append(x)
spisok = sorted(spisok)
print(*sorted(spisok, key=lambda x: sum([ord(i) - ord('A') for i in x.upper()])), sep='\n')