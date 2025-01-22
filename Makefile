
CC = gcc
CFLAGS = -g
SRC = $(wildcard src/*.c) $(wildcard libs/WiTUI/src/*.c)
INCLUDES = -I. -Ilibs/WiTUI/include -Ilibs/WiTUI/submodules/WiTesting
LIBS = -Llibs/WiTUI/src 
OBJ = $(SRC:.c=.o)
OUT = build/app

# Targets
all: $(OUT)

$(OUT): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) $(INCLUDES) $(LIBS) -o $(OUT)

%.o: %.c
	$(CC) $(CFLAGS) -c $< $(INCLUDES) -o $@

clean:
	rm -f $(OBJ) $(OUT)

# .PHONY: all clean

