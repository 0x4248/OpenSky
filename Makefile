# Open sky makefile

all: add

add:
	python3 tools/add.py
	bash tools/process.sh