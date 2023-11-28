#include <iostream>
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(0);
    long long suma;
    int n, liczba_testow;
 
    cin >> liczba_testow;
    while(liczba_testow--) {
        cin >> n;
        suma = 0;
        int i;
        for(i = 1; i * i < n; i++) {
            if(n % i == 0) {
                suma += i;
                suma += n / i;
            }
        }
        if(i*i == n) suma += i;
        cout << suma << endl;
    }
} 
