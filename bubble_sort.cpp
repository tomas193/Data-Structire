#include  <iostream>
#include <random>
#include <vector>

std::vector<int> bubble_sort(std::vector<int> array);
void print_elements(std::vector<int> array);

int main(){
    std::random_device rd;  // Semilla aleatoria basada en el hardware
    std::mt19937 gen(rd()); // Generador Mersenne Twister
    std::uniform_int_distribution<> distrib(1, 100);

    std::vector<int> numbers;
    int  elements,i;
    std::cout<<"A list of random numbers will be generated."<<std::endl;
    std::cout<<"Enter number of elements: ";
    std::cin>>elements;
    for (i=0;i<elements;++i){
        numbers.push_back(distrib(gen));
    }
    print_elements(numbers);
    numbers=bubble_sort(numbers);
    print_elements(numbers);
}

std::vector<int> bubble_sort(std::vector<int> array){
    int length=array.size();
    int aux;
    for (int i=0;i<length;++i){
        for (int k=i+1;k<length;++k){
            if(array[i]>array[k]){
                aux=array[i];
                array[i]=array[k];array[k]=aux;
            }
        }
    }
    return array;
}

void print_elements(std::vector<int> array){
    std::cout<<"\nnumbers: "<<std::endl;
    for (int i=0;i<array.size();++i){
        std::cout<<array[i]<<" ";
    }
    std::cout<<"\n";
}