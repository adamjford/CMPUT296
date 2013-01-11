/*
    Queue of int, implemented by a circular buffer in array
*/

#ifndef _queue_h
#define _queue_h

/* queue Abstract Data Type

 list points to an array that contains the elements in queue

 length stores the number of items currently in the queue

 max_length stores the total space allocated for the queue list

 head_index stores the index of the current head of the list,
 	which changes as items are removed from the list

 Invariant:  The head of the queue starts at position list[head_index],
    and goes up to position list[head_index + length -1].  In the
    event that head_index + length -1 > max_length-1, the list wraps
    around to position 0.

    Thus the current items in the queue are at positions
        head_index, head_index+1, ..., max_length-1, 
            0, ..., (length-1) % max_length
*/
typedef struct {
    int *list;
    int length;
    int max_length;
    int head_index;
} queue;

void initializeQueue(queue *q, int size_hint);
int length(queue *q);
void addElement(queue *q, int val);
int removeElement(queue *q);
int getElement(queue *q, int index);

#endif
