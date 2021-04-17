using System;
using my.extensions;


namespace my.binarytree
{
    class AvlTree<TKey> : BinTree<TKey, AvlNode<TKey>>
        where TKey : IComparable
    {
        public override AvlTree<TKey> Clone()
        {
            var theClone = this.DeepCopy();
            return theClone;
        }
    }
}
