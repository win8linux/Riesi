/* rustc -O riesi.rs */

fn main() {

    println!("Riesi: False");
    println!("Riesi?");
    
    let mut riesi = String::new();
    std::io::stdin()
        .read_line(&mut riesi)
        .unwrap();
    
    riesi = riesi
        .to_lowercase()
        .replace("\n", "");
        
    match riesi.as_ref() {
        "y" => println!("Riesi: True"),
        _   => println!("Riesi: False")
    }

}
