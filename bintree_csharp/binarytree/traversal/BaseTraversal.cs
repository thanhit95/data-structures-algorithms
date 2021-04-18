using System;
using System.Collections.Generic;


namespace my.binarytree.traversal
{
    abstract class BaseTraversal<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {
        public abstract List<TKey> Traverse(TNode root, OrderTraversal order);
    }
}
