#ifndef __BIN_TREE_HPP__
#define __BIN_TREE_HPP__


#include <vector>
#include <algorithm>
#include "binnode.hpp"
#include "traveler.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BinTree
{
////////////////////////////////////////////////////////
//                        FIELDS
////////////////////////////////////////////////////////
protected:
    TNode *root = nullptr;
    TravelerRecur<TKey, TNode> traveler;



////////////////////////////////////////////////////////
//                     RULE OF FIVE
////////////////////////////////////////////////////////
public:
    BinTree()
    {

    }



    BinTree(const BinTree &other)
    {
        this->root = __clone(other.root);
    }



    BinTree(BinTree &&other)
    {
        this->root = other.root;
        other.root = nullptr;
    }



    virtual ~BinTree()
    {
        freeMemory(this->root);
    }



    virtual BinTree& operator=(const BinTree &other)
    {
        if (this == &other)
            return *this;

        freeMemory(this->root);

        this->root = __clone(other.root);

        return *this;
    }



    virtual BinTree& operator=(BinTree &&other)
    {
        if (this == &other)
            return *this;

        freeMemory(this->root);

        this->root = other.root;
        other.root = nullptr;

        return *this;
    }



protected:
    virtual TNode* __clone(TNode *nodeSrc)
    {
        if (nullptr == nodeSrc)
            return nullptr;

        TNode *node = new TNode();
        *node = *nodeSrc;

        node->left = __clone(node->left);
        node->right = __clone(node->right);

        return node;
    }



protected:
    virtual void freeMemory(TNode *&node)
    {
        if (nullptr == node)
            return;

        freeMemory(node->left);
        freeMemory(node->right);

        delete node;
        node = nullptr;
    }



////////////////////////////////////////////////////////
//                        METHODS
////////////////////////////////////////////////////////
public:
    inline bool empty() const
    {
        return (nullptr == this->root);
    }



public:
    int height() const
    {
        return __height(root);
    }



public:
    // WARNING: This getter method may cause the tree to malfunction.
    TNode* _getRoot() const
    {
        return this->root;
    }



public:
    std::vector<TKey*> traverse(const OrderTraverse &order)
    {
        return traveler.traverse(this->root, order);
    }



    int __height(TNode *node) const
    {
        if (nullptr == node)
            return 0;

        int heightLe = 1 + __height(node->left);
        int heightRi = 1 + __height(node->right);

        return std::max(heightLe, heightRi);
    }
};



} // bt
} // my



#endif // __BIN_TREE_HPP__
