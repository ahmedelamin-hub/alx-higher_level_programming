#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a numb
 * @head: pointer
 * @number: value
 * Return: addres
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n, *c;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);

	n->n = number;
	n->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		n->next = *head;
		*head = n;
		return (n);
	}

	c = *head;
	while (c->next != NULL && c->next->n < number)
		c = c->next;

	n->next = c->next;
	c->next = n;

	return (n);
}

