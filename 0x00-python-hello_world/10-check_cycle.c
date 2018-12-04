#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop in it
 * @list: head of the linked list to check
 *
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list->next;

	while(slow && fast && fast->next)
	{
		if (slow == fast)
			return(1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
