#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

/*
   print the contents of a queue from head to tail going left 
   to right.

NOTE:  This code is fragile as it inspects the internal 
representation of the queue.

*/
void printf_queue(queue *q) {
  int pos = q->head_index;
  for (int i=0; i < length(q); i++) {
    printf("%d ", q->list[pos]);
    pos = (pos + 1) % q->max_length;
  }
}

int main(int argc, char *argv[]) {
  /* test harness */
  int tests_passed = 0;
  int tests_failed = 0;

  /* create a queue instance and initialize it */ 
  queue q_instance;

  /* create a handle to the queue so that we can manipulate it
     without having to put the & in front all the time */

  queue *qp = &q_instance;

  printf("Initializing queue\n");
  initializeQueue(qp, 20);

  /* how do we see if queue was propery initialized? */

  /* add and remove one element */
  int e1 = 42;

  addElement(qp, e1);
  printf("Test 1: ");
  printf_queue(qp);
  printf("\n");

  /* length should have gone up by one */

  if ( length(qp) != 1 ) {
    printf("Test 1 failed, length %d should be 1\n", 
        length(qp));
    tests_failed++;
  }
  else {
    printf("Test 1 passed.\n");
    tests_passed++;
  }


  printf("Test 2: ");
  int e2 = removeElement(qp);
  printf_queue(qp);
  printf("\n");

  if ( length(qp) != 0 ) {
    printf("Test 2.1 failed, length %d should be 0\n", 
        length(qp));
    tests_failed++;
  }
  else {
    printf("Test 2.1 passed.\n");
    tests_passed++;
  }

  if ( e1 != e2 ) {
    printf("Test 2.2 failed, e2 %d should equal e1 %d\n", 
        e2, e1);
    tests_failed++;
  }
  else {
    printf("Test 2.2 passed.\n");
    tests_passed++;
  }

  printf("Test 3: ");
  for (int i=1; i <= 10; i++) {
    addElement(qp, i);
  }
  printf_queue(qp);
  printf("\n");
  for (int i=1; i<= 10; i++) {
    e1 = removeElement(qp);
    if ( length(qp) != 10-i ) {
      printf("Test 3.1 failed, length %d should be %d\n",
          length(qp), 10-i);
      tests_failed++;
    }
    else {
      tests_passed++;
    }
    if ( e1 != i ) {
      printf("Test 3.2 failed, element %d should be %d\n",
          e1, i);
      tests_failed++;
    }
    else {
      tests_passed++;
    }
  }

  printf("Test 4: ");
  for (int i=1; i <= 10; i++) {
    addElement(qp, i);
  }

  printf_queue(qp);
  printf("\n");

  for (int i=0; i < 10; i++) {
    int expected = i + 1;
    int actual = getElement(qp, i);
    if(expected != actual) {
      printf("Test 4 failed, element #%d should be %d but was %d\n",
          i, expected, actual);
      tests_failed++;
     } else {
     tests_passed++;
     }
  }

  // Reset to empty
  for (int i=1; i <= 10; i++) {
    removeElement(qp);
  }

  int expected5 = getElement(qp, 0);

  if(expected5 != 0) {
    printf("Test 5 failed, an non-existent element should be 0 but was %d\n", expected5);
    tests_failed++;
  } else {
    printf("Test 5 passed.\n");
    tests_passed++;
  }

  /* a fatal test */
  if ( 0 ) {
    printf("Test 6: remove on empty queue\n");
    e2 = removeElement(qp);
    tests_failed++;
  }

  printf("Tests Passed: %d\n", tests_passed);
  printf("Tests Failed: %d\n", tests_failed);
}
