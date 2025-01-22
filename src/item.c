#include "../include/item.h"
#include <stdlib.h>

item *create_item(const char *name, const char *description,
                  const char *category, int weight) {
  item *i = (item *)malloc(sizeof(item));

  i->name = name;
  i->description = description;
  i->category = category;
  i->weight = weight;

  return i;
}
