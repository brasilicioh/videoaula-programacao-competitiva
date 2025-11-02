// Feito por Brasilicio Henrique

#include <iostream>

using namespace std;

int main() {
    int T[4], sum = 0;

    for (int i = 0; i < 4; ++i) {
        cin >> T[i];
    }
    for (int i = 0; i < 4; ++i) {
        sum += T[i]-1;
    }

    sum += 1;
    cout << sum << "\n";
    return 0;
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.030s