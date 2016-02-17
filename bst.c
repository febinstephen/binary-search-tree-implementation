#include<stdio.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};


struct Node* Newnode(int data)
{
    struct Node* node = malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return(node);
}


int lookup(struct Node* node, int target)
// Function to search for an element
{
    if(node == NULL) {
        return 0;
    }
    if(node->data == target) {
       return 1;
    }
    else {
        if (target <= node->data) {
            return lookup(node->left, target);
        }
        else {
            return lookup(node->right, target);
        }
    }
}

struct Node* insertNode(struct Node* node, int data)
// Function to insert a new node to the BST
{
    if(node == NULL) {
        return Newnode(data);
    }
    else {
        if (data < node->data) {
           node->left = insertNode(node->left, data);
           //node->left = Newnode(data);
        }
        else {
          node->right = insertNode(node->right, data);
          //node->right = Newnode(data);
        }
    }
   return node;
}
   /*else {
       printf("Oops element already exists");
       return(node);
   }*/

int size(struct Node* node)
{
   if(node == NULL) {
      return(0);
   } else {
       return(size(node->left) + 1 + size(node->right));
   }
}

void printTree(struct Node* node)
{
   if (node == NULL) return;
   printTree(node->left);
   printf("%i ",node->data);
   printTree(node->right);
}

struct Node* findMin(struct Node* node)
{
        while(node->left != NULL) {
           node = node->left;
        }
        return node;
}

struct Node* delete(struct Node* node, int data)
{
    //struct Node* parent;
    if(node == NULL) {
        return node;
    }
    if (data < node->data) {
       //parent = node;
       node->left = delete(node->left, data);
    }
    if(data > node->data) {
      //parent = node;
      node->right = delete(node->right, data);
    }
    else {
        if (node->left == NULL && node->right == NULL) {
            free(node);
            node = NULL;
        } else if(node->left == NULL) {
            struct Node* temp = node;
            node = node->right;
            free(temp);
        } else if(node->right == NULL) {
            struct Node* temp = node;
            node = node->left;
            free(temp); }
        else {
            struct Node* temp = findMin(node->right);
            temp->left = node->left;
            temp = node;
            //strcpy(root->data,temp->data);
            node = node->right;
            //root->right = delete(root->right,temp->data);
        }
    //return node;
    }
return node;
}

void main()
{
    struct Node* root;
    root = Newnode(1);
    //root->data = NULL;
    printf("%i\n",size(root));
    printf("%i\n",lookup(root, 6));
    printTree(root);
    //delete(root, 8);
    printf("\n");
    //printTree(root);
    insertNode(root, 10);
    printf("\n");
    printTree(root);
    //int choice, item;
    //printf("%i\n",root->data);
    /*do {
        printf("BST options:\n1.search\n2.insertion\n3.deletion\n");
        scanf("%d\n",&choice);
        switch(choice) {
            case 1:
                printf("\nInput search element:");
                scanf("\n%d",&item);
                printf("\n");
                lookup(root, item);
                break;
            case 2:
                printf("\nInput element to insert:");
                scanf("\n%d",&item);
                insertNode(root, item);
                printTree(root);
                printf("\n");
                break;
            case 3:
                exit(0);
            default:
                printf("error:unknown");
                break;
        }
    } while(choice != 3); */
}
