#include<iostream>
#include<stdio.h>
using namespace std;

void hello_world(){
	cout << "hello world" << endl;   
}
// g++ hello_world.cpp

int main(){
    hello_world();
	int a;
	cout << "请输入整数" << endl;
	cin >> a; 
	int *p=&a;
	cout << p << endl << *p << endl;
	cout << *&p << endl << &p << endl;
	return 0;
}

