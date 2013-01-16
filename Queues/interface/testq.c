#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

/*
   print the contents of a queue from head to tail going left 
   to right.
   */
void q_printf(queue q) {
  for (int i=0; i < q_length(q); i++) {
    printf("%d ", q_get_item(q, i));
  }
}


int main(int argc, char *argv[]) {
  /* test harness */
  int tests_passed = 0;
  int tests_failed = 0;

  /* create a queue with a size hint */
  printf("Creating queue\n");
  queue qp = q_create(20);

  /* how do we see if queue was propery initialized? */

  /* add and remove one element */
  int e1 = 42;

  q_add(qp, e1);
  printf("Test 1: ");
  q_printf(qp);
  printf("\n");

  /* length should have gone up by one */

  if ( q_length(qp) != 1 ) {
    printf("Test 1 failed, length %d should be 1\n", 
        q_length(qp));
    tests_failed++;
  }
  else {
    printf("Test 1 passed.\n");
    tests_passed++;
  }


  printf("Test 2: ");
  int e2 = q_remove(qp);
  q_printf(qp);
  printf("\n");

  if ( q_length(qp) != 0 ) {
    printf("Test 2.1 failed, length %d should be 0\n", 
        q_length(qp));
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
    q_add(qp, i);
  }
  q_printf(qp);
  printf("\n");
  for (int i=1; i<= 10; i++) {
    e1 = q_remove(qp);
    if ( q_length(qp) != 10-i ) {
      printf("Test 3.1 failed, length %d should be %d\n",
          q_length(qp), 10-i);
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
    q_add(qp, i);
  }

  q_printf(qp);
  printf("\n");

  for (int i=0; i < 10; i++) {
    int expected = i + 1;
    int actual = q_get_item(qp, i);
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
    q_remove(qp);
  }

  q_add(qp, e1);
  printf("Test 5.1: ");
  q_printf(qp);
  printf("\n");

  /* length should have gone up by one */

  if ( q_length(qp) != 1 ) {
    printf("Test 5.1 failed, length %d should be 1 before deletion\n", 
        q_length(qp));
    tests_failed++;
  }
  else {
    int actual = q_delete_item(qp, 0);
    if( q_length(qp) != 0) {
      printf("Test 5.1 failed, length %d should be 0 after deletion\n", 
          q_length(qp));
      tests_failed++;
    } else if(actual != e1) {
      printf("Test 5.1 failed, element retrieved from deleted: Expected: %d; Actual: %d\n", 
          e1, actual);
      tests_failed++;
    } else {
      printf("Test 5.1 passed.\n");
      tests_passed++;
    }
  }

  printf("Test 5.2: ");
  for (int i=1; i <= 10; i++) {
    q_add(qp, i);
  }

  q_printf(qp);
  printf("\n");

  int deletedElement;

  deletedElement = q_delete_item(qp, 4);
  if(deletedElement != 5) {
    printf("Test 5.2 failed, element retrieved from deleted: Expected: 5; Actual: %d\n", 
        deletedElement);
    tests_failed++;
  }

  deletedElement = q_delete_item(qp, 4);
  if(deletedElement != 6) {
    printf("Test 5.2 failed, element retrieved from deleted: Expected: 6; Actual: %d\n", 
        deletedElement);
    tests_failed++;
  }

  q_printf(qp);
  printf("\n");

  if( q_length(qp) != 8) {
    printf("Test 5.2 failed, length %d should be 8 after deletion\n", 
        q_length(qp));
    tests_failed++;
  } else {
    if(q_get_item(qp, 4) != 7) {
      printf("Test 5.2 failed, value of element at index 4 after deletion: Expected: 7; Actual: %d\n", q_get_item(qp, 4));
      tests_failed++;
    } else {
      printf("Test 5.2 passed.\n");
      tests_passed++;
    }
  }

  /* a fatal test */
  if ( 0 ) {
    printf("Test 4: remove on empty queue\n");
    e2 = q_remove(qp);
    tests_failed++;
  }

  printf("Tests Passed: %d\n", tests_passed);
  printf("Tests Failed: %d\n", tests_failed);
}
