// https://www.acmicpc.net/problem/13549
#include<iostream>
#include<queue>

using namespace std;

int main() {
    // 빠른 입출력을 위해 사용합니다.
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    // 도착한 지점이 없으므로 매우 큰 값을 초기에 할당
    vector<int> t(100001, 0x3f3f3f3f);

    queue<int> Q;
    Q.push(N);
    t[N] = 0;

    // queue 자료 구조에 데이터가 있을 경우 True
    while(!Q.empty()) {
        int now = Q.front(); Q.pop();
        // 순간이동
        if(now * 2 < (int)t.size() && t[now * 2] > t[now]) {
            t[now * 2] = t[now];
            Q.push(now * 2);
        }
        // 이동
        for(int move: {1, -1}) {
            int next = now + move;
            if(0 <= next && next < (int)t.size() && t[next] > t[now] + 1) {
                t[next] = t[now] + 1;
                Q.push(next);
            }
        }
    }
    cout << t[K];

    return 0;
}
