#ifndef __RECUR_TRAVERSAL_HPP__
#define __RECUR_TRAVERSAL_HPP__


#include <vector>
#include "basetraversal.hpp"
#include "ordertraversal.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class RecurTraversal : public BaseTraversal<TKey, TNode>
{
protected:
    std::vector<TKey> resPath;



public:
    virtual ~RecurTraversal() { }



public:
    virtual std::vector<TKey> traverse(const TNode *root, const OrderTraversal &order = OrderTraversal::IN) override
    {
        resPath.clear();

        switch (order)
        {
        case OrderTraversal::PRE :
            traversePre(root);
            break;

        case OrderTraversal::IN :
            traverseIn(root);
            break;

        case OrderTraversal::POST :
            traversePost(root);
            break;

        default:
            break;
        }

        return resPath;
    }



protected:
    virtual void traversePre(const TNode *node)
    {
        if (nullptr == node)
            return;

        resPath.push_back(node->key);
        traversePre(node->left);
        traversePre(node->right);
    }



    virtual void traverseIn(const TNode *node)
    {
        if (nullptr == node)
            return;

        traverseIn(node->left);
        resPath.push_back(node->key);
        traverseIn(node->right);
    }



    virtual void traversePost(const TNode *node)
    {
        if (nullptr == node)
            return;

        traversePost(node->left);
        traversePost(node->right);
        resPath.push_back(node->key);
    }
};



} // bt
} // my



#endif // __RECUR_TRAVERSAL_HPP__
