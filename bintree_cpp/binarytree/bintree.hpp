#ifndef __BIN_TREE_HPP__
#define __BIN_TREE_HPP__


#include <vector>
#include <string>
#include <algorithm>
#include "binnode.hpp"
#include "traversal/recurtraversal.hpp"
#include "binarytreedisp/bintreedisplay.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BinTree
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



protected:
    TNode *root = nullptr;



//////////////////////////////////////////////////////////////
//                        RULE OF FIVE
//////////////////////////////////////////////////////////////



public:
    BinTree()
    {

    }



    BinTree(const BinTree &other)
    {
        this->root = other.root->cloneBranch();
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

        this->root = other.root->cloneBranch();

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



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



public:
    bool empty() const
    {
        return (nullptr == this->root);
    }



    virtual int height() const
    {
        return this->_height(this->root);
    }



    void clear()
    {
        freeMemory(this->root);
        assert( nullptr == this->root );
    }



    std::vector<TKey> traverse(const OrderTraversal &order) const
    {
        RecurTraversal<TKey, TNode> traversal;
        return traversal.traverse(this->root, order);
    }



    // Adapter method connecting BinTreeDisplay and BinTree
    std::string display(my::btdisp::BinTreeDisplay &disp) const
    {
        auto res = disp.get(this->root);
        return res;
    }



    // Adapter method connecting BinTreeDisplay and BinTree
    std::vector<std::string> displayLstRows(my::btdisp::BinTreeDisplay &disp) const
    {
        auto res = disp.getLstRows(this->root);
        return res;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



protected:
    virtual int _height(TNode *node) const
    {
        if (nullptr == node)
            return 0;

        int heightLe = _height(node->left);
        int heightRi = _height(node->right);

        return 1 + std::max(heightLe, heightRi);
    }



    virtual TNode* createNode(const TKey &key) const
    {
        return new TNode(key);
    }



    virtual void freeMemory(TNode *&node)
    {
        if (nullptr == node)
            return;

        freeMemory(node->left);
        freeMemory(node->right);

        delete node;
        node = nullptr;
    }
};



} // bt
} // my



#endif // __BIN_TREE_HPP__
