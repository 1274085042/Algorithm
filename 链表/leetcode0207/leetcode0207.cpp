// Definition for singly-linked list.
struct ListNode 
{
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(nullptr) {}
};

class Solution 
{
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) 
    {
        ListNode* a = headA;
        ListNode* b = headB;

        int aLen = 0;
        int bLen = 0;
        while (a)
        {
            ++aLen;
            a = a->next;
        }
        while (b)
        {
            ++bLen;
            b = b->next;
        }

        a = headA;
        b = headB;

        int gap;

        if (aLen > bLen)
        {
            gap = aLen - bLen;
            while (gap)
            {
                --gap;
                a = a->next;
            }
        }
        else
        {
            gap = bLen - aLen;
            while (gap)
            {
                --gap;
                b = b->next;
            }
        }

        while (a)
        {
            if (a == b)
            {
                return a;
            }
            a = a->next;
            b = b->next;
        }

        return nullptr;
    }
};
