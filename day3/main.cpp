#include <cmath>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

enum class State {
    NORMAL,
    SAW_M,
    SAW_MU,
    SAW_MUL,
    SAW_OPEN,
    SAW_FIRST,
    SAW_COMMA,
    SAW_SECOND,
};

int part1(const std::string &content, int start_i, int end_i) {
    int total = 0;
    State curr_state = State::NORMAL;

    std::string first, second;
    for (int i = start_i; i < end_i; i++) {
        switch (curr_state) {
            case State::NORMAL:
                if (content[i] == 'm') {
                    curr_state = State::SAW_M;
                }
                break;
            case State::SAW_M:
                if (content[i] == 'u') {
                    curr_state = State::SAW_MU;
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_MU:
                if (content[i] == 'l') {
                    curr_state = State::SAW_MUL;
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_MUL:
                if (content[i] == '(') {
                    curr_state = State::SAW_OPEN;
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_OPEN:
                if (isdigit(content[i])) {
                    curr_state = State::SAW_FIRST;
                    first = content[i];
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_FIRST:
                if (isdigit(content[i])) {
                    first += content[i];
                } else if (content[i] == ',') {
                    curr_state = State::SAW_COMMA;
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_COMMA:
                if (isdigit(content[i])) {
                    curr_state = State::SAW_SECOND;
                    second = content[i];
                } else {
                    curr_state = State::NORMAL;
                }
                break;
            case State::SAW_SECOND:
                if (isdigit(content[i])) {
                    second += content[i];
                } else if (content[i] == ')') {
                    total += atoi(first.c_str()) * atoi(second.c_str());
                    curr_state = State::NORMAL;
                } else {
                    curr_state = State::NORMAL;
                }
                break;
        }
    }
    return total;
}

int part2(const std::string &content) {

    int total = 0;


    return total;
}

int main() {
    std::ifstream file("input.txt");
    if (!file.is_open()) {
        std::cerr << "Could not open file" << std::endl;
        return 1;
    }

    std::string content((std::istreambuf_iterator<char>(file)), 
                    std::istreambuf_iterator<char>());

    // part 1
    std::cout << "Part 1: " << part1(content, 0, content.size()) << std::endl;

    // part 2
    std::cout << "Part 2: " << part2(content) << std::endl;
}