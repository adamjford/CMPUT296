#include <Arduino.h>
#include <mem_syms.h>

// some formatting routines to indent our messages to make it easier
// to trace the recursion.

uint8_t indent_pos = 0;
const uint8_t indent_amt = 2;

void indent_in() {
    if ( indent_pos <= 32 ) {
        indent_pos ++;
        }
    }

void indent_out() {
    if ( indent_pos >= indent_amt ) {
        indent_pos --;
        }
    }

void indent() {
    for (uint8_t i=0; i < indent_pos * indent_amt; i++) {
        Serial.print(" ");
        }
    }

// print out memory use info, s is a simple descriptive string
void mem_info(char *s) {
    indent();
    Serial.print(s);
    Serial.print(" Stack: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Avail: ");
    Serial.print(AVAIL_MEM);
    Serial.println();
    }

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

void merge(int16_t *Left, int16_t Left_len, int16_t *Right, int16_t Right_len, 
    int16_t *S) {

    // position of next element to be processed
    int Left_pos = 0;
    int Right_pos = 0;

    // position of next element of S to be specified
    // note: S_pos = Left_pos+Right_pos
    int S_pos = 0;

    // false, take from right, true take from left
    int pick_from_left = 0;

    while ( S_pos < Left_len + Right_len ) {

    // pick the smallest element at the head of the lists
    // move smallest of Left[Left_pos] and Right[Right_pos] to S[S_pos] 
    if ( Left_pos >= Left_len ) {
        pick_from_left = 0;
        }
    else if ( Right_pos >= Right_len ) {
        pick_from_left = 1;
        }
    else if ( Left[Left_pos] <= Right[Right_pos] ) {
        pick_from_left = 1;
        }
    else {
        pick_from_left = 0;
        }

    if ( pick_from_left ) {
        S[S_pos] = Left[Left_pos];
        Left_pos++;
        S_pos++;
        }
    else {
        S[S_pos] = Right[Right_pos];
        Right_pos++;
        S_pos++;
        }
    
    }
}


// sort in place, i.e. A will be reordered
void merge_sort(int16_t *A, int16_t A_len) {
    indent_in();
    indent();
    Serial.print("Entering merge sort: array addr ");
    Serial.print( (int) A );
    Serial.print(" len ");
    Serial.println( A_len);
    mem_info("");

    assert_free_mem_ok(128, "merge_sort");

    if ( A_len < 2 ) {
        indent_out();
        return;
        }

    if ( A_len == 2 ) {
        if ( A[0] > A[1] ) {
            int temp = A[0];
            A[0] = A[1];
            A[1] = temp;
            }
        indent_out();
        return;
        }

    // split A in half, sort left, sort right, then merge
    // left half is:  A[0], ..., A[split_point-1]
    // right half is: A[split_point], ..., A[A_len-1]

    int split_point = A_len / 2;

    indent();
    Serial.println("Doing left sort");

    merge_sort(A, split_point);

    mem_info("After left sort");

    indent();
    Serial.println("Doing right sort");

    merge_sort(A+split_point, A_len-split_point);

    mem_info("After right sort");

    // don't need the merging arrat S until this point
    int *S = (int *) malloc( A_len * sizeof(int) );

    assert_malloc_ok(S, "Cannot get merge buffer");

    mem_info("Doing merge");

    merge(A, split_point, A+split_point, A_len-split_point, S);

    for (int i=0; i < A_len; i++) {
        A[i] = S[i];
        }

    // now we are done with it
    free(S);

    mem_info("After free");
    indent_out();
    }

void setup() {
    Serial.begin(9600);

    // int *bad_news = (int *) malloc(4000);

    mem_info("********* THIS IS THE BEGINNING *********");
    randomSeed(analogRead(0));

    int16_t Test_len = 256;
    int16_t Test[Test_len];

    Serial.print("In: ");
    for (int16_t i=0; i < Test_len; i++) {
        Test[i] = random(0, 100);
if ( 1 ) {
        Serial.print(Test[i]);
        Serial.print(" ");
}
        }
    Serial.println();

    merge_sort(Test, Test_len);
    
if ( 1 ) {
    Serial.print("Out: ");
    for (int16_t i=0; i < Test_len; i++) {
        if ( i < Test_len-1 && Test[i] > Test[i+1] ) {
            Serial.print("Out of order!!");
            }

        Serial.print(Test[i]);
        Serial.print(" ");
        }
    Serial.println();
}
    }

void loop() {
    }
