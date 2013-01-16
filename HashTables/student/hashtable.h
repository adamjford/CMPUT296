#ifndef _hashtable_h
#define _hashtable_h


#include "student.h"
/*
    Hash table of student records.

    The hash table is implemented using collision lists.  Each collision
    list contains all the student info records whose id hashes to the same 
    index value.

    NOTE: we manipulate and store actual student records in the hash table, 
    not pointers to the records.
*/

typedef struct ht_node {
  student_info entry;
  struct ht_node *next;
} ht_node;

typedef struct {
  ht_node **table;  /* pointer to an array of pointers to ht_node */
  int size;
} ht_table_instance;

typedef ht_table_instance *hashtable;

/* 
    Constructor: create a hash table of a given size and return a pointer
    to the instance.
*/
hashtable ht_create(int size_hint);

/*
    Destructor: release all the storage used by the hash table.
*/
void ht_destroy(hashtable h);

/*
    Insert the given entry into the hash table using id as the key.
    If an entry already exists in the table with the same id, replace 
    it with this new one.
*/
void ht_insert(hashtable h, student_info entry);

/*
    Lookup the student info entry that matches the given id.

    If present, return it in the struct pointed to by entryp, and 
    return 1.

    If missing, don't modify the entry, and return 0.
*/
int ht_lookup(hashtable h, int id, student_info *entryp);


#endif
