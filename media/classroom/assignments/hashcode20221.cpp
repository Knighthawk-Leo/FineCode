#include<bits/stdc++.h>
using namespace std;
int main(){
	//for input
	int n,m;
	cin>>n>>m;
	while(n--){
		map<string,int> m;
		for(int i=0;i<n;i++){
			string name;
			int no_of_skills;
			cin>>name>>no_of_skills;
			m.insert({name,no_of_skills});
			while(no_of_skills--){
				map<string,int> m1;
				string skill;
				int skill_level;
				m1.insert({skill,skill_level});
			}
		}
	}
	while(m--){

	}
}