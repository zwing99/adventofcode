SOLVE2:=$(wildcard solve2.py)

ifeq ("${SOLVE2}", "")
	FILENAME=solve.py
else
	FILENAME=solve2.py
endif

.PHONY: solve, test, part2, solve2, test2, solve1, solve2
test:
	./${FILENAME} test.txt
solve:
	./${FILENAME} input.txt
solve1:
	./solve.py
test1:
	./solve.py test.txt
solve2:
	./solve2.py
test2:
	./solve2.py test.txt
part2: solve2.py
solve2.py:
	cp solve.py solve2.py
	code -r solve2.py