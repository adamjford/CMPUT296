int count_upper_case(char s[]) {
  char upper_case[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  int count = 0;
  int string_index = 0;
  int upper_case_index = 0;

  while(s[string_index] != '\0') {
    upper_case_index = 0;

    while(upper_case[upper_case_index] != '\0') {
      if(s[string_index] == upper_case[upper_case_index]) {
        count += 1;
        break;
      } 
      upper_case_index += 1;
    }

    string_index += 1;
  }

  return count;
}

int count_upper_case_v2(char s[]) {
  int count = 0;
  int string_index = 0;

  for (int i = 0; s[i] != '\0'; i++) {
    char current = s[i];
    int letter = current % 32; 
    if (letter > 0 && letter <= 26 && (current >> 5) == 2) {
      count += 1;
    }
  }

  return count;
}

void setup() {
  char str[] = "[{Hello WorldZz!@}]";
  Serial.begin(9600);
  Serial.println(count_upper_case(str));
  Serial.println(count_upper_case_v2(str));
}

void loop() {
}
