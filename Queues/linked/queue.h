/*
    Queue of int, implemented by a linked list
*/
#ifndef _queue_h
#define _queue_h

/*
    A linked list contains nodes which hold the information for 
    that node (val) and the pointer to the next node in the 
    list (next).

    When next is 0 (null pointer) there is no following cell.
*/
typedef struct node {
    int val;
    struct node *next;
} node;

/*
    The queue is implemented by keeping a pointer to the head 
    node of a linked list.  To make adding nodes to the queue 
    efficient, we also have a pointer to the tail node of the 
    list.

    A queue is manipulated by passing around a pointer to its 
    queue struct.
*/
typedef struct {
    node *head;
    node *tail;
    int length;
} queue;

void initializeQueue(queue *q, int size_hint);
int length(queue *q);
void addElement(queue *q, int val);
int removeElement(queue *q);
int getElement(queue *q, int index);

#endif
