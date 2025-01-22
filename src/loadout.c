#include "constants.h"
#include "loadout.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

loadout *create_loadout(const char *name, const char *description,
                        const char icon, size_t item_count) {
  loadout *ld = (loadout *)malloc(sizeof(loadout));
  if (!ld) {
    fprintf(stderr, "Failed to allocate memory for loadout\n");
    return NULL;
  }

  ld->name = strdup(name);
  ld->description = strdup(description);
  ld->icon = icon;

  return ld;
}

/*1: coult not add*/
int add_item_to_loadout(loadout *loadout, const item *item) {
  if (loadout->item_count == loadout->max_item_count) {
    int result = double_item_array(loadout);

    if (result == ALLOCATION_FAILURE) {
      return 1; 
    }
  }


  return 0;
}

int double_item_array(loadout *loadout) {
  item* items = (item*) realloc(loadout->items, loadout->max_item_count * 2);

  if (items == NULL) {
    return ALLOCATION_FAILURE;
  }

  loadout->items = items;


  return 0;
}
