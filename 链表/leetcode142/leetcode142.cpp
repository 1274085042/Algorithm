//Definition for singly-linked list.
 
struct ListNode 
 {
     int val;
     ListNode *next;
 ListNode(int x) : val(x), next(nullptr)
 {}
};

class Solution 
{
public:
    ListNode* detectCycle(ListNode* head) 
    {
        ListNode* slow = head;
        ListNode* fast = head;
        while (slow && fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast)
            {
                ListNode* index1 = head;
                ListNode* index2 = slow;
                while (index1 != index2)
                {
                    index1 = index1->next;
                    index2 = index2->next;
                }

                return index1;
            }
        }

        return nullptr;
    }
};