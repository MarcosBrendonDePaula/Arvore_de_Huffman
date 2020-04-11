#include <iostream>
#include <fstream>
#include <map>
using namespace std;
map<int,char> Frequencias;

void CarreFrequenciasArq(string arquivo){
    map<char,int> TFrequencias;
    fstream Arquivo;
    Arquivo.open(arquivo);
    string temp;
    while(getline(Arquivo,temp)){
        for(auto x :temp){
            cout<<x;
            TFrequencias[x]++;
        }
    }
    for(auto i :TFrequencias){
        Frequencias[i.second]=i.first;
    }
}

int main(){
    CarreFrequenciasArq("arquivo.txt");
    for(auto i:Frequencias){
        cout<<i.first<<":"<<i.second<<endl;
    }
    return 0;
}