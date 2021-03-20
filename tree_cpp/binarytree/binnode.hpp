#ifndef __BIN_NODE_HPP__
#define __BIN_NODE_HPP__


namespace mybt
{



/*
Binary Node.

Args:
    key: The key stored in the node.
*/
template <typename T=int>
class BinNode
{
public:
    T key;
    BinNode<T> *left = nullptr;
    BinNode<T> *right = nullptr;


public:
    BinNode(T key = T())
    {
        this->key = key;
    }
};



} // mybt


#endif
