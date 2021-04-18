#ifndef __NONRECUR_TRAVERSAL_HPP__
#define __NONRECUR_TRAVERSAL_HPP__


#include <vector>
#include <stack>
#include <algorithm>
#include "itraversal.hpp"
#include "ordertraversal.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class NonRecurTraversal : public ITraversal<TKey, TNode>
{
public:
    virtual ~NonRecurTraversal() { }



public:
    virtual std::vector<TKey> traverse(const TNode *root, const OrderTraversal &order = OrderTraversal::IN) override
    {
        std::vector<TKey> resPath;

        switch (order)
        {
        case OrderTraversal::PRE :
            traversePre(root, resPath);
            break;

        case OrderTraversal::IN :
            traverseIn(root, resPath);
            break;

        case OrderTraversal::POST :
            traversePost(root, resPath);
            break;

        default:
            break;
        }

        return resPath;
    }



protected:
    virtual void traversePre(const TNode *node, std::vector<TKey> &resPath)
    {
        resPath.clear();
        std::stack<TNode> stack;

        stack.push(node);

        while (false == stack.empty())
        {
            node = stack.top();
            stack.pop();
            resPath.push_back(node->key);

            if (nullptr != node->right)
                stack.push(node->right);

            if (nullptr != node->left)
                stack.push(node->left);
        }
    }



    virtual void traversePost(const TNode *node, std::vector<TKey> &resPath)
    {
        resPath.clear();
        std::stack<TNode> stack;

        stack.push(node);

        while (false == stack.empty())
        {
            node = stack.top();
            stack.pop();
            resPath.push_back(node->key);

            if (nullptr != node->left)
                stack.push(node->left);

            if (nullptr != node->right)
                stack.push(node->right);
        }

        std::reverse(resPath.begin(), resPath.end());
    }



    virtual void traverseIn(const TNode *node, std::vector<TKey> &resPath)
    {
        resPath.clear();
        std::stack<TNode> stack;
        TNode *pickedNode = nullptr;

        while (1)
        {
            while (node)
            {
                stack.push(node);
                node = node->left;
            }

            if (false == stack.empty())
                break;

            pickedNode = stack.top();
            stack.pop();

            resPath.push_back(pickedNode->key);
            node = pickedNode->right;
        }
    }
};



} // bt
} // my



#endif // __NONRECUR_TRAVERSAL_HPP__
