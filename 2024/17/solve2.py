#!/usr/bin/env python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as fh:
    lines = [line.strip() for line in fh.readlines()]

regAorig = int(lines.pop(0).split(":")[1].strip())
regBorig = int(lines.pop(0).split(":")[1].strip())
regCorig = int(lines.pop(0).split(":")[1].strip())
# print(regA, regB, regC)

program = [int(x) for x in lines[1].split(":")[1].strip().split(",")]
# print(program)


def run_program(regA, regB, regC, program):
    def get_combo_operand(opperand: int) -> int:
        # Combo operands 0 through 3 represent literal values 0 through 3.
        # Combo operand 4 represents the value of register A.
        # Combo operand 5 represents the value of register B.
        # Combo operand 6 represents the value of register C.
        # Combo operand 7 is reserved and will not appear in valid programs.
        if opperand < 4:
            return opperand
        elif opperand == 4:
            return regA
        elif opperand == 5:
            return regB
        elif opperand == 6:
            return regC
        else:
            assert opperand == 0, "This should never happen"

    pnt = 0
    out = []
    # print(regA, regB, regC, out)
    while pnt < len(program):
        # print(pnt)
        op_code = program[pnt]
        operand = program[pnt + 1]

        # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
        if op_code == 0:
            operand = get_combo_operand(operand)
            regA //= 2**operand
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
        elif op_code == 1:
            regB ^= operand
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        elif op_code == 2:
            operand = get_combo_operand(operand)
            regB = operand % 8
        # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        elif op_code == 3:
            if regA != 0:
                pnt = operand
                # print(pnt, regA, regB, regC, out)
                continue  # skip the pnt += 2
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
        elif op_code == 4:
            regB ^= regC
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        elif op_code == 5:
            operand = get_combo_operand(operand)
            operand = operand % 8
            out.append(operand)
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        elif op_code == 6:
            operand = get_combo_operand(operand)
            regB = regA // 2**operand
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
        elif op_code == 7:
            operand = get_combo_operand(operand)
            regC = regA // 2**operand

        pnt += 2
        # print(regA, regB, regC, out)
    return out


progam_len = len(program)
digit = -1
i = 8 ** (progam_len + digit)
while True:
    out = run_program(i, regBorig, regCorig, program)
    print(i, out)
    if out == program:
        print(i, out)
        break
    while out[digit] == program[digit]:
        digit -= 1
    if out[digit] != program[digit]:
        print(progam_len + digit)
        i += 8 ** (progam_len + digit)

# 281474976710656 That's not the right answer; your answer is too high
# 202322348616234 That's not the right answer.
# 202322348616234
# 202322348616237
# 202322348616239
# 202322348616237
