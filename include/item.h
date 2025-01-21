#ifndef ITEM_H
#define ITEM_H

typedef struct {
  const char *name;
  const char *description;
  const char *category;

  int weight; // in grams

  int is_worn;
  int is_favourite;
  int is_water;
  int is_food;
} item;

item *create_item(const char *name, const char *description, const char* category, int weight);

#endif // !ITEM_H
