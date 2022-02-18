#include <iostream>
using namespace std;

class MyLinkedList 
{
private:
    struct  Node
    {
        int val;
        Node* next;
        Node(int v) :val(v), next(nullptr)
        {}
    };

private:
    int size_;
    Node* dummyHead_;

public:
    MyLinkedList():size_(0),dummyHead_(new Node(0))
    {
    }

    int get(int index) 
    {
        Node* cur = dummyHead_;
    
        while (cur && index)
        {
            index--;
            cur = cur->next;

        }
        if (cur)
        {
            return cur->next->val;
        }
        else
        {

            return -1;
        }
         
    }

    void addAtHead(int val) 
    {
        Node* newNode=new Node(val);
        newNode->next = dummyHead_->next;
        dummyHead_->next = newNode;
    }

    void addAtTail(int val) 
    {
        Node* cur = dummyHead_;
        while (cur->next)
        {
            cur = cur->next;
        }

        Node* newNode = new Node(val);
        cur->next = newNode;
        newNode->next = nullptr;
    }

    void addAtIndex(int index, int val) 
    {
        if (index > size_)
        {
            return;
        }

        else
        {
            Node* cur = dummyHead_;

            while (index)
            {
                cur = cur->next;
                --index;
            }
            Node* newNode = new Node(val);
            newNode->next = cur->next->next;
            cur->next = newNode;
        }
    }

    void deleteAtIndex(int index) 
    {
        if (index < 0 || index >= size_)
        {
            return;
        }

        else
        {
            Node* cur = dummyHead_;
            while (index)
            {
                --index;
                cur = cur->next;
            }
            Node* tmp = cur->next;
            cur->next = cur->next->next;
            delete tmp;
        }
    }
};
