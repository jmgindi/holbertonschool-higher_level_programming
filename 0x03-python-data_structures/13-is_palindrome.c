#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: list to check
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int i, len, check;
	int *pal_check;
	listint_t *temp = *head;

	if (head == NULL)
		return (1);

	for (len = 0; temp->next != NULL; len++)
		temp = temp->next;

	pal_check = malloc(sizeof(int) * len);
	temp = *head;

	for (i = 0; temp != NULL; i++)
	{
		pal_check[i] = temp->n;
		temp = temp->next;
	}

	check = len/2;

	for (i = 0; i <= check; i++)
	{
		if (pal_check[i] == pal_check[len - (i)])
			;
		else
			return (0);
	}
	return (1);
}
