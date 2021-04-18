using System;
using System.Collections.Generic;


namespace my.binarytree.traversal
{
    interface ITraversal<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {
        List<TKey> Traverse(TNode root, OrderTraversal order);
    }
}
