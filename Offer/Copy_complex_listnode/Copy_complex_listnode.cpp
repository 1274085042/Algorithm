/*
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
*/

struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(nullptr), random(nullptr) {
    }
};

class Solution
{
public:
    void CopyNodes(RandomListNode * pHead);
    void ConnectRandomNodes(RandomListNode *pHead);
    RandomListNode * ConnectCopyNodes(RandomListNode *pHead);

    RandomListNode* Clone(RandomListNode* pHead)
    {
        CopyNodes(pHead);
        ConnectRandomNodes(pHead);
        RandomListNode * CloneHead=ConnectCopyNodes(pHead);
        return CloneHead;
        
    }


};

void Solution::CopyNodes(RandomListNode * pHead)
{
    /*
        if (pHead==nullptr)
    {
        return;
    }
    else
    {
        RandomListNode *pNode=pHead;
        while (pNode!=nullptr)
        {   
            //RandomListNode CloneNode=*pNode;
            RandomListNode *CloneNode=new RandomListNode(pNode->label);
            CloneNode->next=pNode->next;
            CloneNode->random=nullptr;
            pNode->next=CloneNode;
            pNode=CloneNode->next;
        }
    }
    */

   RandomListNode *pNode=pHead;
   while (pNode!=nullptr)
   {
       RandomListNode *CloneNode=new RandomListNode(pNode->label);
       CloneNode->next=pNode->next;
       CloneNode->random=nullptr;

       pNode->next=CloneNode;
       pNode=CloneNode->next;

   }
   

}


void Solution::ConnectRandomNodes(RandomListNode *pHead)
{
    
    if (pHead==nullptr)
    {
        return;
    }
    else
    {
        RandomListNode *pNode=pHead;
        while (pNode!=nullptr)
        {
             RandomListNode *ClonePNode=pNode->next;
            if(pNode->random!=nullptr)
            {
                ClonePNode->random=(pNode->random)->next;
            }
            pNode=ClonePNode->next;
            
        }
    }
    
/*
   RandomListNode *pNode=pHead;
   while (pNode!=nullptr)
   {
       RandomListNode *CloneNode=pNode->next;
       if(pNode->random!=nullptr)
       {
           CloneNode->random=pNode->random->next;
       }
       pNode=CloneNode->next;

   }
*/
}

RandomListNode * Solution::ConnectCopyNodes(RandomListNode *pHead)
{
    
    if (pHead==nullptr)
    {
        return pHead;
    }
    else
    {
        RandomListNode *pNode=pHead;
        RandomListNode *ClonePhead,*ClonePnode=pHead;
       

        if(pNode->next!=nullptr)
        {
            ClonePnode=ClonePhead=pNode->next;
            pNode->next=ClonePnode->next;
          
            pNode=ClonePnode->next;
          
        }

        while (pNode!=nullptr)
        {
            ClonePnode->next=pNode->next;
            ClonePnode=ClonePnode->next;
            pNode->next=ClonePnode->next;
            pNode=ClonePnode->next;
        }
        return ClonePhead;
    }
    
/*
   RandomListNode *pNode=pHead;
   RandomListNode *CloneHead,*CloneNode=nullptr;

   if(pNode!=nullptr)
   {
       CloneHead=CloneNode=pNode->next;
       pNode->next=CloneNode->next;
       pNode=pNode->next;
   }

   while (pNode!=nullptr)
   {
       CloneNode->next=pNode->next;
       CloneNode=CloneNode->next;
       pNode->next=CloneNode->next;
       pNode=pNode->next;
   }
   return CloneHead;
  */ 
}