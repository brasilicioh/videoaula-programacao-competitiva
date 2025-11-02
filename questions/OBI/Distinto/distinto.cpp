// Feito por Brasilicio Henrique

#include <iostream>
#include <vector>
#include <unordered_set>

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    int n;
    std::cin >> n;

    std::vector<int> I(n);
    for (int i = 0; i < n; i++) std::cin >> I[i];

    std::unordered_set<int> interval;
    int maxInterval = 0, start = 0;

    for (int i = 0; i < n; i++) {
        while (interval.count(I[i])) {
            interval.erase(I[start]);
            start++;
        }
        interval.insert(I[i]);
        maxInterval = std::max(maxInterval, i - start + 1);
    }

    std::cout << maxInterval << "\n";
    return 0;
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.029s