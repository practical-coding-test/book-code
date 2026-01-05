// https://www.acmicpc.net/problem/15650
#include<iostream>
#include<vector>

using namespace std;

int N, M;
void combination(const vector<int> &data, vector<int> &res, int index) {
    // base case: 
    // 1. m개의 데이터 선택
    // 2. index가 마지막에 도달
    if((int)res.size() == M) {
        for(int i: res) {
            cout << i << ' ';
        }
        cout << '\n';
        return;
    }
    if(index == (int)data.size()) return;

    // general case
    // 1. index번 데이터 선택
    res.push_back(data[index]);
    combination(data, res, index + 1);
    res.pop_back();

    // 2. index번 데이터 선택하지 않음
    combination(data, res, index + 1);
}

int main() {
    // 빠른 입출력을 위해 사용합니다.
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    vector<int> data, res;
    for(int i = 0; i < N; ++i) {
        data.push_back(i + 1);
    }
    combination(data, res, 0);

    return 0;
}
