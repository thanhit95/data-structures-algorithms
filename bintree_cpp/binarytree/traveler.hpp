#ifndef __TRAVELER_HPP__
#define __TRAVELER_HPP__


#include <vector>



namespace my
{
namespace bt
{



enum class OrderTraverse
{
    PRE,
    IN,
    POST
};



////////////////////////////////////////////////////////////////



template < typename TKey, typename TNode >
class Traveler
{
public:
    virtual ~Traveler() { }



public:
    virtual std::vector<TKey*> traverse(TNode *root, const OrderTraverse &order) = 0;
};



////////////////////////////////////////////////////////////////



template < typename TKey, typename TNode >
class TravelerRecur : public Traveler<TKey, TNode>
{
protected:
    std::vector<TKey*> _resPath;



public:
    virtual std::vector<TKey*> traverse(TNode *root, const OrderTraverse &order) override
    {
        _resPath.clear();

        switch (order)
        {
        case OrderTraverse::PRE :
            traversePre(root);
            break;

        case OrderTraverse::IN :
            traverseIn(root);
            break;

        case OrderTraverse::POST :
            traversePost(root);
            break;

        default:
            break;
        }

        return _resPath;
    }



protected:
    void traversePre(TNode *node)
    {
        if (nullptr == node)
            return;

        _resPath.push_back(&node->key);
        traversePre(node->left);
        traversePre(node->right);
    }



    void traverseIn(TNode *node)
    {
        if (nullptr == node)
            return;

        traverseIn(node->left);
        _resPath.push_back(&node->key);
        traverseIn(node->right);
    }



    void traversePost(TNode *node)
    {
        if (nullptr == node)
            return;

        traversePost(node->left);
        traversePost(node->right);
        _resPath.push_back(&node->key);
    }
};



} // bt
} // my



#endif
