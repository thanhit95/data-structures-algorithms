#ifndef __AVL_NODE_HPP__
#define __AVL_NODE_HPP__


#include <algorithm>


namespace mybt
{



template < typename TKey >
class AvlNode
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
public:
    TKey key;
    AvlNode *left = nullptr;
    AvlNode *right = nullptr;

private:
    int _height = 1;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    AvlNode(TKey key = TKey())
    {
        this->key = key;
    }



public:
    const int height() const
    {
        return this->_height;
    }



    void updateHeight()
    {
        this->_height = 1 + std::max(heightChild(this->left), heightChild(this->right));
    }



public:
    const int balance() const
    {
        int heightLe = heightChild(this->left);
        int heightRi = heightChild(this->right);
        return heightLe - heightRi;
    }



    const int balanceLeft() const
    {
        if (nullptr == this->left)
            return 0;

        return this->left->balance();
    }



    const int balanceRight() const
    {
        if (nullptr == this->right)
            return 0;

        return this->right->balance();
    }



protected:
    const int heightChild(AvlNode *child) const
    {
        if (nullptr == child)
            return 0;

        return child->height();
    }
};



}


#endif // __AVL_NODE_HPP__
