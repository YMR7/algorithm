/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/*
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{   
    int total = 0;
    struct ListNode *node;
    total = TheInt(l1) + TheInt(l2);
    while (total % 10 != 0 || total / 10 != 0)
    {
       
        node->val = total % 10;
        node = node->next;
    }
    return node;
      
}

int TheInt(struct ListNode* l)
{
    int i = 0; 
    int sum = 0;
    int temp[10] = {0};
    while (l)
    {
        
        i++;
        l = l->next;
        temp[i] = l->val;
    }
    for(i; i >= 0; i--)
    {
        sum += temp[i] * pow(10, i);
    }
    return sum;
}
*/

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *temp = malloc(sizeof(struct ListNode));
    temp->next = NULL;
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    struct ListNode* curr = temp;
    int x,y,sum= 0;
    int carry = 0;
    
    memset(curr,0,sizeof(struct ListNode));
    
    while(NULL!=p || NULL!=q)
    {
        x = (NULL!=p) ? p->val : 0;
        y = (NULL!=q) ? q->val : 0;
        sum = carry + x + y;
        carry = sum/10;
        curr->next = malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = sum%10;
        curr->next = NULL;
        if(NULL!=p)
            p = p->next;
        if(NULL!=q)
            q = q->next;
    }
    if(carry > 0)
    {
        curr->next = malloc(sizeof(struct ListNode));
        curr = curr->next;
        curr->val = carry;
        curr->next = NULL;
    }

    return temp->next;
    
}

