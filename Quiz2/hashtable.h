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
    student_info item;
    struct ht_node *next;
} ht_node;

typedef struct {
    /* items in the table are placed into buckets, each bin holding items with
    the same hash index */
    ht_node **buckets;  
    int num_buckets;
} ht_table_instance;

typedef ht_table_instance *hashtable;

/* 
    Constructor: create a hash table that will contain roughly size_hint
    items and return a pointer to the instance.
*/
hashtable ht_create(int size_hint);

/*
    Destructor: release all the storage used by the hash table.
*/
void ht_destroy(hashtable h);

/*
    Insert the given item into the hash table using id as the key.
    If an item already exists in the table with the same id, replace 
    it with this new one.
*/
void ht_insert(hashtable h, student_info item);

/*
    Lookup the student info item that matches the given id.

    If present, return it in the struct pointed to by itemp, and 
    return 1.

    If missing, don't modify the item, and return 0.
*/
int ht_lookup(hashtable h, int id, student_info *itemp);

/*
    Delete the student info item that matches the given id.

    If missing, don't do anything.
*/
void ht_delete(hashtable h, int id);

#endif
