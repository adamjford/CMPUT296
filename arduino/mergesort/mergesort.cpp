#include <Arduino.h>

const int n_l = 4;
const int n_r = 5;

int L[n_l];
int R[n_r];

int S[n_l + n_r];


void merge(int *left, int n_Left, int *right, int n_Right, int *s) {
  // position of the next element to be processed
  int left_pos = 0;
  int right_pos = 0;
  
  // position of next element of S to be specified
  // note: s_pos = left_pos + right_pos
  int s_pos = 0;
  int pickFromLeft = 0;

  for(int s_pos = 0; s_pos < (n_Left + n_Right); s_pos++) {
    if (left_pos >= n_Left) {
      pickFromLeft = 0;
    } else if (right_pos >= n_Right) {
      pickFromLeft = 1;
    } else if (left[left_pos] <= right[right_pos]) {
      pickFromLeft = 1;
    } else {
      pickFromLeft = 0;
    }

    if(pickFromLeft) {
      s[s_pos] = left[left_pos];
      left_pos++;
    } else {
      s[s_pos] = right[right_pos];
      right_pos++;
    }
  }
}

void mergesort(int *A, int length) {
  if(length <= 1) {
    return;
  }
  if(length == 2) {
    if ( A[0] > A[1] ) {
      int tmp = A[0];
      A[0] = A[1];
      A[1] = tmp;
    }
    return;
  }

  // split A in half
  // A[0 .. midpoint - 1], A[midpoint .. length]
  int midpoint = length / 2;

  mergesort(A, midpoint);
  mergesort(A+midpoint, length-midpoint);

  int S[length];
  merge(A, midpoint, A+midpoint, length - midpoint, S);

  for(int i=0; i < length; i++) {
    A[i] = S[i];
  }
}

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(12));

int test_len = 32;
int test[test_len];

Serial.print("In: ");
for(int i =0; i < test_len; i++) {
  test[i] = random(0, 100);
  Serial.print(test[i]);
  Serial.print(" ");
}

Serial.println(" ");

mergesort(test, test_len);

Serial.print("Out: ");
for(int i =0; i < test_len; i++) {
  test[i] = random(0, 100);
  Serial.print(test[i]);
  Serial.print(" ");
}

Serial.println(" ");



  /*

  Serial.print("L: ");
  for (int i = 0; i < n_l; i++) {
    L[i] = random(i * 10, (i+1) * 10);
    Serial.print(L[i]);
    Serial.print(" ");
  }

  Serial.println(" ");

  Serial.print("R: ");
  for (int i = 0; i < n_r; i++) {
    R[i] = random(i * 10, (i+1) * 10);
    Serial.print(R[i]);
    Serial.print(" ");
  }

  Serial.println(" ");

  merge(L, n_l, R, n_r, S);

  Serial.print("S: ");
  for (int i = 0; i < n_l + n_r; i++) {
    Serial.print(S[i]);
    Serial.print(" ");
  }

  Serial.println(" ");
  */
}

void loop() {

}
