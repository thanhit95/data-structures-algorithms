#ifndef __BIN_NODE_HPP__
#define __BIN_NODE_HPP__


namespace mybt
{



template < typename TKey >
class BinNode
{
public:
    TKey key;
    BinNode *left = nullptr;
    BinNode *right = nullptr;


public:
    BinNode(TKey key = TKey())
    {
        this->key = key;
    }
};



} // mybt


#endif
