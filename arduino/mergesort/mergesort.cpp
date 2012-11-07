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

  for(int s_pos = 0; s_pos < (n_Left + n_Right); s_pos++) {
    if (left_pos == n_Left) {
      s[s_pos] = right[right_pos];
      right_pos++;
    } else if (right_pos == n_Right) {
      s[s_pos] = left[left_pos];
      left_pos++;
    } else if (left[left_pos] <= right[right_pos]) {
      s[s_pos] = left[left_pos];
      left_pos++;
    } else {
      s[s_pos] = right[right_pos];
      right_pos++;
    }
  }
}

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(12));

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
}

void loop() {

}
