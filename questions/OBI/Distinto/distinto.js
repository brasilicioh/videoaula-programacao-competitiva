// Feito por Brasilicio Henrique

var n;
scanf("%d", "n");

var I = [], num;
for (var i = 0; i < n; i++) {
    scanf("%d", "num");
    I.push(num);
}

var interval = new Set();
var start = 0, maxInterval = 0;

for (var end = 0; end < n; end++) {
    while (interval.has(I[end])) {
        interval.delete(I[start]);
        start++;
    }
    interval.add(I[end]);
    maxInterval = Math.max(maxInterval, end - start + 1);
}

printf("%d\n", maxInterval);

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.11s