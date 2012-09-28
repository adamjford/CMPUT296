uint16_t encryptionKey;
uint16_t p = 19211;
uint16_t g = 6;

/* Function returns 16bit random number, uses empty analog pin 0. */ 
/* Source: Timothy Put, CMPUT296 Discussion Forum */ 
uint16_t getRandom(){
  uint16_t randomBytes = 0;
  for(int i=0; i <= 15; i++) {
    randomBytes = randomBytes << 1;
    randomBytes = randomBytes | (analogRead(0) & 1);
    delayMicroseconds(100);
  }
  return randomBytes;
}

/*
    Compute and return (b ** e) mod m
    For unsigned b, e, m and m > 0
*/
uint32_t pow_mod(uint32_t b, uint32_t e, uint32_t m)
{
  if (b == 0) return 0;

  uint32_t result = 1;

  b = b % m;

  for (uint32_t i = 0; i < e; i++) {
    result = (result * b) % m;
  }

  return result;
}

void displayYourSharedSecret(uint16_t privateSecret) {
  uint16_t sharedSecret = pow_mod(g, privateSecret, p);
  Serial.print("My shared secret: ");
  Serial.println(sharedSecret);
}

void setup() {
  Serial.begin(9600);

  uint16_t privateSecret = getRandom();
  displayYourSharedSecret(privateSecret);

  uint16_t sharedIndex = readInOtherSharedSecret();
  encryptionKey = computeSharedEncryptionKey(sharedIndex);
}

void loop() {
  
}
