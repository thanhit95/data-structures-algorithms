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
        if (nullptr == this->left)
            return 0;

        return this->left->balance();
    }



    int balanceRight() const
    {
        if (nullptr == this->right)
            return 0;

        return this->right->balance();
    }
};



} // mybt


#endif // __AVL_NODE_HPP__
