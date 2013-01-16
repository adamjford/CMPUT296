/*
    Queue of int, implemented by a linked list

    Names are prefixed with q_ to indicate methods that belong to the
    queue ADT.
*/
#ifndef _queue_h
#define _queue_h

/*
    A linked list contains nodes which hold the information for 
    that node (val) and the pointer to the next node in the 
    list (next).

    When next is 0 (null pointer) there is no following cell.
*/
typedef struct q_node_t {
    int val;
    struct q_node_t *next;
} q_node_t;

/*
    The queue is implemented by keeping a pointer to the head 
    node of a linked list.  To make adding nodes to the queue 
    efficient, we also have a pointer to the tail node of the 
    list.

    A queue is manipulated by passing around a pointer to its 
    queue struct.
*/
typedef struct {
    q_node_t *head;
    q_node_t *tail;
    int length;
} q_instance_t;

/*  
    A queue is a pointer to a queue_instance  
*/
typedef q_instance_t *queue;

/*
    Constructor: create a queue instance and return a queue 
    (i.e. a pointer to the struct).
*/

queue q_create(int size_hint);

/*
    Destructor: free up the storage used by the queue.
*/
void q_destroy(queue q);

/*
    Get the current length of the queue
*/
int q_length(queue q);

/*
    Add the element val to the tail of the queue q
*/
void q_add(queue q, int val);

/*
    Remove and return the element at the head of queue q

    Pre-condition: q_length(q) > 0
*/
int q_remove(queue q);

/*
    Get the element of the queue at position index,
    where the head of the queue is position 0, and the
    tail is at position q_length(q)-1
*/
int q_get_item(queue q, int index);

/*
    Return the element at index in the queue, and deletes it from inside 
    the queue. 
*/
int q_delete_item(queue q, int index);

#endif
