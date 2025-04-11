#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<limits.h>

typedef struct _Node{
    struct _Node *parent;
    struct _Node *left;
    struct _Node *right;
    int data;
}BSTN;

typedef struct _BST{
    struct _Node * root;
    int size;
}BST;

//insert, search, delete

void insert(BST *bst, int value);
int delete(BST *bst, int value);
BSTN *search(BST *bst, int value);
BSTN *findMinNodeFromRightSubTree(BSTN *subRoot);
int main(){

}

void insert(BST *bst, int value){
    BSTN *node = malloc(sizeof(BSTN));
    node->data = value;
    node->left = NULL;
    node->right = NULL;
    node->parent = NULL;

    if(bst->size == 0){
        bst->root = node;
    } else {
        BSTN *curr = bst->root;
        while (1) {
            if (value < curr->data) {
                if (curr->left == NULL) {
                    curr->left = node;
                    node->parent = curr;
                    break;
                } else {
                    curr = curr->left;
                }
            } else {
                if (curr->right == NULL) {
                    curr->right = node;
                    node->parent = curr;
                    break;
                } else {
                    curr = curr->right;
                }
            }
        }
    }

    bst->size++;
}

int delete(BST *bst, int value) {
    BSTN *node = search(bst, value);
    if (node == NULL) {
        printf("Node not found!\n");
        return -1;
    }

    BSTN *parent = node->parent;

    // 1. 자식이 없는 경우 (Leaf 노드)
    if (node->left == NULL && node->right == NULL) {
        if (parent == NULL) {
            bst->root = NULL;
        } else if (parent->left == node) {
            parent->left = NULL;
        } else {
            parent->right = NULL;
        }
        free(node);
    }

    // 2. 왼쪽 자식만 있는 경우
    else if (node->left != NULL && node->right == NULL) {
        if (parent == NULL) {
            bst->root = node->left;
        } else if (parent->left == node) {
            parent->left = node->left;
        } else {
            parent->right = node->left;
        }
        node->left->parent = parent;
        free(node);
    }

    // 3. 오른쪽 자식만 있는 경우
    else if (node->left == NULL && node->right != NULL) {
        if (parent == NULL) {
            bst->root = node->right;
        } else if (parent->left == node) {
            parent->left = node->right;
        } else {
            parent->right = node->right;
        }
        node->right->parent = parent;
        free(node);
    }

    // 4. 자식이 둘 다 있는 경우
    else {
        // 오른쪽 서브트리에서 최솟값 노드 찾기 (중위 후속자)
        BSTN *minNode = findMinNodeFromRightSubTree(node);

        // minNode가 node의 오른쪽 자식이 아닌 경우
        if (minNode->parent != node) {
            if (minNode->right != NULL) {
                minNode->parent->left = minNode->right;
                minNode->right->parent = minNode->parent;
            } else {
                minNode->parent->left = NULL;
            }
        }

        // minNode를 삭제 노드 자리로 이동
        minNode->left = node->left;
        minNode->right = (minNode == node->right) ? minNode->right : node->right;

        if (node->left != NULL)
            node->left->parent = minNode;
        if (node->right != NULL && node->right != minNode)
            node->right->parent = minNode;

        minNode->parent = node->parent;

        if (node->parent == NULL) {
            bst->root = minNode;
        } else if (node->parent->left == node) {
            node->parent->left = minNode;
        } else {
            node->parent->right = minNode;
        }

        free(node);
    }

    bst->size--;
    return 0;
}

BSTN* search(BST *bst, int value){
    BSTN *node = bst->root;
    while(node != NULL){
        if(node->data == value){
            return node;
        }else if(node->data > value){
            node = node->left;
        }else if(node->data < value){
            node = node->right;
        }
    }
    return NULL;
}

BSTN *findMinNodeFromRightSubTree(BSTN *subRoot){
    BSTN *node = subRoot->right;
    while (node && node->left != NULL){
        node = node->left;
    }
    return node;
}