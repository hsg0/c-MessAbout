// building a calculator using c++14
#include <iostream>
using namespace std;



int main(){

    char op;
    double num1;
    double num2;
    double result;

    std::cout << "*************Calculator*************" << std::endl;

    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter operator (+, -, *, /): ";
    std::cin >> op;

    std::cout << "Enter second number: ";
    std::cin >> num2;

    switch(op){

        case '+':
            result = num1 + num2;
            std::cout << "Result: " << result << std::endl;
            break;

        case '-':
            result = num1 - num2;
            std::cout << "Result: " << result << std::endl;
            break;

        case '*':
            result = num1 * num2;
            std::cout << "Result: " << result << std::endl;
            break;

        case '/':
            if(num2 != 0){
                result = num1 / num2;
                std::cout << "Result= " << result << std::endl;
            break;
            } else {
                std::cout << "Error: Division by zero is not allowed." << std::endl;
            }
            break;

        default:
            std::cout << "Error: Invalid operator." << std::endl;
            break;
        
    }
}