package main 
  
import (
 "fmt"
 "strings"
)

func main() { 
    var frog string 
    fmt.Scanln(&frog)
    frog = strings.ToLower(frog)
    
    if frog == "riesi" {
        fmt.Print(frog)
    } else {
        fmt.Println("not riesi")
    }
}
