#include <Arduino.h>
#include <mem_syms.h>

void merge(int *Left, int Left_len, int *Right, int Right_len, int *S) {
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
void merge_sort(int *A, int A_len) {
    Serial.print("Entering merge sort: ");
    Serial.print((int) A);
    Serial.print(" len:");
    Serial.println(A_len);
    Serial.print("Entering Stack: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Available Memory: ");
    Serial.print(AVAIL_MEM);
    Serial.println();

    if ( AVAIL_MEM < 128 ) {
        Serial.print("ACK, no stack either! ");
        Serial.println(AVAIL_MEM);
        while ( 1 ) {}
    }

    if ( A_len < 2 ) {
        return;
        }

    if ( A_len == 2 ) {
        if ( A[0] > A[1] ) {
            int temp = A[0];
            A[0] = A[1];
            A[1] = temp;
            }
        return;
        }

    // split A in half, sort left, sort right, then merge
    // A[0], ..., A[split_point-1]
    int split_point = A_len / 2;

    Serial.println("Doing merge sort 1: ");
    merge_sort(A, split_point);

    Serial.print("Stack after merge sort 1: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Available Memory: ");
    Serial.print(AVAIL_MEM);
    Serial.println();

    Serial.println("Doing merge sort 2: ");
    merge_sort(A+split_point, A_len-split_point);
    Serial.print("Stack after merge sort 2: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Available Memory: ");
    Serial.print(AVAIL_MEM);
    Serial.println();

    // don't need S until this point
    int *S = (int *) malloc( A_len * sizeof(int) );

    if ( ! S ) {
        Serial.println("ARRGH, No memory left.");
        while(1) { }
        }

    Serial.print("Stack after malloc: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Available Memory: ");
    Serial.print(AVAIL_MEM);
    Serial.println();

    merge(A, split_point, A+split_point, A_len-split_point, S);

    for (int i=0; i < A_len; i++) {
        A[i] = S[i];
        }

    free(S);

    Serial.print("Stack after free: ");
    Serial.print(STACK_SIZE);
    Serial.print(" Heap: ");
    Serial.print(HEAP_SIZE);
    Serial.print(" Available Memory: ");
    Serial.print(AVAIL_MEM);
    Serial.println();
    }

void setup() {
    Serial.begin(9600);

    //int *bad_news = (int *) malloc(4000);

    Serial.println("********* THIS IS THE BEGINNING *********");
    randomSeed(analogRead(0));

    int Test_len = 2048;
    int Test[Test_len];

    Serial.print("In: ");
    for (int i=0; i < Test_len; i++) {
        Test[i] = random(0, 100);
        Serial.print(Test[i]);
        Serial.print(" ");
        }
    Serial.println();

    merge_sort(Test, Test_len);
    
if ( 1 ) {
    Serial.print("Out: ");
    for (int i=0; i < Test_len; i++) {
        if ( 0 && i < Test_len-1 && Test[i] > Test[i+1] ) {
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
