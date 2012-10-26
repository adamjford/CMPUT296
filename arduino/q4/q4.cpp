#include <Arduino.h>

typedef struct {
  int16_t x;
  int16_t y;
} position_t;

const uint16_t UINT_MAX = 65535;

/*
 * Shrinks a 32-bit unsigned integer to a 16-bit one.
 * If the value is larger than what can fit in a 16-bit integer,
 * it returns the maximum.
 */
uint16_t shrink(uint32_t value) {
  if(value > UINT_MAX){
    return UINT_MAX;
  }
  return value;
}

/* 
 * Return the Manhattan distance between two positions.
 * If the distance is greater than 65535, 65535 is returned instead.
 */
uint16_t manhattan_dist(position_t *pos1, position_t *pos2) {
  uint32_t result = abs((int32_t)pos1->x - (int32_t)pos2->x) + abs((int32_t)pos1->y - (int32_t)pos2->y);
  return shrink(result);
}

/* 
 * Return the straight-line distance between two positions.
 * If the distance is greater than 65535 or , 65535 is returned instead.
 */
uint16_t crow_dist(position_t *pos1, position_t *pos2) {
  int32_t x_diff = (int32_t)pos1->x - (int32_t)pos2->x;
  int32_t y_diff = (int32_t)pos1->y - (int32_t)pos2->y;
  if(x_diff > UINT_MAX || y_diff > UINT_MAX) {
    return UINT_MAX;
  }

  uint32_t x_power = (uint32_t)(x_diff * x_diff);
  uint32_t y_power = (uint32_t)(y_diff * y_diff);

  /* If both squared numbers are bigger than 2^31,
   * then adding them together will overflow.
   * */
  if(x_power > 2147483647 && y_power > 2147483647) {
    return UINT_MAX;
  } else {
    uint32_t result = sqrt(x_power + y_power);
    return shrink(result);
  }
}

void test_distances(int16_t x1, int16_t y1, int16_t x2, int16_t y2) {
  position_t pos1 = {x1, y1};
  position_t pos2 = {x2, y2};

  Serial.print("Testing distance between (");
  Serial.print(pos1.x);
  Serial.print(",");
  Serial.print(pos1.y);
  Serial.print(") and (");
  Serial.print(pos2.x);
  Serial.print(",");
  Serial.print(pos2.y);
  Serial.println(")");
  Serial.print("Manhattan distance: ");
  Serial.println(manhattan_dist(&pos1, &pos2));
  Serial.print("Straight-line distance:");
  Serial.println(crow_dist(&pos1, &pos2));
  Serial.println("");
}

void setup() {
  Serial.begin(9600);

  test_distances(0, 0, 0, 0);
  test_distances(100, 100, 200, 200);
  test_distances(-100, -100, -200, -200);
  test_distances(100, 100, -200, -200);
  test_distances(-100, -100, 200, 200);
  test_distances(1, 2, 3, 4);
  test_distances(-1, -2, 3, 4);
  test_distances(1, 2, -3, -4);
  test_distances(14000, 14000, -14000, -14000);
  test_distances(32700, 32700, -32700, -32700);
  test_distances(32767, 32767, 32767, 32767);
  test_distances(-32768, -32768, -32768, -32768);
  test_distances(-32768, -32768, 32767, 32767);
  test_distances(32767, 32767, -32768, -32768);
  test_distances(32767, -32768, 32767, -32768);
  test_distances(32767, -32768, -32768, 32767);
  test_distances(32767, -32768, -32768, 32767);
  test_distances(-32768, 32767, -32768, 32767);
}

void loop() {
  
}
