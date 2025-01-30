#include <iostream>

long long factorial(int number);

int main(){
    int number;
    std::cout<<"Enter a number to calculate factorial: ";
    std::cin>>number;
    std::cout<<"factorial of "<<number<<": "<<factorial(number)<<std::endl;
}

long long factorial(int number){
    long long fact=1;
    for (int i=1;i<=number;i++){
        fact = fact*i;
    }
    return fact;
}