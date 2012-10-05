/*  CMPUT 296/114 - Assignment 1 Part 2 - Due 2012-10-09

    By: Adam Ford

    This assignment is a solo effort, and
    any extra resources are cited in the code below.

*/
uint16_t privateSecret;
uint16_t sharedSecret;
uint32_t p = 2147483647;
uint32_t g = 16807;

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
    Source: class discussions
*/
uint32_t pow_mod(uint32_t b, uint32_t e, uint32_t m)
{
  if (b == 0) return 0;
  uint32_t v = b % m;
  uint32_t result = 1;

  for (uint32_t i = 0; e >> i; i++) {
    uint32_t mask = ((uint32_t)1) << i;
    if (e & mask) { /* Check the i'th bit */
      result = mul_mod(result, v, m);
    }
    v = mul_mod(v, v, m);
  }

  return result;
}

uint32_t mul_mod(uint32_t a, uint32_t b, uint32_t m) {
  uint32_t result = 0;

  if(a && b && m) {
    uint32_t v = b % m;
    for (uint32_t i = 0; a >> i; i++) {
      uint32_t mask = ((uint32_t)1) << i;
      if (a & mask) {
        result = (result + v) % m;
      }
      v = (v << 1) % m;
    }
  }

  return result;
}

/* 
    Read a sequence characters from the serial monitor and interpret
    them as a decimal integer.
 
    The characters can be leading and tailing blanks, a leading '-',
    and the digits 0-9.
 
    Return that number as a 32 bit int.
    Source: Tangible Computing Notes - 7. Diffie-Hellman Key Exchange
*/
int32_t readlong()
{
  char s[128]; /* 128 characters should be more than enough. */
  readline(s, 128);
  return atol(s);
}
 
/* 
    Read a \n terminated line from the serial monitor and store the result 
    in string s.
 
    String s has maximum size, including the terminating \0, of bufsize
    characters.  If the input line is longer than can be stored in s, then
    it is truncated.  bufsize must be at least 1.
 
    s will always be a properly terminted string.
    Source: Tangible Computing Notes - 7. Diffie-Hellman Key Exchange
*/
void readline(char *s, int bufsize)
{
  uint8_t i = 0;
  
  while( i < bufsize-1 ) {
    while (Serial.available() == 0) { } /* Do nothing */
 
    s[i] = Serial.read();
 
    if (s[i] == '\n' || s[i] == '\0') break;
    i += 1;
  }
  // \0 teminate the string
  s[i] = '\0';
}

uint16_t computeSharedSecretEncryptionKey(uint16_t sharedIndex) {
  return pow_mod(sharedIndex, privateSecret, p);
}

/* Source: Tangible Computing Notes */
uint16_t encryptOrDecrypt(uint16_t value, uint16_t key) {
  return value ^ key;
}

void sendMySharedIndex(uint32_t sharedIndex) {
  uint32_t mask = 0xFF;
  Serial1.write(sharedIndex & mask);
  Serial1.write((sharedIndex << 8) & mask);
  Serial1.write((sharedIndex << 16) & mask);
  Serial1.write((sharedIndex << 24) & mask);
}

uint32_t readYourSharedIndex() {
  while(Serial1.available() < 4) {
    /* Wait until all bytes of 32-bit shared index are available */
  }

  return Serial1.read() | Serial1.read() << 8 | Serial1.read() << 16 | Serial1.read() << 24;
}

int digitalOutput = 10;
int digitalInput = 11;

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  pinMode(digitalOutput, OUTPUT);
  pinMode(digitalInput, INPUT);

  digitalWrite(digitalOutput, HIGH);

  Serial.println("Waiting for other device to be ready...");

  while(!digitalRead(digitalInput)) {
    /* Wait for other device to signal that they are ready */
  }
  
  Serial.println("Other device found!");

  privateSecret = getRandom();
  uint32_t sharedIndex = pow_mod(g, privateSecret, p);
  Serial.print("My shared index: ");
  Serial.println(sharedIndex);

  sendMySharedIndex(sharedIndex);
  uint32_t yourSharedIndex = readYourSharedIndex();
  Serial.print("Your shared index: ");
  Serial.println(yourSharedIndex);

  sharedSecret = computeSharedSecretEncryptionKey(yourSharedIndex);

  Serial.println("Waiting for input...");
}

/* Source: Tangible Computing Notes */
void loop() {
  while (Serial1.available()) {
    randomSeed(sharedSecret);
    char character;
    do {
      uint8_t encryptionKey = random(0xFF);
      character = encryptOrDecrypt(Serial1.read(), encryptionKey);
      Serial.write(character);
    } while (character != '\n');
  }

  while (Serial.available()) {
    randomSeed(sharedSecret);
    char character;
    do {
      uint8_t encryptionKey = random(0xFF);
      character = encryptOrDecrypt(Serial.read(), encryptionKey);
      Serial1.write(character);
    } while (character != '\n');
  }
}

