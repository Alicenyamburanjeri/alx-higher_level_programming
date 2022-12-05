#include "lists.h"
#include <stdio.h>

/**
* insert_node - inserts a node into the right position
* in a sorted list
* @head: pointer to the head of the linked list
* @number: number to be added
* 
* Return: pointer to the list
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;

	if (!(*head) || current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
while (current->next)
		{
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
	}
	return (new);
}
