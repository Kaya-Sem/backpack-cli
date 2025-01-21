#include "item.h"
#include <cstddef>

typedef struct {
  char *name;
  char *description;
  char icon;

  item items[];

} loadout;

loadout *create_loadout(const char *name, const char *description, char icon,
                        size_t item_count);
