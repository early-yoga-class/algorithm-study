#include <stdio.h>
#include <stdlib.h>

//BSTNode라는 사용자 정의 자료형
// value, left, right - 멤버변수/ 필드
typedef struct BSTNode {
    int value;
    struct BSTNode* left;
    struct BSTNode* right;
} BSTNode;

//BSTNode 구조체 포인터를 반환 , 입력값: root & value
BSTNode* insert(BSTNode* root, int value) {
    // 재귀를 계속 돌다가 루트가 없을 때 실행 즉, 리프노드에 다랐을때
    // 1. 새로운 노드를 만든다 
    if (root == NULL) {
        // newNode = BSTNode사이즈 만큼의 크기 할당
        BSTNode* newNode = malloc(sizeof(BSTNode));
        newNode->value = value;
        newNode->left = newNode->right = NULL;
        return newNode;
    }

    // root 값보다 작으면? 왼쪽 서브트리의 루트 -> 루트가 됨.
    if (value < root->value)
        root->left = insert(root->left, value);
    else if (value > root->value)
        root->right = insert(root->right, value);
    // root -> left/ right에 다음 루트를 연결하는 역할을 함.
    return root;
}


BSTNode* search(BSTNode* root, int value) {
    // 찾는 값이 루트에 있다면? 그 값을 반환
    // 찾는 값이 없다면? NULL 반환
    if (root == NULL || root->value == value)
        return root;
    //찾는 값이 더 작으면 왼쪽으로 내려간다.
    if (value < root->value)
        return search(root->left, value);
    else
        return search(root->right, value);
}

//왼쪽으로 타고내려가면서 포인터 변수 자체가 가리키는 대상을 변경
BSTNode* findMin(BSTNode* node) {
    while (node->left != NULL)
        node = node->left;
    return node;
}

//삭제할 root, value
BSTNode* delete(BSTNode* root, int value) {
    //없으면 NULL 변환
    if (root == NULL) return NULL;

    //루트보다 작으면 왼쪽 서브트리로 타고간다.
    if (value < root->value)
        root->left = delete(root->left, value);
    else if (value > root->value)
        root->right = delete(root->right, value);

    // 삭제할 값을 찾았을 때 !!
    else {
        // 1. 자식이 없는 경우
        if (root->left == NULL && root->right == NULL) {
            free(root);
            return NULL;
        }
        // 2. 자식이 하나만 있는 경우
        else if (root->left == NULL || root->right == NULL) {
            BSTNode* temp = (root->left) ? root->left : root->right;
            free(root);
            return temp;
        }
        // 3. 자식이 둘다 있는 경우
        else {
            // 오른쪽 서브트리에서 가장 작은 값을 가져온다.
            BSTNode* successor = findMin(root->right);
            root->value = successor->value;
            root->right = delete(root->right, successor->value);
        }
    }
    return root;
}


// ... 위에 있는 insert, search, delete 함수 그대로 두고

void inorder(BSTNode* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->value);
    inorder(root->right);
}

int main() {
    BSTNode* root = NULL;

    // 삽입 테스트
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 70);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 60);
    root = insert(root, 80);

    printf("중위 순회: ");
    inorder(root);  // 20 30 40 50 60 70 80
    printf("\n");

    // 탐색 테스트
    BSTNode* found = search(root, 60);
    if (found != NULL)
        printf("60 찾음! ✅\n");
    else
        printf("60 없음! ❌\n");

    // 삭제 테스트
    root = delete(root, 50);
    printf("50 삭제 후 중위 순회: ");
    inorder(root);  // 20 30 40 60 70 80
    printf("\n");

    return 0;
}
