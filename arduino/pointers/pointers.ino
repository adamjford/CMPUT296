void rev(char *s) {
  char *t = s;
  while (*t) {
    t++;
  }

  char *fromStart = s;
  char *fromEnd = t - 1;
  while(fromStart != fromEnd) {
    Serial.print("From Start: ");
    Serial.print(*fromStart);
    Serial.print("From End: ");
    Serial.println(*fromEnd);
    fromStart++;
    fromEnd--;
  }
  Serial.print("Middle character: ");
  Serial.println(*fromStart);
}

void setup() {
  Serial.begin(9600);
  rev("abcdef");
}

void loop() {
  
}
