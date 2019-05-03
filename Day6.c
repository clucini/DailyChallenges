#include <stdio.h>
#include <stdlib.h>


struct node {
    struct node* combined;
    int value;
};

struct node* get_next(struct node* n, struct node* last){
    struct node* next = (struct node*)((long)n->combined ^ (long)&last);
    return next;
};

void append(struct node* head, int v){
    printf("penis");
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    printf("%ld", (long)new_node);
    struct node* last = (struct node*)0;
    struct node* cur = get_next(head, last);
    while(cur != (struct node*)0){
        struct node* temp = cur;
        cur = get_next(cur, last);
        last = temp;
    }

    new_node->value = v;
    new_node->combined = last;
    
    last->combined = (struct node*)((long)new_node->combined ^ (long)&last);
}


struct node* get(long count, struct node* h, char p){
    struct node* cur = h;
    struct node* last;
    struct node* next;
    for(long i = 0; i < count; i++){
        if (p == 'y'){
            printf("%d", cur->value); 
        }
        next = get_next(cur, last);
        last = cur;
        cur = next;
    }
    return cur;
}

long main(){
    struct node* head = (struct node*) malloc(sizeof(struct node));
    head->combined = head;
    head->value = 3;
    append(head, 1);
    append(head, 2);
    append(head, 3);
    append(head, 4);
    append(head, 5);
    append(head, 6);
    append(head, 7);
    append(head, 8);

    get(3, head, 'y');
    printf("\n");
}