def ancien_cipher(n):
    code = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                code += f'{i}{j}'
    return code

for n in range(3, 20):
    code = ancien_cipher(n)
    print(f'{n} - {code}')