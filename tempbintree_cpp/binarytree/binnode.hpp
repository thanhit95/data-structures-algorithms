#ifndef __BIN_NODE_HPP__
#define __BIN_NODE_HPP__



namespace my
{
namespace bt
{



template < typename TKey >
class BinNode
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
};



} // bt
} // my



#endif // __BIN_NODE_HPP__
