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
    }

void setup() {
    Serial.begin(9600);

    randomSeed(analogRead(0));

    int Test_len = 10;
    int Test[Test_len];

    Serial.print("In: ");
    for (int i=0; i < Test_len; i++) {
        Test[i] = random(0, 100);
        Serial.print(Test[i]);
        Serial.print(" ");
        }
    Serial.println();

    merge_sort(Test, Test_len);
    
    Serial.print("Out: ");
    for (int i=0; i < Test_len; i++) {
        Serial.print(Test[i]);
        Serial.print(" ");
        }
    Serial.println();
    }

void loop() {
    }
