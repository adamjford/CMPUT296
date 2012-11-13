#include <Arduino.h>
#include <mem_syms.h>

// call this after a malloc to confirm that the malloc worked, and 
// if not, display the message s and enter a hard loop

void assert_malloc_ok(void * mem_ptr, char *s) {
    if ( ! mem_ptr ) { 
        Serial.print("Malloc failed. ");
        Serial.print(s);
        Serial.println();
        while ( 1 ) { }
        }
    }

// call this on entry to a procedure to assue that at least required amt of
// memory is available in the free area between stack and heap if not, display
// the message s and enter a hard loop

void assert_free_mem_ok(uint16_t required_amt, char *s) {

    if ( AVAIL_MEM < required_amt ) { 
        Serial.print("Insufficient Free Memory: ");
        Serial.print(s);
        Serial.print(" require ");
        Serial.print(required_amt);
        Serial.print(", have ");
        Serial.print(AVAIL_MEM);
        Serial.println();
        while ( 1 ) { }
        }
    }

// change this to sort different kinds of things, along with the
// comparison in the indexed_merge procedure
typedef int16_t element_t;

/*
    Here is the indexed merge routine, see below for details
    
    Given the Original array of element_t items, and with Left_index
    and Right_index being ascending sorts of sub-arrays of Original,
    then merge the two into a new Index of ascending order.

    Index must have size at least Left_len + Right_len.
*/

void indexed_merge(element_t Original[],
    uint16_t Left_index[], int16_t Left_len, 
    uint16_t Right_index[], int16_t Right_len, 
    uint16_t Index[]) {

    // position of next element to be processed
    int Left_pos = 0;
    int Right_pos = 0;

    // position of next element of Index to be specified
    // note: Index_pos = Left_pos+Right_pos
    int Index_pos = 0;

    // false, take from right, true take from left
    int pick_from_left = 0;

    while ( Index_pos < Left_len + Right_len ) {

    // pick the smallest element of Original at the head of the lists
    if ( Left_pos >= Left_len ) {
        pick_from_left = 0;
        }
    else if ( Right_pos >= Right_len ) {
        pick_from_left = 1;
        }
    // note that this is the only code that changed!
    else if ( Original[Left_index[Left_pos]] <= Original[Right_index[Right_pos]] ) {
        pick_from_left = 1;
        }
    else {
        pick_from_left = 0;
        }

    if ( pick_from_left ) {
        Index[Index_pos] = Left_index[Left_pos];
        Left_pos++;
        Index_pos++;
        }
    else {
        Index[Index_pos] = Right_index[Right_pos];
        Right_pos++;
        Index_pos++;
        }
    
    }
}


/* 
    Given an Original array, and an initial Index into the array initialized 
    to Index[i] = i for i = 0 to Original_len-1, reorder the contents of
    Index such that it permutes the elements of Original in ascending order.
    
    Suppose that we want to sort an array, Original, in a variety of 
    orders.  Rather than rearranging the elements of Original, we can
    keep it untouched and instead manipulate arrays of indexes 
    into the Original array.  Each index describes a particular ordering
    of the Original array.

    Note: this is exactly what is going on when we sorted restaurants
    in Assignment 2.

    Thus if we want to sort Original, we don't move the elements of Original
    around, we move the elements of Index around.  Index is the
    same size as Original, but instead of Index[i] containing data, it 
    contains the subscript of the element of Original that would be in that
    position.  Index is originally initialized so that Index[i]=i.

    For example, if
        Original = {'A', 'Z', 'D', 'F', 'A', 'T'};
    then we start off with 
        Index = {0, 1, 2, 3, 4, 5};
    and then after sorting Index describes Original sorted in ascending order 
        Index = {0, 4, 2, 3, 5, 1};

    This code will print out Original in ascending order:
        for (uint16_t i=0; i < Original_len; i++ ) {
            Serial.println(Original[Index[i]]);
            }
*/
void indexed_merge_sort(element_t Original[], 
       uint16_t Index[], uint16_t Original_len) {

    if ( Original_len < 2 ) {
        return;
        }

    if ( Original_len == 2 ) {
        if ( Original[Index[0]] > Original[Index[1]] ) {
            uint16_t temp = Index[0];
            Index[0] = Index[1];
            Index[1] = temp;
            }
        return;
        }

    // split A in half, sort left, sort right, then merge
    // left half is:  [0], ..., [split_point-1]
    // right half is: [split_point], ..., [Original_len-1]

    int split_point = Original_len / 2;

    indexed_merge_sort(Original, Index, split_point);
    indexed_merge_sort(Original, Index+split_point, Original_len-split_point);

    // don't need the merging array S until this point
    uint16_t *S = (uint16_t *) malloc( Original_len * sizeof(uint16_t) );

    assert_malloc_ok(S, "Cannot get merge buffer");

    // merge the left and right
    indexed_merge(Original, Index, split_point, Index+split_point, Original_len-split_point, S);

    for (int i=0; i < Original_len; i++) {
        Index[i] = S[i];
        }

    // now we are done with it
    free(S);

    }

void setup() {
    Serial.begin(9600);

    Serial.println("********* START *********");
    randomSeed(analogRead(0));

    int16_t Test_len = 8;
    element_t Test[Test_len];
    uint16_t Index[Test_len];

    Serial.print("In: ");
    for (int16_t i=0; i < Test_len; i++) {
        Test[i] = random(0, 100);
        Serial.print(Test[i]);
        Serial.print(" ");
        }
    Serial.println();

    // establish the original Index mapping
    
    if(0) {
    for (int16_t i=0; i < Test_len; i++) {
        Index[i] = i;
        }
    }
    indexed_merge_sort(Test, Index, Test_len);
    
    Serial.print("Out: ");
    for (int16_t i=0; i < Test_len; i++) {
        if ( i < Test_len-1 && Test[Index[i]] > Test[Index[i+1]] ) {
            Serial.print("Out of order!!");
            }

        Serial.print(Index[i]);
        Serial.print("->");
        Serial.print(Test[Index[i]]);
        Serial.print(" ");
        }
    Serial.println();
    }

void loop() {
    }
