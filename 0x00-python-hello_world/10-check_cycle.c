#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a singly linked list
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{

	listint_t *fast_node = list;
	listint_t *slow_node = list;

	while (fast_node != NULL && slow_node != NULL)
	{
		fast_node = fast_node->next->next;
		slow_node = slow_node->next;
		if (fast_node == slow_node)
                        return (1);
	}
	return (0);
}
