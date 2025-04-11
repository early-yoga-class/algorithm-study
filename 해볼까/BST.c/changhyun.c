#include <stdio.h>
#include <stdlib.h>

typedef struct _node{
    int data;
    struct _node *left;
    struct _node *right;
}Node;

Node* search(Node* node, int target);
Node* insert(Node* node, int value);
Node* delete(Node* node, int value);
Node* findMinNode(Node *node);
void print(Node* node);

Node* search(Node* node, int target){
    if(node == NULL) return NULL;
    
    if(node->data == target){
        return node;
    }else if(node->data < target){
        return search(node->right, target);
    }else{
        return search(node->left, target);
    }
}

Node* insert(Node* node, int value){
    if(node == NULL){
        node = (Node*)malloc(sizeof(Node));
        node->left = NULL;
        node->right = NULL;
        node->data = value;
        return node;
    }

    if (node->data > value){
        node->left = insert(node->left, value);
    }else{
        node->right = insert(node->right, value);
    }
    return node;
}

Node* delete(Node* node, int value){
    if(!node) return NULL;
    Node* temp = NULL;

    if(node->data > value){
        node->left = delete(node->left, value);
    }else if(node->data < value){
        node->right = delete(node->right, value);
    }else{
        if (node->right && node->left){
            temp = findMinNode(node->right);
            node->data = temp->data;
            node->right = delete(node->right, temp->data);
        }else{
            temp = (!node->left) ? node->right:node->left;
            free(node);
            return temp;
        }
    }
    return node;
}

Node* findMinNode(Node *node){
    if (!node) return NULL;

    Node *current = node;
    while(current->left) current = current->left;
    
    return current;
}

void print(Node* node){
    if(node == NULL) return;

    printf("%d ", node->data);
    print(node->left);
    print(node->right);
}

int main() {
    Node *root = NULL;
    int c, i, j;
	c = 1;

    printf("1: Insert an integer to the bst:\n");
    printf("2: search node in bst\n");
    printf("3: delete node in bst\n");
	printf("4: Print the bst:\n");

	while (c != 0)
	{
		printf("\nPlease input your choice(1/2/3/4/0): ");
		scanf("%d", &c);

		switch (c)
		{
		case 1:
			printf("Input an integer that you want to add to the linked list: ");
			scanf("%d", &i);
			printf("The resulting Binary Search Tree is: ");
            root = insert(root, i);
			print(root);
			break;
		case 2:
			printf("Input an integer that you want to search to the binary search tree: ");
            scanf("%d", &i);
            Node* found = search(root, i);
            if(found) printf("Found : %d\n", found->data);
            else printf("Not found.\n");
			break;
        case 3:
            printf("Input an integer that you want to delete to the binary search tree: ");
            scanf("%d", &i);
            root = delete(root, i);
            print(root);
            break;
        case 4:
            print(root);
            break;
		default:
			printf("Choice unknown;\n");
			break;
		}
	}
    return 0;
}