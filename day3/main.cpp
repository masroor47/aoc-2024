#include <cmath>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

enum class MulState {
    NORMAL,
    SAW_M,
    SAW_MU,
    SAW_MUL,
    SAW_OPEN,
    SAW_FIRST,
    SAW_COMMA,
    SAW_SECOND,
    MATCHED,
};

enum class ToggleState {
    NORMAL,
    SAW_D,
    SAW_DO,
    SAW_DO_OPEN,
    MATCHED_DO,
    SAW_DON,
    SAW_DON_QUOTE,
    SAW_DONT,
    SAW_DONT_OPEN,
    MATCHED_DONT,
};

int part1(const std::string &content, int start_i, int end_i) {
    int total = 0;
    MulState curr_state = MulState::NORMAL;

    std::string first, second;
    for (int i = start_i; i < end_i; i++) {
        switch (curr_state) {
            case MulState::NORMAL:
                if (content[i] == 'm') {
                    curr_state = MulState::SAW_M;
                }
                break;
            case MulState::SAW_M:
                if (content[i] == 'u') {
                    curr_state = MulState::SAW_MU;
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_MU:
                if (content[i] == 'l') {
                    curr_state = MulState::SAW_MUL;
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_MUL:
                if (content[i] == '(') {
                    curr_state = MulState::SAW_OPEN;
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_OPEN:
                if (isdigit(content[i])) {
                    curr_state = MulState::SAW_FIRST;
                    first = content[i];
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_FIRST:
                if (isdigit(content[i])) {
                    first += content[i];
                } else if (content[i] == ',') {
                    curr_state = MulState::SAW_COMMA;
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_COMMA:
                if (isdigit(content[i])) {
                    curr_state = MulState::SAW_SECOND;
                    second = content[i];
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::SAW_SECOND:
                if (isdigit(content[i])) {
                    second += content[i];
                } else if (content[i] == ')') {
                    total += atoi(first.c_str()) * atoi(second.c_str());
                    curr_state = MulState::NORMAL;
                } else {
                    curr_state = MulState::NORMAL;
                }
                break;
            case MulState::MATCHED:
                std::cerr << "Error: should not be here" << std::endl;
                break;
        }
    }
    return total;
}

struct match_result {
    int product;
    MulState mul_state;
    bool matched_do;
    bool matched_dont;
    ToggleState toggle_state;
};

struct curr_state {
    std::string first;
    std::string second;
    int product;
    MulState mul_state;
    // bool matched_do;
    // bool matched_dont;
    ToggleState toggle_state;
};

void match_keywords(curr_state &s, char c) {

    switch (s.mul_state) {
        case MulState::NORMAL:
            if (c == 'm') {
                s.mul_state = MulState::SAW_M;
            }
            break;
        case MulState::SAW_M:
            if (c == 'u') {
                s.mul_state = MulState::SAW_MU;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_MU:
            if (c == 'l') {
                s.mul_state = MulState::SAW_MUL;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_MUL:
            if (c == '(') {
                s.mul_state = MulState::SAW_OPEN;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_OPEN:
            if (isdigit(c)) {
                s.mul_state = MulState::SAW_FIRST;
                s.first = c;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_FIRST:
            if (isdigit(c)) {
                s.mul_state = MulState::SAW_FIRST;
                s.first += c;
            } else if (c == ',') {
                s.mul_state = MulState::SAW_COMMA;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_COMMA:
            if (isdigit(c)) {
                s.mul_state = MulState::SAW_SECOND;
                s.second = c;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::SAW_SECOND:
            if (isdigit(c)) {
                s.mul_state = MulState::SAW_SECOND;
                s.second += c;
            } else if (c == ')') {
                s.product = atoi(s.first.c_str()) * atoi(s.second.c_str());
                s.mul_state = MulState::MATCHED;
            } else {
                s.mul_state = MulState::NORMAL;
            }
            break;
        case MulState::MATCHED:
            std::cerr << "Error: matched mul not reset" << std::endl;
            break;
    }

    switch (s.toggle_state) {
        case ToggleState::NORMAL:
            if (c == 'd') {
                s.toggle_state = ToggleState::SAW_D;
            }
            break;
        case ToggleState::SAW_D:
            if (c == 'o') {
                s.toggle_state = ToggleState::SAW_DO;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DO:
            if (c == '(') {
                s.toggle_state = ToggleState::SAW_DO_OPEN;
            } else if (c == 'n') {
                s.toggle_state = ToggleState::SAW_DON;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DON:
            if (c == '\'') {
                s.toggle_state = ToggleState::SAW_DON_QUOTE;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DO_OPEN:
            if (c == ')') {
                s.toggle_state = ToggleState::MATCHED_DO;
                // s.matched_do = true;
                return;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DON_QUOTE:
            if (c == 't') {
                s.toggle_state = ToggleState::SAW_DONT;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DONT:
            if (c == '(') {
                s.toggle_state = ToggleState::SAW_DONT_OPEN;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::SAW_DONT_OPEN:
            if (c == ')') {
                s.toggle_state = ToggleState::MATCHED_DONT;
                // s.matched_dont = true;
                return;
            } else {
                s.toggle_state = ToggleState::NORMAL;
            }
            break;
        case ToggleState::MATCHED_DO:
            std::cerr << "Error: matched do not reset" << std::endl;
            break;
        case ToggleState::MATCHED_DONT:
            std::cerr << "Error: matched don't not reset" << std::endl;
            break;
    }
}

int part2(const std::string &content) {

    int total = 0;
    bool enabled = true;

    curr_state s = { 
        "", 
        "",
        0, 
        MulState::NORMAL, 
        ToggleState::NORMAL 
    };

    for (int i = 0; i < content.size(); i++) {
        // std::cout << content[i] << "; ";
        match_keywords(s, content[i]);
        // std::cout << "mul_state: " << (int)s.mul_state << " toggle_state: " << (int)s.toggle_state << std::endl;

        if (enabled && s.mul_state == MulState::MATCHED) {
            // std::cout << "Matched mul: " << s.product << std::endl;
            total += s.product;
            s.mul_state = MulState::NORMAL;
        } else if (s.mul_state == MulState::MATCHED) {
            s.mul_state = MulState::NORMAL;
        }

        if (s.toggle_state == ToggleState::MATCHED_DO) {
            // std::cout << "matched do, enabling" << std::endl;
            enabled = true;
            s.toggle_state = ToggleState::NORMAL;
        }

        if (s.toggle_state == ToggleState::MATCHED_DONT) {
            // std::cout << "matched don't, disabling" << std::endl;
            enabled = false;
            s.toggle_state = ToggleState::NORMAL;
        }
    }
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