CC = gcc
SRC = src/main.c $(wildcard libs/WiTUI/src/*.c)
INCLUDES = -Ilibs/WiTUI/include -Ilibs/WiTUI/submodules/WiTesting
OBJ = $(SRC:.c=.o)
OUT = build/app

# Targets
all: $(OUT)

$(OUT): $(OBJ)
	$(CC) $(OBJ) $(INCLUDES) -o $(OUT)

%.o: %.c
	$(CC) -c $< $(INCLUDES) -o $@

clean:
	rm -f $(OBJ) $(OUT)

.PHONY: all clean

