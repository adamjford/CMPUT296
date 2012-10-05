void setup()
{
  Serial.begin(9600); 
}
 
void loop()
{
  uint32_t b, e, m;
  
  b = readlong();
  Serial.print("b=");
  Serial.print(b);
  Serial.print(" ");
  
  e = readlong();
  Serial.print("e=");
  Serial.print(e);
  Serial.print(" ");
  
  m = readlong();
  Serial.print("m=");
  Serial.print(m);
  Serial.print("\n");
  Serial.print("answer: ");  

  uint32_t time = micros();
  uint32_t result = pow_mod_v2(b, e, m);
  time = micros() - time;
  Serial.println(result);
  Serial.print("Time taken: ");
  Serial.println(time);
}
 
// common functions and procedures
 
/*
    Compute and return (b ** e) mod m
    For unsigned b, e, m and m > 0
*/
uint32_t pow_mod_v2(uint32_t b, uint32_t e, uint32_t m)
{
  if (b == 0) return 0;
  uint32_t v = b % m;
  uint32_t result = 1;

  for (uint32_t i = 0; e >> i; i++) {
    uint32_t mask = ((uint32_t)1) << i;
    if (e & mask) { /* Check the i'th bit */
      result = (result * v) % m;
    }
    v = (v * v) % m;
  }

  return result;
}
  
/* 
    Read a sequence characters from the serial monitor and interpret
    them as a decimal integer.
 
    The characters can be leading and tailing blanks, a leading '-',
    and the digits 0-9.
 
    Return that number as a 32 bit int.
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
