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
    ITraversal<TKey, TNode> *traversal = nullptr;



//////////////////////////////////////////////////////////////
//                        RULE OF FIVE
//////////////////////////////////////////////////////////////



public:
    BinTree()
    {
        this->traversal = new RecurTraversal<TKey, TNode>();
    }



    virtual ~BinTree()
    {
        disposeRoot(this->root);
        delete this->traversal;
        this->traversal = nullptr;
    }



    BinTree(const BinTree &other)
    {
        this->root = other.root->cloneBranch();
        this->traversal = other.traversal->clone();
    }



    BinTree(BinTree &&other)
    {
        this->root = other.root;
        this->traversal = other.traversal;
        other.root = nullptr;
        other.traversal = nullptr;
    }



    virtual BinTree& operator=(const BinTree &other)
    {
        if (this == &other)
            return *this;

        disposeRoot(this->root);
        delete this->traversal;

        this->root = other.root->cloneBranch();
        this->traversal = other.traversal->clone();

        return *this;
    }



    virtual BinTree& operator=(BinTree &&other)
    {
        if (this == &other)
            return *this;

        disposeRoot(this->root);
        delete this->traversal;

        this->root = other.root;
        this->traversal = other.traversal;
        other.root = nullptr;
        other.traversal = nullptr;

        return *this;
    }



//////////////////////////////////////////////////////////////
//                        ABSTRACT METHODS
//////////////////////////////////////////////////////////////



public:
    virtual bool insert(const TKey &key) = 0;
    virtual bool remove(const TKey &key) = 0;



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
        disposeRoot(this->root);
        assert( nullptr == this->root );
    }



    std::vector<TKey> traverse(const OrderTraversal &order) const
    {
        return this->traversal->traverse(this->root, order);
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



    virtual void disposeRoot(TNode *&node)
    {
        if (nullptr == node)
            return;

        disposeRoot(node->left);
        disposeRoot(node->right);

        delete node;
        node = nullptr;
    }
};



} // bt
} // my



#endif // __BIN_TREE_HPP__
