#include "item.h"

typedef struct {
  char *name;
  char *description;
  char icon;

  item items[];

} loadout;
