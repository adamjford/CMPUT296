#include <Arduino.h>

#define swap(x, y) { int tmp = x; x = y; y = tmp; }

uint16_t partition(uint16_t *A, uint16_t len) {
  Serial.print("Start partition -- in: ");
  for (int16_t i=0; i < len; i++) {
      Serial.print(A[i]);
      Serial.print(" ");
  }
  Serial.println();

  uint16_t pivot = 0;
  uint16_t end = len - 1;
  while(pivot < end) {
    if(A[pivot] < A[pivot + 1]) {
      swap(A[pivot + 1], A[end]);
      end--;
    } else {
      swap(A[pivot], A[pivot + 1]);
      pivot++;
    }
  }

  Serial.print("Partition out: ");
  for (int16_t i=0; i < len; i++) {
      Serial.print(A[i]);
      Serial.print(" ");
  }
  Serial.println();
  Serial.print("Pivot: ");
  Serial.println(pivot);

  return pivot;
}

void quicksort(uint16_t *A, uint16_t len) {
  Serial.print("Start quicksort -- in: ");
  for (int16_t i=0; i < len; i++) {
      Serial.print(A[i]);
      Serial.print(" ");
  }
  Serial.println();

  if(len < 2) {
    Serial.print("len = ");
    Serial.print(len);
    Serial.println("; returning.");
    return;
  }
  
  uint16_t pivot = partition(A, len);
  quicksort(A, pivot);
  quicksort(A+pivot+1, len-pivot-1);
  Serial.print("Start quicksort -- out: ");
  for (int16_t i=0; i < len; i++) {
      Serial.print(A[i]);
      Serial.print(" ");
  }
  Serial.println();
}

void setup() {
    Serial.begin(9600);

    randomSeed(analogRead(0));

    uint16_t Test_len = 9;
    uint16_t Test[9] = { 4, 13, 2, 1, 7, 5, 9, 3, 11 };


    quicksort(Test, Test_len);
    
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

void loop() {

}
