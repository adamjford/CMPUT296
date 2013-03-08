#include <Arduino.h>
#include <Adafruit_ST7735.h>
#include <SD.h>
#include <mem_syms.h>

#include "map.h"

extern Adafruit_ST7735 tft;

const int INSIDE = 0; // 0000
const int LEFT = 1;   // 0001
const int RIGHT = 2;  // 0010
const int BOTTOM = 4; // 0100
const int TOP = 8;    // 1000

// Compute the bit code for a point (x, y) using the clip rectangle
// bounded diagonally by (xmin(), ymin()), and (xmax(), ymax())

int32_t xmin() {
    return screen_map_x;
}

int32_t xmax() {
    return screen_map_x + display_window_width;
}

int32_t ymin() {
    return screen_map_y;
}

int32_t ymax() {
    return screen_map_y + display_window_height;
}

// Source: http://en.wikipedia.org/w/index.php?title=Cohen%E2%80%93Sutherland_algorithm&oldid=535367724
int ComputeOutCode(int32_t x, int32_t y)
{
    int code;

    code = INSIDE;          // initialised as being inside of clip window

    if (x < xmin())           // to the left of clip window
        code |= LEFT;
    else if (x > xmax())      // to the right of clip window
        code |= RIGHT;
    if (y < ymin())           // below the clip window
        code |= BOTTOM;
    else if (y > ymax())      // above the clip window
        code |= TOP;

    return code;
}

// Cohen–Sutherland clipping algorithm clips a line from
// P0 = (x0, y0) to P1 = (x1, y1) against a rectangle with 
// diagonal from (xmin(), ymin()) to (xmax(), ymax()).
// Source: http://en.wikipedia.org/w/index.php?title=Cohen%E2%80%93Sutherland_algorithm&oldid=535367724
void CohenSutherlandLineClipAndDraw(int32_t x0, int32_t y0, int32_t x1, int32_t y1)
{
    // compute outcodes for P0, P1, and whatever point lies outside the clip rectangle
    int outcode0 = ComputeOutCode(x0, y0);
    int outcode1 = ComputeOutCode(x1, y1);
    bool accept = false;

    while (true) {
        if (!(outcode0 | outcode1)) { // Bitwise OR is 0. Trivially accept and get out of loop
            accept = true;
            break;
        } else if (outcode0 & outcode1) { // Bitwise AND is not 0. Trivially reject and get out of loop
            break;
        } else {
            // failed both tests, so calculate the line segment to clip
            // from an outside point to an intersection with clip edge
            int32_t x, y;

            // At least one endpoint is outside the clip rectangle; pick it.
            int outcodeOut = outcode0 ? outcode0 : outcode1;

            // Now find the intersection point;
            // use formulas y = y0 + slope * (x - x0), x = x0 + (1 / slope) * (y - y0)
            if (outcodeOut & TOP) {           // point is above the clip rectangle
                x = x0 + (x1 - x0) * (ymax() - y0) / (y1 - y0);
                y = ymax();
            } else if (outcodeOut & BOTTOM) { // point is below the clip rectangle
                x = x0 + (x1 - x0) * (ymin() - y0) / (y1 - y0);
                y = ymin();
            } else if (outcodeOut & RIGHT) {  // point is to the right of clip rectangle
                y = y0 + (y1 - y0) * (xmax() - x0) / (x1 - x0);
                x = xmax();
            } else if (outcodeOut & LEFT) {   // point is to the left of clip rectangle
                y = y0 + (y1 - y0) * (xmin() - x0) / (x1 - x0);
                x = xmin();
            }

            // Now we move outside point to intersection point to clip
            // and get ready for next pass.
            if (outcodeOut == outcode0) {
                x0 = x;
                y0 = y;
                outcode0 = ComputeOutCode(x0, y0);
            } else {
                x1 = x;
                y1 = y;
                outcode1 = ComputeOutCode(x1, y1);
            }
        }
    }
    if (accept) {
        // Need to first convert x/y values for whole map to x/y values on Adafruit screen
        tft.drawLine(x0 - screen_map_x, y0 - screen_map_y, x1 - screen_map_x, y1 - screen_map_y, BLUE);
    }
}
