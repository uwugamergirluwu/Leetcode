/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummyNode = malloc(sizeof(struct ListNode));
    dummyNode->val = 0;
    dummyNode->next = NULL;
    struct ListNode* current = dummyNode;
    int carry = 0;
    while (l1 || l2 || carry){
        int x = (l1) ? l1->val : 0;
        int y = (l2) ? l2->val : 0;
        int sum = x + y + carry;
        carry = sum/10;
        current->next = malloc(sizeof(struct ListNode));
        current->next->val = sum%10;
        current->next->next = NULL;
        current = current->next;
        if (l1){l1=l1->next;}
        if (l2){l2=l2->next;}

    }
    return dummyNode->next;
}
