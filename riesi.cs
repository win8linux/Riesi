/* dotnet script riesi.cs */
bool   reisi = false;
string input;

Console.WriteLine($"Reisi: {reisi.ToString()}");
Console.Write("Reisi?");

input = Console.ReadLine().ToLower();
reisi = (input == "y");

Console.WriteLine($"Reisi: {reisi.ToString()}");