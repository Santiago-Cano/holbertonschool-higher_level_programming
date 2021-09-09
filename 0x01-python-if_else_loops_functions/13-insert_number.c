#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: head node of singly linked list
 * @number: number to insert in sorted singly linked list
 * Return: address to new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *tmp;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	tmp = *head;

	if (*head == NULL || newnode->n <= tmp->n)
	{
		newnode->next = tmp;
		*head = newnode;
		return (newnode);
	}

	while (tmp->next != NULL)
	{
		if (tmp->next->n >= number)
		{
			newnode->next = tmp->next;
			tmp->next = newnode;
			return (newnode);
		}
		tmp = tmp->next;
	}

	tmp->next = newnode;
	newnode->next = NULL;
	return (newnode);
}
