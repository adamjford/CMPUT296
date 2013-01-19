#include "hashtable.h"
#include <stdio.h>

void lookup_test(hashtable ht, int test_id) {
  student_info s;
  if (ht_lookup(ht, test_id, &s) ) {
    printf("Id %d has id %d, name %s, grade %s\n", 
        test_id, s.id, s.name, s.grade);
  }
  else {
    printf("Id %d not found in hash table\n", test_id);
  }
}


/* our test data */
student_info students[] = { 
  { 451241, "Marjorie G. Smith", "B+" },
  { 519244, "Michael P. Anderson", "C", },
  { 129426, "Ben E. Harrison", "A-" }, 
  { 743295, "William A. Leslie", "B-" },
  { 623599, "Brenda M. Crumble", "A+" },
  { 195151, "Mary M. Toney", "A-" },
  { 435324, "Markus G. Smith", "B+" },
  { 519246, "Cassandra P. Anderson", "C", },
  { 129425, "Foo B. Bar", "A-" }, 
  { 743299, "Leslie A. Williams", "B-" },
  { 623593, "Norah M. Stumble", "A+" }
};
int num_students = 12;

int test_ids[] = {
  195151, 519244, 666222,
};
int num_test_ids = 3;

void test_delete() {
  printf("Delete Tests:\n");

  hashtable ht;

  printf("1. Trying to delete something from an empty hashtable: ");

  ht = ht_create(3);

  ht_delete(ht, 0);

  //If code after the previous line is still executing, the test passed
  printf("Passed\n");

  ht_destroy(ht);
  ht = ht_create(3);

  printf("2. Deleting an element from the hashtable when it contains only that element: ");

  student_info test_student = students[0];
  student_info lookup;

  ht_insert(ht, test_student);

  if(ht_lookup(ht, test_student.id, &lookup) == 0 || lookup.id != test_student.id) {
    printf("FAILED -- Insert failed to properly insert student\n");
  } else {
    ht_delete(ht, 0);
    if(ht_lookup(ht, test_student.id, &lookup) != 0) {
      printf("FAILED -- Delete did not remove student from hashtable\n");
    } else {
      printf("Passed");
    }
  }

  ht_destroy(ht);
  ht = ht_create(3);

  printf("2. Deleting an element from the hashtable when there's one element in each hashtable: ");

  for (int i=0; i < 3; i++) {
    ht_insert(ht, students[i]);
  }

  test_student = students[1];

  if(ht_lookup(ht, test_student.id, &lookup) == 0 || lookup.id != test_student.id) {
    printf("FAILED -- Insert failed to properly insert student\n");
  } else {
    ht_delete(ht, 1);
    if(ht_lookup(ht, test_student.id, &lookup) != 0) {
      printf("FAILED -- Delete did not remove student from hashtable\n");
    } else {
      printf("Passed");
    }
  }

  ht_destroy(ht);
  ht = ht_create(3);

  printf("2. Deleting an element from the hashtable when there's multiple elements in each hashtable: ");

  for (int i=0; i < num_students; i++) {
    ht_insert(ht, students[i]);
  }

  test_student = students[3];

  if(ht_lookup(ht, test_student.id, &lookup) == 0 || lookup.id != test_student.id) {
    printf("FAILED -- Insert failed to properly insert student\n");
  } else {
    ht_delete(ht, 3);
    if(ht_lookup(ht, test_student.id, &lookup) != 0) {
      printf("FAILED -- Delete did not remove student from hashtable\n");
    } else {
      printf("Passed");
    }
  }
}

int main(int argc, char *argv[]) {
  // need to know implementation to realise that size 3 will create collisions
  hashtable ht = ht_create(3);

  // how test collisions?
  for (int i=0; i < num_students; i++) {
    ht_insert(ht, students[i]);
  }

  for (int i=0; i < num_test_ids; i++) {
    int test_id = test_ids[i];
    lookup_test(ht, test_id);
  }

  // how would you test this?
  ht_destroy(ht);

  test_delete();
}

