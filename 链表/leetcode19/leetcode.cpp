//Definition for singly-linked list.
struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution 
{
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        ListNode* dummy=new ListNode;
        dummy->next = head;
        ListNode* slow = dummy;
        ListNode* fast = dummy;
        while (n)
        {
            fast = fast->next;
            --n;
        }

        while (fast->next)
        {
            fast = fast->next;
            slow = slow->next;
        }

        ListNode* tmp = slow->next;
        slow->next = tmp->next;
        delete tmp;

        ListNode* res = dummy->next;
        delete dummy;

        return res;
    }
};