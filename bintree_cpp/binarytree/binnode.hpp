#ifndef __BIN_NODE_HPP__
#define __BIN_NODE_HPP__


#include "iclonebranch.hpp"



namespace my
{
namespace bt
{



template <typename TKey>
class BinNode : public ICloneBranch<BinNode<TKey>>
{
public:
    TKey key;
    BinNode *left = nullptr;
    BinNode *right = nullptr;



public:
    BinNode(const TKey &key = TKey())
    {
        this->key = key;
    }



public:
    BinNode* cloneBranch() const override
    {
        auto *theClone = new BinNode<TKey>(this->key);

        if (nullptr != this->left)
            theClone->left = this->left->cloneBranch();

        if (nullptr != this->right)
            theClone->right = this->right->cloneBranch();

        return theClone;
    }
};



} // bt
} // my



#endif // __BIN_NODE_HPP__
