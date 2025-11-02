// Feito por Brasilicio Henrique

#include <iostream>

int main() {
    int T[4], sum = 0;

    for (int i = 0; i < 4; ++i) {
        std::cin >> T[i];
    }
    for (int i = 0; i < 4; ++i) {
        sum += T[i]-1;
    }

    sum += 1;
    std::cout << sum << "\n";
    return 0;
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.03s