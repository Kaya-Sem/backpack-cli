#include "../libs/WiTUI/include/wi_tui.h"
#include "item.h"
#include "loadout.h"
#include <asm-generic/ioctls.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>

bool FULLSCREEN = 1;

unsigned int get_shell_height();
void start_tui(loadout *loadouts, unsigned long amount_loadouts);
void populate_loadout_list(wi_window *loadout_window, loadout *loadouts,
                           int items_size);

int main() {

  loadout *loadout1 = create_loadout("Kungsleden", "mooi zweden", 'h');
  item *item1 = create_item("my item", "my_description", "shelter", 100);

 // add_item_to_loadout(loadout1, item1);

  loadout loadouts[5] = {*loadout1};

  start_tui(loadouts, 5);

  return 0;
}

void start_tui(loadout *loadouts, unsigned long amount_loadouts) {

  /* session*/
  wi_session *session = wi_make_session(1);
  session->start_clear_screen = FULLSCREEN;

  /* gear list window*/
  wi_window *loadout_window = wi_make_window();

  loadout_window->cursor_rendering = LINEBASED;
  loadout_window->width = 30;
  loadout_window->border.title = " Gear Loadouts ";
  loadout_window->border.title_alignment = RIGHT;
  loadout_window->border.footer = " footer ";
  loadout_window->height = get_shell_height() - 3;

  /* detailed gear window view*/
  wi_window *detailed_gear_list = wi_make_window();
  detailed_gear_list->cursor_rendering = INVISIBLE;

  populate_loadout_list(loadout_window, loadouts, amount_loadouts);

  wi_add_content_to_window(detailed_gear_list, "", (wi_position){0, 0});

  wi_add_window_to_session(session, loadout_window, 0);
  wi_add_window_to_session(session, detailed_gear_list, 0);
  wi_show_session(session);
}

unsigned int get_shell_height() {
  struct winsize w;
  ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);

  return w.ws_row;
}



void populate_loadout_list(wi_window *loadout_window, loadout *loadouts,
                           int items_size) {

  // Calculate the total size needed
  size_t total_length = 1; // 1 for the null terminator
  for (int i = 0; i < items_size; i++) {
    total_length += strlen(loadouts[i].name) + 1; // Add 1 for the newline
  }

  // Allocate memory for the resulting string
  char *window_string = (char *)malloc(total_length);
  if (window_string == NULL) {
    fprintf(stderr, "Memory allocation for window failed.\n");
    return;
  }

  // Build the string by concatenating the list items
  window_string[0] = '\0'; // Ensure the string starts empty
  for (int i = 0; i < items_size; i++) {
    strcat(window_string, loadouts[i].name);
    strcat(window_string, "\n");
  }

  wi_add_content_to_window(loadout_window, window_string, (wi_position){0, 0});

  free(window_string);
}

