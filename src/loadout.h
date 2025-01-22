#ifndef LOADOUT_H
#define LOADOUT_H

#include "item.h"
#include <stddef.h>

typedef struct {
  const char *name;
  const char *description;
  char icon;
  item *items;
  size_t item_count;
  size_t max_item_count;
} loadout;

loadout *create_loadout(const char *name, const char *description,
                        const char icon);

int add_item_to_loadout(loadout *loadout, item *item);

int double_item_array(loadout *loadout);

#endif // LOADOUT_H
