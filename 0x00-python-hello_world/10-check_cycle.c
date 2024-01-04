#include "lists.h"

/**
 * check_cycle - singly linked list
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
		return (0);

	t = list;
	h = list->next;

	while (h != NULL && h->next != NULL)
	{
		if (t == h)
			return (1);

		t = t->next;
		h = h->next->next;
	}

	return (0);
}

