/*
  Accepts an array of integers and modifies each
  element of the array by incrementing it by one.

  Parameters:
  array: an array of integers
  size: the number of items in the array
*/
void increment(int* array, uint32_t size) {
  for(uint32_t i = 0; i < size; i++) {
    array[i] += 1;
  }
}

void setup() {
  Serial.begin(9600);
  uint32_t size = 10;
  int array[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

  increment(array, size);

  for(uint32_t i = 0; i < size; i++) {
    Serial.println(array[i]);
  }
}

void loop() {
  
}
