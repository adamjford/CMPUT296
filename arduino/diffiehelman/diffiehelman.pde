void setup() {
  unsigned int x = 1;
  int count = 0;

  Serial.begin(9600);

  while (x != 0) {
    count = count + 1;
    x = x << 1;
  }

  Serial.print("Number of bits:");
  Serial.println(count);
}

void loop() {
}
