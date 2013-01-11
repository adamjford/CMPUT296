/*
    Implementation of queue Abstract Data Type (ADT)
*/

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "queue.h"

/* 
    Take a declared empty queue structure and initialize it.

    Warning: Do not call on an existing queue.  Will get a 
    memory leak.
*/

void initializeQueue(queue *q, int size_hint) {
    q->head = 0;
    q->tail = 0;
    q->length = 0;
}

/*
    Get the current length of the queue
*/
int length(queue *q) {
    return q->length;
    }

/*
    Add the element val to the tail of the queue q
*/

void addElement(queue *q, int val) {
    node * n = (node *) malloc(sizeof(node));

    // make sure malloc worked
    assert(n != 0);

    n->val = val;
    n->next = NULL;

    if (q->length != 0) {
            q->tail->next = n;
    } else {
            q->head = n;
    }
    q->tail = n;
    q->length++;
    }

/*
    Remove and return the element at the head of queue q

    Pre-condition: q->length > 0
*/

int removeElement(queue *q) {
    assert(q->length > 0);
    
    int rval = q->head->val;
    node * new_head = q->head->next;

    /* Now we can free the old head so that we don't leave unused 
       memory allocated
    */
    free(q->head);

    q->length--;

    // Now we can set the head to new_head
    q->head = new_head;

    if (q->length == 0) {
        q->tail = 0;
        }

    return rval;
    }

/*
    Get the element of the queue at position index,
    where the head of the queue is position 0, and the
    tail is at position length(q)-1
*/
int getElement(queue *q, int index) {
  assert(0 <= index && index < q->length);

  node *node;

  int tailIndex = length(q)-1;
  if(index == tailIndex) {
    node = q->tail;
  } else {
    int pos = 0;
    node = q->head;
    while(pos < index) {
      node = node->next;
      pos++;
    }
  }

  return node->val;
    }
    
/*
    Return the element at index in the queue, and deletes it from inside
    the queue.
*/
int deleteElement(queue *q, int index) {
    /* STUB - does not work, must be implemented */
    return 0;
    }

