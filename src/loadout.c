#include "loadout.h"
#include "constants.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

loadout *create_loadout(const char *name, const char *description,
                        const char icon) {
  loadout *ld = (loadout *)malloc(sizeof(loadout));
  if (!ld) {
    fprintf(stderr, "Failed to allocate memory for loadout\n");
    return NULL;
  }

  ld->name = name;
  ld->description = description;
  ld->icon = icon;

  item *items = (item *)malloc(sizeof(item));
  if (items == NULL) {
    free(ld);
    return NULL;
  }

  ld->item_count = 0;
  ld->max_item_count = 1;

  return ld;
}

/*1: could not add*/
int add_item_to_loadout(loadout *loadout, item *item) {
  if (loadout->item_count == loadout->max_item_count) {
    if (double_item_array(loadout) == ALLOCATION_FAILURE) {
      return 1;
    }
  }

  loadout->items[loadout->item_count] = *item;
  loadout->item_count += 1;

  return 0;
}

int double_item_array(loadout *loadout) {
  item *items = (item *)realloc(loadout->items, loadout->max_item_count * 2);

  if (items == NULL) {
    return ALLOCATION_FAILURE;
  }

  loadout->items = items;
  loadout->max_item_count *= 2;

  return 0;
}
