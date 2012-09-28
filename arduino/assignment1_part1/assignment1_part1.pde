uint16_t encryptionKey;

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

void setup() {
  Serial.begin(9600);

  uint16_t privateSecret = getRandom();
  displayYourSharedSecret(privateSecret);

  uint16_t sharedIndex = readInOtherSharedSecret();
  encryptionKey = computeSharedEncryptionKey(sharedIndex);
}

void loop() {
  
}
