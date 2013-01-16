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
};
int num_students = 6;

int test_ids[] = {
  195151, 519244, 666222,
};
int num_test_ids = 3;

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
}
