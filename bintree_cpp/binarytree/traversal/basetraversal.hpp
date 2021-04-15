#ifndef __BASE_TRAVERSAL_HPP__
#define __BASE_TRAVERSAL_HPP__


#include <vector>
#include "ordertraversal.hpp"
#include "binnode.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BaseTraversal
{
public:
    virtual ~BaseTraversal() { }

public:
    virtual std::vector<TKey*> traverse(const TNode *root, const OrderTraversal &order = OrderTraversal.IN) = 0;
};



} // bt
} // my



#endif // __BASE_TRAVERSAL_HPP__
