int mod(int a, int b) {
  int result;
  if(b == 0) {
    return 0;
  } else {
    if(a < 0) {
      a = -a;
    }
    if(b < 0) {
      b = -b;
    }

    return a % b;
  }
}

void to_upper(char s[]) {
  for(int i = 0; s[i] != '\0'; i++) {
    if(s[i] >= 'a' && s[i] <= 'z') {
      s[i] = s[i] ^ 32;
    }
  }
}

void setup() {
  Serial.begin(9600);

  Serial.println("11 % 4: ");
  Serial.print("Arduino: ");
  Serial.println(11 % 4);
  Serial.print("Custom: ");
  Serial.println(mod(11, 4));

  Serial.println("11 % -4: ");
  Serial.print("Arduino: ");
  Serial.println(11 % -4);
  Serial.print("Custom: ");
  Serial.println(mod(11, -4));

  Serial.println("-11 % 4: ");
  Serial.print("Arduino: ");
  Serial.println(-11 % 4);
  Serial.print("Custom: ");
  Serial.println(mod(-11, 4));

  Serial.println("-11 % -4: ");
  Serial.print("Arduino: ");
  Serial.println(-11 % -4);
  Serial.print("Custom: ");
  Serial.println(mod(-11, -4));

  char string[] = "[{Hello WorldZz!}]";
  to_upper(string);
}

void loop() {
  
}
