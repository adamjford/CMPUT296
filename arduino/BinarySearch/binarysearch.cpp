#include <Arduino.h>
#include <stdlib.h>

// type of things to be sorted and searched
typedef struct { 
  int16_t x; 
  int16_t y; 
} item_t; 

void print_item(item_t a) {
  Serial.print("{");
  Serial.print(a.x);
  Serial.print(",");
  Serial.print(a.y);
  Serial.print("}");
}

void print_list(item_t *list, size_t len) {
  for (size_t i=0; i < len; i++) {
    print_item(list[i]);
    Serial.print(" ");
  }
  Serial.println();
}

// the comparison function for things of type item_t
int16_t item_compare (const item_t *a, const item_t *b) {
  // Question: what happens if we return a-b instead?
  int16_t diff = a->x - b->x;
  if(diff == 0) {
    diff = a->y - b->y;
  }
  return diff;
}

// the test to see if a list of things of type item_t is in ascending order
//uint8_t is_in_order(item_t *list, size_t len) {
uint8_t is_in_order(void *list, size_t len, size_t width, int (*compar)(const void *, const void *)) {
  for (size_t i=0; i < len-1; i++) {
    void* item1 = (char *)list + (width*i);
    void* item2 = (char *)list + (width*(i+1));
    if (compar(item1, item2) > 0 ) {
      // out of order
      return 0;
    }
  }
  // ok, it's in order
  return 1;
}

// Question: how would you write a generic is_in_order function similar to
// qsort and bsearch?

void setup() {
  size_t n_items = 32;
  item_t list[n_items];

  item_t  e_first;
  item_t  e_mid;
  item_t  e_last;

  Serial.begin(9600);

  // generate a random list of item_t things
  for (size_t i=0; i < n_items; i++) {
    list[i].x = random(0, 32);
    list[i].y = random(0, 32);
  }

  print_list(list, n_items);

  // pick the original first, mid, and last elements
  e_first = list[0];
  e_mid = list[n_items/2];
  e_last = list[n_items-1];

  Serial.print("first "); print_item(e_first);
  Serial.print(" mid "); print_item(e_mid);
  Serial.print(" last "); print_item(e_last);
  Serial.println();

  // now sort them
  qsort(list, n_items, sizeof(item_t), (__compar_fn_t) item_compare);

  print_list(list, n_items);

  // are they sorted?
  if ( is_in_order(list, n_items, sizeof(item_t), (__compar_fn_t) item_compare) ) {
    Serial.println("OK, list is in order");
  }
  else {
    Serial.println("ERROR, list is out of order");
  }

  // find the sorted positions of the first, mid, and last

  // note that bsearch returns a pointe to the item, but you can
  // get it's index by simply subtracting the base address of the list

  item_t *i_first = 
    (item_t *) bsearch(&e_first, list, n_items, sizeof(item_t), 
        (__compar_fn_t) item_compare);

  item_t *i_mid = 
    (item_t *) bsearch(&e_mid, list, n_items, sizeof(item_t), 
        (__compar_fn_t) item_compare);

  item_t *i_last = 
    (item_t *) bsearch(&e_last, list, n_items, sizeof(item_t), 
        (__compar_fn_t) item_compare);

  // note the subtraction to get the index

  Serial.print("i_first "); Serial.print(i_first - list);
  Serial.print(" i_mid "); Serial.print(i_mid - list);
  Serial.print(" i_last "); Serial.print(i_last - list);
  Serial.println();

  // now let's look for something that is not there
  item_t missing;
  missing.x = -1;
  missing.y = -1;

  item_t *i_missing = 
    (item_t *) bsearch(&missing, list, n_items, sizeof(item_t), 
        (__compar_fn_t) item_compare);
  Serial.print("Result of search for "); print_item(missing); 
  Serial.print(" is " ); Serial.print((int) i_missing);
  Serial.println();


}

void loop() {
}
