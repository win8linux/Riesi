﻿/* dotnet script riesi.cs */
bool   riesi = false;
string input;

Console.WriteLine($"Riesi: {riesi.ToString()}");
Console.Write("Riesi?");

input = Console.ReadLine().ToLower();
riesi = (input == "y");

Console.WriteLine($"Riesi: {riesi.ToString()}");
