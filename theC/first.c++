#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int a;
	cout << "请输入整数" << endl;
	cin >> a; 
	int *p=&a;
	cout << p << endl << *p << endl;
	cout << *&p << endl << &p << endl;
	return 0;
}

