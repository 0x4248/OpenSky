# Open sky makefile
# A repository of open source sky images.
# Github: https://www.github.com/awesomelewis2007/opensky

all: add

add:
	python3 tools/add.py
	bash tools/process.sh