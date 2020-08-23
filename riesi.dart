import 'dart:io';

void main() {
  String frog = stdin.readLineSync();
  String ribbit = frog.toLowerCase();
  
  if (ribbit == "riesi") {
    stdout.writeln(ribbit);
  } else {
    stdout.writeln("not riesi");
  }
}
