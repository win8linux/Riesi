/* g++ -std=c++11 riesi.cpp -o riesi_cpp -pedantic -Wall -Wextra -Werror */
#include <iostream>

int main(void)
{
    bool riesi = false;
    char input;

    std::cout << "Riesi: " << (riesi ? "True" : "False") << std::endl;
    std::cout << "Riesi?";

    std::cin >> input;

    input = std::tolower(input);
    riesi = (input == 'y');

    std::cout << "Riesi: " << (riesi ? "True" : "False") << std::endl;

    return 0;
}