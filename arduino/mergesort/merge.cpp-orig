#include <Arduino.h>

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


void setup() {
    Serial.begin(9600);

    // lists to be merged
    // Assume: L, R sorted in ascending order
    const int n_L = 4;
    const int n_R = 5;
    int L[n_L];
    int R[n_R];


    // Result: L, R merged
    int S[n_L + n_R];

    Serial.print("L: ");
    for (int i=0; i < n_L; i++) {
        L[i] = random(i * 10, (i+1) * 10);
        Serial.print(L[i]);
        Serial.print(" ");
        }
    Serial.println();

    Serial.print("R: ");
    for (int i=0; i < n_R; i++) {
        R[i] = random(i * 10, (i+1) * 10);
        Serial.print(R[i]);
        Serial.print(" ");
        }
    Serial.println();

    merge(L, n_L, R, n_R, S);
    
    Serial.print("S: ");
    for (int i=0; i < n_L + n_R; i++) {
        Serial.print(S[i]);
        Serial.print(" ");
        }
    Serial.println();
    }

void loop() {
    }
