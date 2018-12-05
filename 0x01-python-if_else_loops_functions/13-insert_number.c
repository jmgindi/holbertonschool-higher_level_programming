#include "lists.h"

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: pointer to head of list
 * @number: data for newnode->n
 *
 * Return: address of new node, NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	if (*head == NULL)
		*head = newnode;
	else
	{
		while (current->next != NULL)
		{
			if (number >= current->n && number <= current->next->n)
			{
				newnode->next = current->next;
				current->next = newnode;
				return (newnode);
			}
			else
				current = current->next;
		}
	}
	newnode->next = NULL;
	current->next = newnode;
	return (newnode);
}
