
# Variables
CC = gcc
SRC = src/main.c libs/WiTUI/src/*.c
INCLUDES = -Ilibs/WiTUI/include -Ilibs/WiTUI/submodules/WiTesting
OUT = build/app

# Targets
all: $(OUT)

$(OUT):
	$(CC) $(SRC) $(INCLUDES) -o $(OUT)

clean:
	rm -f $(OUT)

.PHONY: all clean

