#include <iostream>
#include <exception>  // Para std::exception

void dividir(int a, int b) {
    if (b == 0) {
        throw std::exception();
    }
    std::cout << "Resultado: " << a / b << std::endl;
}

int main() {
    try {
        int x = 10;
        int y = 0; 

        dividir(x, y);
    } catch (const std::exception& e) {  // Captura una excepción de tipo std::exception
        std::cout << "Se produjo una excepción: " << e.what() << std::endl;
    }

    return 0;
}
