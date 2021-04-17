using System;


namespace my.binarytree
{
    class BinNode<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>
    {
        public TKey Key = default;
        public TNode Left = null;
        public TNode Right = null;



        public BinNode(TKey key = default)
        {
            this.Key = key;
        }
    }
}
