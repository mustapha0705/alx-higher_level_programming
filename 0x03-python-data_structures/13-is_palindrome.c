#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head, *fast_ptr = *head;
    listint_t *prev_slow_ptr = NULL, *second_half = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (is_palindrome);

    /* Get the middle of the list */
    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    /* Reverse the second half of the list */
    second_half = slow_ptr;
    prev_slow_ptr->next = NULL;
    reverse_list(&second_half);

    /* Compare the first half with the reversed second half */
    is_palindrome = compare_lists(*head, second_half);

    /* Restore the original list */
    reverse_list(&second_half);
    prev_slow_ptr->next = second_half;

    return (is_palindrome);
}

/**
 * reverse_list - Reverses a singly linked list
 * @head_ref: Pointer to the pointer to the head of the list
 */
void reverse_list(listint_t **head_ref)
{
    listint_t *prev = NULL, *current = *head_ref, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head_ref = prev;
}

/**
 * compare_lists - Compares two singly linked lists
 * @list1: Pointer to the head of the first list
 * @list2: Pointer to the head of the second list
 *
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);

        list1 = list1->next;
        list2 = list2->next;
    }

    return (1);
}

