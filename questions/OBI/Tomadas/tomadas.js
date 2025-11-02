// Feito por Brasilicio Henrique

var tomada, soma = 0;

for (var i = 0; i < 4; i++) {
    scanf("%d", "tomada");
    if (i === 0) soma += tomada;
    else soma += tomada - 1;
}

printf("%d\n", soma);

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.051s