#include <iostream>
#include <regex>
#include <vector>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N,M;
    cin>>N>>M;
    vector<string> words(N);
    for(int i=0;i<N;i++){
        cin>>words[i];
    }
    for(int j=0;j<M;j++){
        int cnt=0;
        string pattern;
        cin>>pattern;
        pattern.replace(pattern.begin(),pattern.end(),".",".?");
        regex p(pattern);
        for(auto word:words){
            if(regex_match(word,p)){
                cnt+=1;
            }
        }
        cout<<cnt;
    }
    return 0;
}
