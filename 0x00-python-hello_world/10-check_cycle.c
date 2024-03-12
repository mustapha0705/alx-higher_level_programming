#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint {
    int data;
    struct listint *next;
} listint_t;

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list) {
    listint_t *slow = list, *fast = list;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        /* If slow and fast pointers meet, there is a cycle */
        if (slow == fast)
            return 1;
    }
    /* If loop terminates, there is no cycle */
    return 0;
}

