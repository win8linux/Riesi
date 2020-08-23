Dim riesi As Boolean
Dim input As String

Console.WriteLine($"Riesi: {riesi.ToString()}")
Console.Write("Riesi?")

input = Console.ReadLine().ToLower()
riesi = (input = "y")

Console.WriteLine($"Riesi: {riesi.ToString()}")
