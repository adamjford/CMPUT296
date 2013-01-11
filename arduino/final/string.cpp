#include <Arduino.h>
/*
char *strncpy(char *s1, const char *s2, int n) {
  boolean hitEndOfs1 = false;
  boolean hitEndOfs2 = false;

  for(size_t i = 0; i < n; i++) {
    char current;
    if(hitEndOfs2) {
      current = '\0';
    }
    else {
      current = s2[i];
      if(current == '\0') {
        hitEndOfs2 = true;
      }
    }

    s1[i] = current;
  }

  return s1;
}

void testcase1() {
  char s[5];
  char *s1 = s;
  const char *s2 = "foo";

  s1 = strncpy(s1, s2, 3);
  
  Serial.println(s1);
}

void testcase2() {
  char s[5];
  char *s1 = s;
  const char *s2 = "foo";

  s1 = strncpy(s1, s2, 5);
  
  Serial.println(s1);
}

void testcase3() {
  char s[5];
  char *s1 = s;
  const char *s2 = "Hello World!";

  s1 = strncpy(s1, s2, 5);
  
  Serial.println(s1);
}

void setup() {
  Serial.begin(9600);

  testcase1();
  testcase2();
  testcase3();
}

void loop() {
}
*/
