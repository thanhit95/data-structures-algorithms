#ifndef __AVL_NODE_HPP__
#define __AVL_NODE_HPP__


#include <algorithm>
#include "iclonebranch.hpp"



namespace my
{
namespace bt
{



template < typename TKey >
class AvlNode : public ICloneBranch<AvlNode<TKey>>
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



public:
    TKey key;
    AvlNode *left = nullptr;
    AvlNode *right = nullptr;

protected:
    int _height = 1;



//////////////////////////////////////////////////////////////
//                        METHODS
//////////////////////////////////////////////////////////////



public:
    AvlNode(const TKey &key = TKey())
    {
        this->key = key;
    }



public:
    inline int height() const
    {
        return this->_height;
    }



    inline int heightLeft() const
    {
        return (nullptr == this->left) ? 0 : this->left->height();
    }



    inline int heightRight() const
    {
        return (nullptr == this->right) ? 0 : this->right->height();
    }



    void updateHeight()
    {
        this->_height = 1 + std::max(heightLeft(), heightRight());
    }



public:
    int balance() const
    {
        int heightLe = heightLeft();
        int heightRi = heightRight();
        return heightLe - heightRi;
    }



    int balanceLeft() const
    {
        return (nullptr == this->left) ? 0 : this->left->balance();
    }



    int balanceRight() const
    {
        return (nullptr == this->right) ? 0 : this->right->balance();
    }



public:
    AvlNode* cloneBranch() const override
    {
        auto *theClone = new AvlNode<TKey>(this->key);
        theClone->_height = this->_height;

        if (nullptr != this->left)
            theClone->left = this->left->cloneBranch();

        if (nullptr != this->right)
            theClone->right = this->right->cloneBranch();

        return theClone;
    }
};



} // bt
} // my



#endif // __AVL_NODE_HPP__
