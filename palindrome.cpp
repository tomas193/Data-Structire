#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
void c_method();
void cpp_method();

int main(){
    c_method();
    cpp_method();
}

void cpp_method(){
    cout<<"\ntype a word: ";
    string word;
    getline(cin,word);
    int size=word.size();
    cout<<"C++: ";
    for(int i=0;i<size;++i){
        if(word[i]!=word[size-i-1]){
            cout<<"not palindrome"<<endl;
            return;
        }
    }
    cout<<"word is palindrome"<<endl;
}

void c_method(){
    printf("type a word: ");
    int word[50];
    int c,count;
    count=0;
    while((c=getchar())!='\n'){
        if (c!=' '){
            word[count]=c;
            ++count;
        }
    }
    printf("C: ");
    for(int i=0;i<count;++i){
        if(word[i]!=word[count-i-1]){
            printf("not palindrome");
            return;
        }
    }
    printf("word is palindrome");
}