using System;
using my.binarytree;


namespace my.test
{
    class BinNodeConcrete<TKey> : BinNode<TKey, BinNodeConcrete<TKey>>
        where TKey : IComparable
    {
        
    }
}
