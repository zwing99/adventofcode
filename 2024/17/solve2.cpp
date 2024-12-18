#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>

// Function to split a string by a delimiter
std::vector<std::string> split(const std::string &str, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(str);
    while (std::getline(tokenStream, token, delimiter))
    {
        tokens.push_back(token);
    }
    return tokens;
}

// Function to trim whitespace from a string
std::string trim(const std::string &str)
{
    size_t first = str.find_first_not_of(" \t\n\r");
    if (first == std::string::npos)
        return "";
    size_t last = str.find_last_not_of(" \t\n\r");
    return str.substr(first, (last - first + 1));
}

int get_combo_operand(int operand, int regA, int regB, int regC)
{
    if (operand < 4)
        return operand;
    if (operand == 4)
        return regA;
    if (operand == 5)
        return regB;
    if (operand == 6)
        return regC;
    assert(false && "This should never happen");
    return 0;
}

std::vector<int> run_program(int regA, int regB, int regC, const std::vector<int> &program)
{
    int pnt = 0;
    std::vector<int> out;

    while (pnt < program.size())
    {
        int op_code = program[pnt];
        int operand = program[pnt + 1];

        switch (op_code)
        {
        case 0:
        {
            operand = get_combo_operand(operand, regA, regB, regC);
            regA /= std::pow(2, operand);
            break;
        }
        case 1:
        {
            regB ^= operand;
            break;
        }
        case 2:
        {
            operand = get_combo_operand(operand, regA, regB, regC);
            regB = operand % 8;
            break;
        }
        case 3:
        {
            if (regA != 0)
            {
                pnt = operand;
                continue;
            }
            break;
        }
        case 4:
        {
            regB ^= regC;
            break;
        }
        case 5:
        {
            operand = get_combo_operand(operand, regA, regB, regC);
            operand %= 8;
            out.push_back(operand);
            for (size_t i = 0; i < out.size(); ++i)
            {
                if (out[i] != program[i])
                {
                    return out;
                }
            }

            break;
        }
        case 6:
        {
            operand = get_combo_operand(operand, regA, regB, regC);
            regB = regA / std::pow(2, operand);
            break;
        }
        case 7:
        {
            operand = get_combo_operand(operand, regA, regB, regC);
            regC = regA / std::pow(2, operand);
            break;
        }
        default:
            assert(false && "Invalid opcode");
        }
        pnt += 2;
    }

    return out;
}

void print_vector(const std::vector<int> &vec)
{
    for (size_t i = 0; i < vec.size(); ++i)
    {
        std::cout << vec[i];
        if (i != vec.size() - 1)
        {
            std::cout << ", ";
        }
    }
    std::cout << std::endl;
}

int main(int argc, char *argv[])
{
    std::string filename = (argc > 1) ? argv[1] : "input.txt";

    std::ifstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line))
    {
        lines.push_back(trim(line));
    }
    file.close();

    if (lines.size() < 4)
    {
        std::cerr << "Error: Insufficient lines in input file." << std::endl;
        return 1;
    }

    int regAorig = std::stoi(split(lines[0], ':')[1]);
    int regBorig = std::stoi(split(lines[1], ':')[1]);
    int regCorig = std::stoi(split(lines[2], ':')[1]);

    std::vector<int> program;
    for (const auto &str : split(split(lines[4], ':')[1], ','))
    {
        program.push_back(std::stoi(trim(str)));
    }
    std::cout << filename << std::endl;

    long int i = 20043460000;
    std::cout << INTMAX_MAX << std::endl;
    exit(0);
    while (true)
    {
        std::vector<int> out = run_program(i, regBorig, regCorig, program);
        // std::cout << i << std::endl;
        // std::cout << i % 8 << std::endl;
        // print_vector(out);

        if (out == program)
        {
            std::cout << i << std::endl;
            break;
        }
        i += 8;
        if (i % 1000 == 0)
        {
            std::cout << i << std::endl;
        }
    }

    return 0;
}
