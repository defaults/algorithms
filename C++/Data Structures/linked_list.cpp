#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct node
{
	int data;
	struct node *next;
};

// This function prints contents of linked list starting from
// the given node
void printList(struct node *n)
{
	while (n != NULL)
	{
		 printf(" %d ", n->data);
		 n = n->next;
	}
}

int main(int argc, char *argv[]) {
	struct node* head = NULL;
	struct node* second = NULL;
	struct node* third = NULL;

	// allocate 3 nodes in the heap
	head  = (struct node*)malloc(sizeof(struct node));
	second = (struct node*)malloc(sizeof(struct node));
	third  = (struct node*)malloc(sizeof(struct node));

	//assign data and link
	head->data = 1;
	head->next = second;

	second->data = 2;
	second->next = third;

	third->data = 3;
	third->next = NULL;

	printList(head);

	return 0;
}