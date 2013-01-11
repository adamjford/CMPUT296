CFLAGS = -std=gnu99 -Wall -Werror

all : testq

# the queue implementation depends on the header also
queue.o : queue.c queue.h

# testq also depends on the queue library
testq : queue.o 

clean :
	rm -f queue.o testq
