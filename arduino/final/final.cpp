#include <Arduino.h>

typedef struct {
  uint32_t n;
  uint32_t d;
} frac;

frac fraclarger(int *d1, size_t d1len, int *d2, size_t d2len) {
  int higherCount = 0;
  int totalCount = d1len * d2len;

  for(int i = 0; i < d1len; i++) {
    for(int j = 0; j <d2len; j++) {
      if(d1[i] > d2[j]) {
        higherCount++;
      }
    }
  }
  frac frac;
  frac.n = higherCount;
  frac.d = totalCount;
  return frac;
}

void printFrac(frac frac) {
  Serial.print("{ ");
  Serial.print(frac.n);
  Serial.print(" , ");
  Serial.print(frac.d);
  Serial.println(" }");
}

int function(uint32_t n) {
  Serial.print("Input: ");
  Serial.println(n);

  int min = 0, max = 32;
  int i;

  int count = 0;
  Serial.print("Iteration #");
  Serial.print(count);
  Serial.print(": i = ");
  Serial.print(i);
  Serial.print("; min = ");
  Serial.print(min);
  Serial.print("; max = ");
  Serial.println(max);

  while(min != max) {
    i = (min + max) / 2;

    if(n >> i) {
      min = i+1;
    } else {
      max = i;
    }

    count++;
    Serial.print("Iteration #");
    Serial.print(count);
    Serial.print(": i = ");
    Serial.print(i);
    Serial.print("; min = ");
    Serial.print(min);
    Serial.print("; max = ");
    Serial.println(max);
  }

  Serial.print("Returned: ");
  Serial.println(min);
  Serial.println();

  return min;
}

void setup() {
  Serial.begin(9600);
  /*
     int d6[] = {1, 2, 3, 4, 5, 6};
     int d1[] = {10};
     int d2[] = { 0, 7 };

     frac f1 = fraclarger(d6, 6, d6, 6);
     printFrac(f1);
     frac f2 = fraclarger(d6, 6, d1, 1);
     printFrac(f2);
     frac f3 = fraclarger(d6, 6, d2, 2);
     printFrac(f3);
     */

  function(0x2A3);
  function(5000);
  function(10000);
}

void loop() {
}
