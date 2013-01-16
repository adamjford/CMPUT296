CFLAGS = -std=gnu99 -Wall -Werror

all : testhash

# the hashtable implementation depends on the header also
hashtable.o : hashtable.c hashtable.h

# testhash also depends on the hashtable library
testhash : testhash.c hashtable.o 
	$(CC) $(CFLAGS) testhash.c hashtable.o -o testhash

clean :
	rm -f hashtable.o testhash
