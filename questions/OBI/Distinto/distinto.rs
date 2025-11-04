// Feito por Guilherme Aleixo

use std::collections::HashSet;

fn main() {
    let stdin = std::io::stdin();

    let mut n = String::new();
    stdin.read_line(&mut n).unwrap();

    let n: usize = n.trim().parse().unwrap();

    let mut i = vec![0; n];
    let mut interval = HashSet::new();


    for index in 0..i.len() {
        let mut number = String::new();

        stdin.read_line(&mut number).unwrap();
        let number = number.trim().parse().unwrap();

        i[index] = number;
    };

    let mut max_interval = 0;
    let mut start = 0;

    for end in 0..i.len() {
        while interval.contains(&i[end]) {
            interval.remove(&i[start]);
            start += 1;
        }

        interval.insert(&i[end]);
        max_interval = std::cmp::max(max_interval, end - start + 1);
    }

    println!("{max_interval}");
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.039s;