uint16_t encryption_key;

void setup() {
  Serial.begin(9600);

  uint16_t private_secret = get_private_secret();
  display_your_shared_index(private_secret);

  uint16_t shared_index = read_in_other_shared_index();
  encryption_key = compute_shared_encryption_key(shared_index);
}

void loop() {
  
}
