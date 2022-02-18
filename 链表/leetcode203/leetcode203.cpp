/*
 * Definition for singly-linked list.
 */
 struct ListNode 
 {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
/*
 * 链表移除：通过前一个结点来移除当前节点
*/
class Solution 
{
public:
    ListNode* removeElements(ListNode* head, int val) 
    {
        ListNode* dummpy = new ListNode;
        dummpy->next = head;
        ListNode* cur = dummpy;
        while (cur->next != nullptr)
        {
            if (cur->next->val == val)
            {
                ListNode* tmp = cur->next;
                cur->next = tmp->next;
                delete tmp;
            }
            else
            {
                cur = cur->next;
            }
        }

        head = dummpy->next;
        delete dummpy;
        return head;
    }
};