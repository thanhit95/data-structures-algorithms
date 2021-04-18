#ifndef __INTERFACE_TRAVERSAL_HPP__
#define __INTERFACE_TRAVERSAL_HPP__


#include <vector>
#include "ordertraversal.hpp"
#include "../binnode.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class ITraversal
{
public:
    virtual ~ITraversal() { }

public:
    virtual std::vector<TKey> traverse(const TNode *root, const OrderTraversal &order = OrderTraversal::IN) = 0;
};



} // bt
} // my



#endif // __INTERFACE_TRAVERSAL_HPP__
