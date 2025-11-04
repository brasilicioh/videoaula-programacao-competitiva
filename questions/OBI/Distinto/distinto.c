// Feito por Guilherme Aleixo

#include <stdio.h>
#include <stdlib.h>

#define MAX_NUM 10001 // includes 10000
#define BITSET_SIZE ((MAX_NUM / 8) + 1) // 8 bits per int + 1 to get size 

unsigned char bitset[BITSET_SIZE];

void add(int num) {
    bitset[num / 8] |= (1 << (num % 8));
}

void rmv(int num) {
    // assumes bit is already set
    bitset[num / 8] ^= (1 << (num % 8));
}

int contains(int num) {
    return bitset[num / 8] & (1 << (num % 8));
}


int main() {
    int sequence_size;
    scanf("%d", &sequence_size);

    int* sequence = (int*) malloc(sizeof(int) * sequence_size);

    // read numbers into the array
    for (int i = 0; i < sequence_size; i++) {
        scanf("%d", sequence+i);
    }

    int largest = 0, start = 0;

    for (int i = 0; i < sequence_size; i++) {
        while (contains(sequence[i])) {
            rmv(sequence[start]);
            start++;
        }

        add(sequence[i]);
        if (i-start + 1 > largest) {
            largest = i - start + 1;
        }
    }

    printf("%d", largest);

    // no leaky memory
    free(sequence);

    return 0;
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.11s