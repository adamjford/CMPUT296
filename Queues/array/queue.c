/* Implementation of Queue ADT using circular list in an array */
#include "queue.h"
#include <stdlib.h>
#include <assert.h>

/* 
    Take a declared empty queue structure and initialize it.
 
    Warning: Do not call on an existing queue.  Will get a 
    memory leak.
*/
void initializeQueue(queue *q, int size_hint) {
        assert(q != 0);

	q->max_length = size_hint;
	q->length = 0;
        q->head_index = 0;
	q->list = malloc(q->max_length*sizeof(int));
        assert(q->list != 0);
    }

/* internal method to increase size of queue */
void increaseSize(queue *q, int increase) {
    int new_max_length = q->max_length + increase;

    int * bigger_list = malloc(new_max_length * sizeof(int));
    assert(bigger_list != 0);

    for (int i = 0; i < q->max_length; i++) {
        bigger_list[i] = q->list[i];
        }

    free(q->list);
    q->list = bigger_list;
    q->max_length = new_max_length;
    }


/*
    Add the element val to the tail of the queue q
*/
void addElement(queue *q, int val) {
    if (q->length == q->max_length) {
        /* double the current length of the queue */
        increaseSize(q, q->max_length);
        }

    int new_index = (q->head_index + q->length) % q->max_length;
    q->length++;

    q->list[new_index] = val;
    }

/*
    Remove and return the element at the head of queue q
     
    Pre-condition: q->length > 0
*/
int removeElement(queue *q) {
    assert(q->length > 0);
	
    // Obtain the current head of the list
    int current_head_item = q->list[q->head_index];

    q->length--;

    /* 
        Since the head has been removed, shift the head index to
        the next position.  If we are at the end of the list, 
        then we wrap around to the beginning.
    */
    if (q->length == 0) {
        /* empty queues start at position 0 */
        q->head_index = 0; 
    } else { 
        q->head_index = (q->head_index + 1) % q->max_length; 
        }

    return current_head_item;
    }
