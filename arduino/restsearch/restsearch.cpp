#include <Arduino.h>
#include <stdlib.h>
#include <string.h>
#include <SPI.h>
#include <SD.h>
#include "mem_syms.h"

#include "wiring_conventions.h"

#include "restaurant.h"

#define RESTAURANTS_COUNT 50

Sd2Card card;

int compare(const void *p1, const void *p2) {
  uint16_t* index1 = (uint16_t*)p1;
  uint16_t* index2 = (uint16_t*)p2;

  Restaurant rest1;
  Restaurant rest2;

  getRestaurant(*index1, &rest1, &card);
  getRestaurant(*index2, &rest2, &card);

  int value = strcmp(rest1.name, rest2.name);

  Serial.print("Comparing index #");
  Serial.print(*index1);
  Serial.print(": ");
  Serial.print(rest1.name);
  Serial.print(" and index #");
  Serial.print(*index2);
  Serial.print(": ");
  Serial.println(rest2.name);
  Serial.print("Value: ");
  Serial.println(value);

  return value;
}

void setup() {
  Serial.begin(9600);

  Serial.print("Initializing SD card...");
  if (!SD.begin(SD_CS)) {
    Serial.println("failed!");
    return;
  }
  Serial.println("OK!");

  // test out reading blocks from the SD card
  if (!card.init(SPI_HALF_SPEED, SD_CS)) {
      Serial.println("Raw SD Initialization has failed");
      while (1) {};  // Just wait, stuff exploded.
  }

  uint16_t Indexes[RESTAURANTS_COUNT];

  for(int i = 0; i < RESTAURANTS_COUNT; i++) {
    Indexes[i] = i;
  }

  qsort(Indexes, RESTAURANTS_COUNT, sizeof(uint16_t), &compare);

  Restaurant rest;
  for(int i = 0; i < RESTAURANTS_COUNT; i++) {
    getRestaurant(Indexes[i], &rest, &card);
    Serial.print("#");
    Serial.print(Indexes[i]);
    Serial.print(": ");
    Serial.println(rest.name);
  }
}

void loop() {
}

