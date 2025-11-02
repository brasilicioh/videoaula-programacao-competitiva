# Feito por Kaio Henrique

n = int(input())

I = []
for i in range(n):
    I.append(int(input()))


interval = set()
max_interval = 0, start = 0

for end in range(len(I)):
    while I[end] in interval:
        interval.remove(I[start])
        start += 1
    interval.add(I[end])
    size = end - start + 1
    max_interval = max(max_interval, size)
    
print(max(max_interval, size))

# Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
# Max runtime: 0.27s