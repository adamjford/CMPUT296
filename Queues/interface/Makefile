CFLAGS = -std=gnu99 -Wall -Werror

all : testq

# the queue implementation depends on the header also
queue.o : queue.c queue.h

# testq also depends on the queue library
testq : testq.c queue.o 
	$(CC) $(CFLAGS) testq.c queue.o -o testq

clean :
	rm -f queue.o testq
