# Open sky makefile
# A repository of open source sky images.
# Github: https://www.github.com/0x4248/opensky
# Licence: Unlicense
#
# Prequisites:
# 1. make
# 2. Python3
# 3. ffmpeg

all: add

add:
	python3 tools/add.py
	bash tools/process.sh

clean:
	rm -rf tmp