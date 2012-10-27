/* Simple Image Drawing
 *
 * Draws an image to the screen.    The image is stored in "parrot.lcd" on 
 * the SD card.    The image file contains only raw pixel byte-pairs.
 */

#include <Adafruit_GFX.h>      // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library
#include <SPI.h>
#include <SD.h>
#include "mem_syms.h"

#include "restaurant.h"

#define SD_CS      5  // Chip select line for SD card

#define BLOCK_LEN 512
Restaurant block_buf[BLOCK_LEN/sizeof(Restaurant)];

Sd2Card card;

#define RESTAURANT_START_BLOCK 4000000

Restaurant buffer[BLOCK_LEN/sizeof(Restaurant)];
uint32_t cachedBlockNumber;

void get_restaurant(int i, Restaurant *r) {
  uint32_t blockNumber = RESTAURANT_START_BLOCK + i/8;

  if(blockNumber != cachedBlockNumber) {
    card.readBlock(blockNumber, (uint8_t *) buffer);
    cachedBlockNumber = blockNumber;
  }

  uint32_t index = i % 8;

  (*r) = buffer[index];
}

void printRest(uint32_t restaurantNumber) {
  Restaurant r;
  get_restaurant(restaurantNumber, &r);
  Serial.print("Restaurant #");
  Serial.print(restaurantNumber);
  Serial.print(" Name: ");
  Serial.println(r.name);
}

void setup(void) {
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

    for(int i = 0; i < 1066; i++) {
      printRest(i);
    }
}

void loop() {
}
