SOLVE2:=$(wildcard solve2.py)
DIRNAME_FULL:=$(shell pwd)
YEAR:=$(shell dirname ${DIRNAME_FULL})
YEAR:=$(shell basename ${YEAR})
DAY:=$(shell basename ${DIRNAME_FULL})


ifeq ("${SOLVE2}", "")
	FILENAME=solve.py
else
	FILENAME=solve2.py
endif

.PHONY: solve, test, part2, solve2, test2, solve1, solve2
test:
	./${FILENAME} test.txt
solve: input.txt
	./${FILENAME} input.txt
solve1: input.txt
	./solve.py
test1:
	./solve.py test.txt
solve2: input.txt
	./solve2.py
test2:
	./solve2.py test.txt
part2: solve2.py
solve2.py:
	cp solve.py solve2.py
	code -r solve2.py
input.txt:
	@$(eval URL:=https://adventofcode.com/${YEAR}/day/${DAY}/input)
	@echo curling ${URL}
	@curl -s --cookie "${COOKIE}" ${URL} > input.txt