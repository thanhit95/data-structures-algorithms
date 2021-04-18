using System;
using my.binarytree;


namespace my.test
{
    class BinNodeImp<TKey> : BinNode<TKey, BinNodeImp<TKey>>
        where TKey : IComparable
    {
        
    }
}
