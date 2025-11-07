// Feito por Guilherme Aleixo

#include <stdio.h>
#include <stdlib.h>
#define MAX_NUM 100001 // includes 100000
#define BITSET_SIZE ((MAX_NUM / 8) + 1) // 8 bits per int + 1 to get size 
unsigned char bitset[BITSET_SIZE];
void add(int num) {
    bitset[num / 8] |= (1 << (num % 8));
}
void rmv(int num) {
    bitset[num / 8] ^= (1 << (num % 8));
}
int contains(int num) {
    return bitset[num / 8] & (1 << (num % 8));
}
int main() {
    int sequence_size, largest = 0, start = 0;
    scanf("%d", &sequence_size);
    int* sequence = (int*) malloc(sizeof(int) * sequence_size);
    for (int i = 0; i < sequence_size; i++) scanf("%d", sequence+i);
    for (int i = 0; i < sequence_size; i++) {
        while (contains(sequence[i])) {
            rmv(sequence[start]);
            start++;
        }
        add(sequence[i]);
        if (i-start + 1 > largest) largest = i - start + 1;
    }
    printf("%d", largest);
    return 0;
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.029s