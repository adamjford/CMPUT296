#include "hashtable.h"
#include <stdlib.h>
#include <assert.h>

/*
    A very simple hash function
*/
int ht_hash(hashtable ht, int id) {
    return id % ht->size;
    }

hashtable ht_create(int size_hint)
{
    int size = size_hint;
    hashtable ht = (hashtable) malloc(sizeof(ht_table_instance));

    ht->size = size;
    ht->table = (ht_node **) malloc(sizeof(ht_node *) * size);

    /* Initialize linked lists to NULL */
    for(int i=0; i<size; i++) {
        ht->table[i] = NULL;
        }

    return ht;
}

void ht_insert(hashtable ht, student_info entry) {
    // what index in the table does it hash to?
    int index = ht_hash(ht, entry.id);

    // empty position
    if ( ! ht->table[index] ) {
        // empty list, just place it there */
        ht_node *n = (ht_node *) malloc(sizeof(ht_node));
        assert(n);
        n->entry = entry;
        n->next = 0;
        ht->table[index] = n;
        return;
        } 

    // collision, insert into the list if not already there
    ht_node *cur = ht->table[index];
    while (cur) {
        if ( (cur->entry).id == entry.id ) {
            // already in table, replace it
            cur->entry = entry;
            cur = 0;
        } else if ( cur->next ) {
            // no match, but more to look at, move on
            cur = cur->next;
        } else {
            // no match, at end of list, insert at end
            ht_node *n = (ht_node *) malloc(sizeof(ht_node));
            assert(n);
            cur->next = n; 
            n->entry = entry;
            n->next = 0;
            cur = 0;
            }
        }
    }

int ht_lookup(hashtable ht, int id, student_info *entryp) {
    int index = ht_hash(ht, id);

    if ( ! ht->table[index] ) {
        // empty list, not present 
        return 0;
        }

    // walk along collision list looking for matching id
    ht_node *cur = ht->table[index];
    while (cur) {
        if ( (cur->entry).id == id ) {
            // found it, return the entry and success
            *entryp = cur->entry;
            return 1;
            }

        // no match, more to look at, move on
        cur = cur->next;
        }

    // could not find it
    return 0;
    }

void ht_destroy(hashtable ht) {
    /* unimplemented stub */
    }
