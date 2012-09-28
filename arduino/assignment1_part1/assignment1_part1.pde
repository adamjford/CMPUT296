uint16_t privateSecret;
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

/* 
    Read a sequence characters from the serial monitor and interpret
    them as a decimal integer.
 
    The characters can be leading and tailing blanks, a leading '-',
    and the digits 0-9.
 
    Return that number as a 32 bit int.
    Source: Tangle Computing Notes - 7. Diffie-Hellman Key Exchange
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
    Source: Tangle Computing Notes - 7. Diffie-Hellman Key Exchange
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

uint16_t readInOtherSharedSecret() {
  Serial.println("Input other shared secret: ");
  return readlong();
}

uint16_t computeSharedSecretEncryptionKey(uint16_t sharedIndex) {
  return pow_mod(sharedIndex, privateSecret, p);
}

void setup() {
  Serial.begin(9600);

  privateSecret = getRandom();
  displayYourSharedSecret(privateSecret);

  uint16_t sharedIndex = readInOtherSharedSecret();
  encryptionKey = computeSharedSecretEncryptionKey(sharedIndex);
}

void loop() {
  
}
