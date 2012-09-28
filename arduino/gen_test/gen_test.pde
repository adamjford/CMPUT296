void setup() {
  Serial.begin(9600);
  
  uint16_t p = 19211;
  uint16_t g = 6;
  uint16_t e = 1;
  uint16_t i = 1;
  
  // check that powers of g mod p generate all the numbers
  // from 1 to p -1
  // g g^2 g^3 ... all mod p.
  
  for(i = 0; i < p - 1; i++) {
    e = (e * g) % p;
  }

    Serial.print("g^");
    Serial.print(i+1);
    Serial.print(": ");
    Serial.println(e);
  /*
  if(e == 1) {
    Serial.print(g);
    Serial.print(" is a generator for ");
    Serial.print(p);
    Serial.println(".");
  } else {
    Serial.print(g);
    Serial.print(" is NOT a generator for ");
    Serial.print(p);
    Serial.println(".");
  }
  */
}

void loop() {
  
}
