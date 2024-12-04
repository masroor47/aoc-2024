#include <cmath>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

int part1(const std::vector<std::string> &lines) {
    int total = 0;
    std::string key = "XMAS";
    std::string key_backwards = "SAMX";

    // horizontal search
    for (int r = 0; r < lines.size(); r++) {
        std::string line = lines[r];
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
    }

    // vertical search
    for (int c = 0; c < lines[0].size(); c++) {
        std::string line = "";
        for (int r = 0; r < lines.size(); r++) {
            line += lines[r][c];
        }
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            std::cout << "found match: " << line << std::endl;
            total++;
            pos += 1;
        }
        pos = 0;
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            std::cout << "found match: " << line << std::endl;
            total++;
            pos += 1;
        }
    }

    // bottom left corner
    for (int r = 0; r < lines.size(); r++) {
        std::string line = "";
        for (int i = 0; r + i < lines.size(); i++) {
            line += lines[r + i][i];
        }
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        pos = 0;
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
    }
    // top right corner
    for (int c = 1; c < lines[0].size(); c++) {
        std::string line = "";
        for (int i = 0; c + i < lines[0].size(); i++) {
            line += lines[i][c + i];
        }
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        pos = 0;
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
    }

    // bottom right corner
    for (int r = 0; r < lines.size(); r++) {
        std::string line = "";
        for (int i = 0; r + i < lines.size(); i++) {
            line += lines[r + i][lines[0].size() - 1 - i];
        }
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        pos = 0;
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        
    }
    // top left corner
    for (int c = 0; c < lines[0].size() - 1; c++) {
        std::string line = "";
        for (int i = 0; c - i >= 0; i++) {
            line += lines[i][c - i];
        }
        int pos = 0;
        while ((pos = line.find(key, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        pos = 0;
        while ((pos = line.find(key_backwards, pos)) != std::string::npos) {
            total++;
            pos += 1;
        }
        std::cout << line << std::endl;
    }

    return total;
}

int part2(const std::vector<std::string> &lines) {
    return 0;
}

int main() {
    std::ifstream file("test.txt");
    if (!file.is_open()) {
        std::cerr << "Error: could not open file" << std::endl;
        return 1;
    }

    std::vector<std::string> lines(
        std::istream_iterator<std::string>{file},
        std::istream_iterator<std::string>()
    );

    std::cout << "Part1: " << part1(lines) << std::endl;
    std::cout << "Part2: " << part2(lines) << std::endl;
}