#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 7;

int n, m;
int ans[N];

int last[N];
vector <int> G[N];
vector <int> in[N];

int main(){
	scanf("%d %d", &n, &m);
	for(int i = 1; i <= m; ++i){
		int u, v;
		scanf("%d %d", &u, &v);
		
		G[u].push_back(v);
		G[v].push_back(u);
	}
	
	for(int i = 1; i <= n; ++i){
		int color;
		scanf("%d", &color);

		in[color].push_back(i);
		if(color > n){
			puts("-1");
			exit(0);
		}
	}
	
	vector <int> result;
	for(int i = 1; i <= n; ++i){
		for(auto u: in[i]){//i번째 color에 대항하는 각각의 blog u
			for(auto v: G[u])//u번 blog의 이웃 v
				last[ans[v]] = u;//d
			
			ans[u] = 1;
			while(last[ans[u]] == u)
				++ans[u];
			
			if(ans[u] != i){
				puts("-1");
				exit(0);
			}
			
			result.push_back(u);
		}
	}
	
	for(int i = 0; i < n; ++i)
		printf("%d%c", result[i], i == n - 1 ? '\n' : ' ');
	return 0;
}