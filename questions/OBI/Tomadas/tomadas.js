// Feito por Brasilicio Henrique

var t, sum = 0;

for (var i = 0; i < 4; i++) {
    scanf("%d", "t");
    if (i === 0) sum += t;
    else sum += t - 1;
}

printf("%d\n", sum);

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.051s