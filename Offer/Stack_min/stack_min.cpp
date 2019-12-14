
/*
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。
在该栈中，调用min、push、及pop的时间复杂度都是O(1)
*/

template <typename type>
class stack
{
    public:
    bool empty() const;
    bool push(const type &value);
    bool pop();
    type top();
};

template <typename type>
class Solution
{
private:
    stack<type> st;         //栈
    stack<type> smin;       //辅助栈，存放最小值

public:
    void push(const type &value)
    {
        st.push(value);
        if (smin.empty())
        {
            smin.push(value);
        }
        if (smin.top()>value)
        {
            smin.push(value);
        }
        else
        {
            smin.push(smin.top());
        }            
    }
    void pop()
    {
        if (st.empty()!=true)
        {
            st.pop();
            smin.pop();
        }
    }

    type top()
    {
        return st.top();
    }

    type min()
    {
        return smin.top();
    }

};