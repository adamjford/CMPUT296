#include "hashtable.h"
#include <stdlib.h>
#include <assert.h>

/*
    A very simple hash function
*/
int ht_hash(hashtable ht, int id) {
    return id % ht->num_buckets;
    }

hashtable ht_create(int size_hint)
{
    int num_buckets = size_hint;
    hashtable ht = (hashtable) malloc(sizeof(ht_table_instance));
    assert(ht);

    ht->num_buckets = num_buckets;
    ht->buckets = (ht_node **) malloc(sizeof(ht_node *) * ht->num_buckets);
    assert(ht->buckets);

    /* Initialize linked lists to NULL */
    for(int i=0; i < ht->num_buckets; i++) {
        ht->buckets[i] = NULL;
        }

    return ht;
}

void ht_insert(hashtable ht, student_info item) {
    // what index in the table does it hash to?
    int index = ht_hash(ht, item.id);

    // empty position
    if ( ! ht->buckets[index] ) {
        // empty list, just place it there */
        ht_node *n = (ht_node *) malloc(sizeof(ht_node));
        assert(n);
        n->item = item;
        n->next = 0;
        ht->buckets[index] = n;
        return;
        } 

    // collision, insert into the list if not already there
    ht_node *cur = ht->buckets[index];
    while (cur) {
        if ( (cur->item).id == item.id ) {
            // already in table, replace it
            cur->item = item;
            cur = 0;
        } else if ( cur->next ) {
            // no match, but more to look at, move on
            cur = cur->next;
        } else {
            // no match, at end of list, insert at end
            ht_node *n = (ht_node *) malloc(sizeof(ht_node));
            assert(n);
            cur->next = n; 
            n->item = item;
            n->next = 0;
            cur = 0;
            }
        }
    }

int ht_lookup(hashtable ht, int id, student_info *itemp) {
    int index = ht_hash(ht, id);

    if ( ! ht->buckets[index] ) {
        // empty list, not present 
        return 0;
        }

    // walk along collision list looking for matching id
    ht_node *cur = ht->buckets[index];
    while (cur) {
        if ( (cur->item).id == id ) {
            // found it, return the item and success
            *itemp = cur->item;
            return 1;
            }

        // no match, more to look at, move on
        cur = cur->next;
        }

    // could not find it
    return 0;
    }

void ht_destroy(hashtable ht) {
    // free up each bucket

    ht_node *cur;
    ht_node *next;

    for(int i=0; i < ht->num_buckets; i++) {
        // star at the head
        cur = ht->buckets[i]; 
        while (cur) {
            // remember the next node in the list
            next = cur->next;
            free(cur);
            // move to next
            cur = next;
            }
        }

    // now clean up the topmost structures
    free(ht->buckets);
    free(ht);
    }

/*
    Delete the student info item that matches the given id.

    If missing, don't do anything.
*/
void ht_delete(hashtable h, int id) {
    /* unimplemented stub */
    }

