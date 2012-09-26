void setup()
{
  Serial.begin(9600); 
}
 
void loop()
{
  uint32_t b, e, m;
  
  b = readlong();
  Serial.print(b);
  Serial.print(" ");
  
  e = readlong();
  Serial.print(e);
  Serial.print(" ");
  
  m = readlong();
  Serial.print(m);
  Serial.print("\n");
 
  Serial.print("answer = ");  
  Serial.println(pow_mod(b, e, m));
}
 
// common functions and procedures
 
/*
    Compute and return (b ** e) mod m
    For unsigned b, e, m and m > 0
*/
uint32_t pow_mod(uint32_t b, uint32_t e, uint32_t m)
{
  return 0;
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
    // wait for a character 
    while (Serial.available() == 0) { } /* Do nothing */
 
    // grab the character and save in the buffer
    s[i] = Serial.read();
 
    // if end of line or somehow a \0 got sent, we are done
    if (s[i] == '\n' || s[i] == '\0') break;
    i += 1;
  }
  // \0 teminate the string
  s[i] = '\0';
}