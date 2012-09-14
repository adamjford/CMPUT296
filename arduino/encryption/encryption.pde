int16_t encryptionKey;

void setup() {
  encryptionKey = 42;
  
  Serial.begin(9600);
  Serial1.begin(9600);
}

int16_t encrypt(int16_t value, int16_t key) {
  //return (value + key) % 256;
  return value ^ key;
}

int16_t decrypt(int16_t value, int16_t key) {
  //return (value - key) % 256;
  return value ^ key;
}

void loop() {
  if (Serial1.available()) {
    int16_t inByte = Serial1.read();
    Serial.write(decrypt(inByte, encryptionKey));
  }
  if (Serial.available()) {
    int16_t inByte = Serial.read();
    Serial1.write(encrypt(inByte, encryptionKey));
  }
}
