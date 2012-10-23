#include <Arduino.h>

typedef struct {
  int16_t x;
  int16_t y;
} position_t;

uint16_t manhattan_dist(position_t *pos1, position_t *pos2) {
  return abs((int32_t)pos1->x - (int32_t)pos2->x) + abs((int32_t)pos1->y - (int32_t)pos2->y);
}

uint16_t crow_dist(position_t *pos1, position_t *pos2) {
  return sqrt(pow(pos1->x - pos2->x, 2) + pow(pos1->y - pos2->y, 2));
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
  test_distances(-100, -100, 100, 100);
  test_distances(100, -100, 100, -100);
  test_distances(-100, 100, -100, 100);
  test_distances(100, -100, -100, 100);
  test_distances(-100, 100, 100, -100);
}

void loop() {
  
}
