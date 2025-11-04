// Feito por Guilherme ALeixo

fn main() {
    let mut line = String::new();

    std::io::stdin().read_line(&mut line).expect("Failed to read line");

    let inputs: Vec<u32> = line.split_whitespace()
        .map(|x| x.parse().expect("Value was not integer"))
        .collect();

    let result: u32 = inputs.iter().sum();

    let result = result - 3;

    println!("{result}");
}

// Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
// Max runtime: 0.018s