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

/*
    Take a declared empty queue structure and initialize it.

    Warning: Do not call on an existing queue.  Will get a
    memory leak.
*/
void initializeQueue(queue *q, int size_hint);

/*
    Get the current length of the queue
*/
int length(queue *q);

/*
    Add the element val to the tail of the queue q
*/
void addElement(queue *q, int val);

/*
    Remove and return the element at the head of queue q

    Pre-condition: q->length > 0
*/
int removeElement(queue *q);

/*
    Get the element of the queue at position index,
    where the head of the queue is position 0, and the
    tail is at position length(q)-1
*/
int getElement(queue *q, int index);

/*
    Return the element at index in the queue, and deletes it from inside 
    the queue. 
*/
int deleteElement(queue *q, int index);

#endif
