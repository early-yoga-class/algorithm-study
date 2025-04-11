#include <stdio.h>
#include <stdlib.h>

// BST의 노드 구조 정의
typedef struct Node {
    int data;               // 저장할 값
    struct Node *left;      // 왼쪽 자식
    struct Node *right;     // 오른쪽 자식
} Node;

// 새로운 노드를 동적으로 생성
Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));  // 메모리 할당
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// BST에 값 삽입 (재귀 사용)
Node* insert(Node* root, int value) {
    if (root == NULL) return createNode(value);   // 비어있으면 새 노드 생성

    if (value < root->data)
        root->left = insert(root->left, value);   // 작으면 왼쪽에 삽입
    else if (value > root->data)
        root->right = insert(root->right, value); // 크면 오른쪽에 삽입
    // 같은 값은 무시 (중복 없음)
    return root;
}

// 중위 순회 (왼쪽 → 루트 → 오른쪽)
void inorder(Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// 값 검색
Node* search(Node* root, int target) {
    if (root == NULL || root->data == target) return root;

    if (target < root->data)
        return search(root->left, target);
    else
        return search(root->right, target);
}

// 가장 작은 값을 가진 노드 찾기 (삭제 시 필요)
Node* findMin(Node* root) {
    while (root->left != NULL)
        root = root->left;
    return root;
}

// 노드 삭제
Node* delete(Node* root, int value) {
    if (root == NULL) return NULL;

    if (value < root->data)
        root->left = delete(root->left, value);
    else if (value > root->data)
        root->right = delete(root->right, value);
    else {
        // 삭제할 노드를 찾음

        // 1. 자식이 없는 경우
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        // 2. 하나의 자식만 있는 경우
        else if (root->left == NULL) {
            Node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            Node* temp = root->left;
            free(root);
            return temp;
        }
        // 3. 두 자식이 있는 경우: 오른쪽에서 최소값을 찾아 교체
        Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = delete(root->right, temp->data);
    }
    return root;
}

// 모든 노드를 순차적으로 해제
void freeTree(Node* root) {
    if (root == NULL) return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

// 테스트용 main 함수
int main() {
    Node* root = NULL;

    // 노드 삽입
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);

    printf("중위 순회 (오름차순 출력): ");
    inorder(root);
    printf("\n");

    // 검색
    int target = 60;
    Node* found = search(root, target);
    if (found != NULL)
        printf("%d 를 찾았습니다.\n", found->data);
    else
        printf("%d 는 트리에 없습니다.\n", target);

    // 삭제
    root = delete(root, 50);
    printf("50 삭제 후 중위 순회: ");
    inorder(root);
    printf("\n");

    // 메모리 해제
    freeTree(root);
    return 0;
}
