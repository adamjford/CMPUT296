/*
   Implementation of queue Abstract Data Type (ADT)
   */

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include "queue.h"

/*
Constructor: create a queue instance and return a queue
(i.e. a pointer to the struct).
*/

queue q_create(int size_hint) {
  queue q = (q_instance_t *) malloc(sizeof(q_instance_t));
  assert(q != 0);

  q->head = 0;
  q->tail = 0;
  q->length = 0;

  return q;
}

/*
Destructor: free up the storage used by the queue.
*/
void q_destroy(queue q) {
  /* get rid of all the elements in the queue */
  while ( q_length(q) > 0 ) {
    q_remove(q);
  }
  free(q);
}

/*
   Get the current length of the queue
   */
int q_length(queue q) {
  return q->length;
}

/*
   Add the element val to the tail of the queue q
   */

void q_add(queue q, int val) {
  q_node_t * n = (q_node_t *) malloc(sizeof(q_node_t));

  // make sure malloc worked
  assert(n != 0);

  // initialze the new node to contain the value and have no next
  n->val = val;
  n->next = 0;

  // if there is stuff in the queue, add new node to end
  // if an empty queue, need to set up head.
  if (q->length != 0) {
    q->tail->next = n;
  } else {
    q->head = n;
  }

  // new node is at the tail
  q->tail = n;
  q->length++;
}

/*
   Remove and return the element at the head of queue q

   Pre-condition: q_length(q) > 0
   */

int q_remove(queue q) {
  assert(q->length > 0);

  // get the value at the head
  int rval = q->head->val;

  // new head is the next one
  q_node_t *new_head = q->head->next;

  /* Now we can free the old head so that we don't leave unused 
     memory allocated
     */
  free(q->head);

  q->length--;

  // Now we can set the head to new_head
  q->head = new_head;

  // if queue is empty, we need to set tail also.
  if (q->length == 0) {
    q->tail = 0;
  }

  return rval;
}

q_node_t * q_get_node(queue q, int index) {
  assert(0 <= index && index < q->length);

  q_node_t *node;

  int tailIndex = q_length(q)-1;
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

  return node;
}

/*
   Get the element of the queue at position index,
   where the head of the queue is position 0, and the
   tail is at position length(q)-1
   */
int q_get_item(queue q, int index) {
  assert(0 <= index && index < q_length(q));

  return q_get_node(q, index)->val;
}

/*
   Return the element at index in the queue, and deletes it from inside
   the queue.
   */
int q_delete_item(queue q, int index) {
  assert(0 <= index && index < q_length(q));

  int val;

  if(index == 0) {
    q_node_t *new_head = q->head->next;
    val = q->head->val;
    free(q->head);
    q->head = new_head;
    if (q->length == 0) {
      q->tail = 0;
    }
  } else {
    q_node_t *previousNode = q_get_node(q, index - 1);
    q_node_t *newNext = previousNode->next->next;
    
    val = previousNode->next->val;

    free(previousNode->next);
    previousNode->next = newNext;
    if(previousNode->next == 0){
      q->tail = previousNode;
    }
  }

  q->length--;
  return val;
}

void q_insert_item(queue q, int index, int val) {
  assert(0 <= index);
}

