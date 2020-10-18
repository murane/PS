#include <bits/stdc++.h>
#define f0r(i,n) for(int i=0; i<n; ++i)
#define f1r(i,n) for(int i=1; i<=n; ++i)
using namespace std;
using ll = long long;
#define chmax(x,y) x=max(x,y)

int a[3005][3005];
ll dp[3005][3005][4];
int getmax(int a,int b){
    if(a>=b)return a;
    else return b;
}
int main(){
    int R,C,n;
    cin>>R>>C>>n;
    f0r(i,n){
        int r,c,v;
        cin>>r>>c>>v;
        a[r][c]=v;
    }
    f1r(i,R)f1r(j,C){
        if(i==1){
            dp[i][j][0]=0;
            dp[i][j][1]=getmax(dp[i][j-1][1], dp[i][j-1][0]+a[i][j]);
            dp[i][j][2]=getmax(dp[i][j-1][2], dp[i][j-1][1]+a[i][j]);
            dp[i][j][3]=getmax(dp[i][j-1][3], dp[i][j-1][2]+a[i][j]);
        }else{
            ll tmp=0;
            for(int k=0;k<4;k++){
                tmp=max(ll(tmp),dp[i-1][j][k]);
            }
            dp[i][j][0]=tmp;
            dp[i][j][1]=getmax(dp[i][j-1][1], getmax(tmp+a[i][j],dp[i][j-1][0]+a[i][j]));
            dp[i][j][2]=getmax(dp[i][j-1][2], dp[i][j-1][1]+a[i][j]);
            dp[i][j][3]=getmax(dp[i][j-1][3], dp[i][j-1][2]+a[i][j]);
        }
    }

    ll ans=0;
    f0r(k,4) chmax(ans,dp[R][C][k]);
    cout<<ans;
    return 0;
}