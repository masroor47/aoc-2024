
#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream file("input.txt");
    std::vector<int> left;
    std::vector<int> right;
    int l, r;
    while (file >> l >> r) {
        left.push_back(l);
        right.push_back(r);
    }

    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    int diff = 0;
    for (int i = 0; i < left.size(); i++) {
        diff += abs(left[i] - right[i]);
    }
    std::cout << "Total difference: " << diff << std::endl;

    // Part 2
    std::unordered_map<int, int> freq;
    for (int n : right) {
        freq[n]++;
    }

    long long sum = 0;
    for (int n : left) {
        sum += n * freq[n];
    }
    std::cout << "Total sum: " << sum << std::endl;
}