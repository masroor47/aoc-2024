#include <cmath>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

int get_num_issues(const std::vector<int> line) {
    std::vector<int> diffs(line.size() - 1);
    for (int i = 0; i < line.size() - 1; i++) {
        diffs[i] = line[i] - line[i + 1];
    }

    int num_diff_fails = 0;
    int dir = diffs[0] > 0 ? 1 : -1;
    bool monotonic_fail = false;
    for (int i = 0; i < diffs.size(); i++) {
        // monotonicity check
        if (dir == 1 && diffs[i] < 0) monotonic_fail = true;
        else if (dir == -1 && diffs[i] > 0) monotonic_fail = true;

        // neighbor difference within 1 and 3
        if (abs(diffs[i]) < 1 || abs(diffs[i]) > 3) {
            num_diff_fails++;
        }
    }
    // treating monotonic fail as 1 is not best idea
    // sometimes there is one diff fail and one monotonic fail but it's fixable with one removal
    return num_diff_fails + monotonic_fail;
}

int main() {
    std::ifstream file("input.txt");
    std::vector<std::vector<int>> lines;
    std::string line;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::vector<int> nums;
        int n;
        while (ss >> n) {
            nums.push_back(n);
        }
        lines.push_back(nums);
    }

    // part 1
    int sum = 0;
    int num_issues;
    for (int r = 0; r < lines.size(); r++) {
        num_issues = get_num_issues(lines[r]);
        sum += num_issues == 0;
    }
    std::cout << sum << std::endl;

    // part 2
    sum = 0;
    for (int r = 0; r < lines.size(); r++) {
        num_issues = get_num_issues(lines[r]);
        if (num_issues == 0) {
            sum++;
            continue;
        }
        if (num_issues > 2) continue;

        // try removing each number and checking
        for (int i = 0; i < lines[r].size(); i++) {
            std::vector<int> copy(lines[r]);
            copy.erase(copy.begin() + i);
            if (get_num_issues(copy) == 0) {
                sum++;
                break;
            }
        }
    }
    std::cout << sum << std::endl;
}
