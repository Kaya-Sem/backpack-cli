#include "../libs/WiTUI/include/wi_tui.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void populate_loadout_list(wi_window *loadout_window, char* items[], int items_size) ;

int main() {

  /* session*/
  wi_session *session = wi_make_session(1);
  session->start_clear_screen = 1;

  /* gear list window*/
  wi_window *loadout_window = wi_make_window();

  printf("populating list");
  loadout_window->cursor_rendering = LINEBASED;
  loadout_window->width = 30;
  loadout_window->border.title = " Gear Loadouts ";
  loadout_window->border.title_alignment = RIGHT;
  loadout_window->border.footer = " footer ";

  /* detailed gear window view*/
  wi_window *detailed_gear_list = wi_make_window();
  detailed_gear_list->cursor_rendering = INVISIBLE;

  char *my_text = "hi";

char *list[5] = {"Kungsleden 2022", "Alta Via 3", "FKT GR11",
                     "Tour Du Mont Blanc", "Camino de Santiago"};

  populate_loadout_list(loadout_window, list, 5);


  wi_add_content_to_window(detailed_gear_list, my_text, (wi_position){0, 0});

  wi_add_window_to_session(session, loadout_window, 0);
  wi_add_window_to_session(session, detailed_gear_list, 0);
  wi_show_session(session);

  return 0;
}

void populate_loadout_list(wi_window *loadout_window, char* items[], int items_size) {
    
    // Calculate the total size needed
    size_t total_length = 1; // 1 for the null terminator
    for (int i = 0; i < items_size; i++) {
        total_length += strlen(items[i]) + 1; // Add 1 for the newline or separator
    }

    // Allocate memory for the resulting string
    char *window_string = (char *)malloc(total_length);
    if (window_string == NULL) {
        fprintf(stderr, "Memory allocation  for window failed.\n");
        return;
    }

    // Build the string by concatenating the list items
    window_string[0] = '\0'; // Ensure the string starts empty
    for (int i = 0; i < items_size; i++) {
        strcat(window_string, items[i]);
        strcat(window_string, "\n");
    }

    wi_add_content_to_window(loadout_window, window_string, (wi_position){0, 0});

    free(window_string);
}

typedef struct {
  char* name;
  char* description;
} item;
