package binarytree.traveler;


import java.util.List;

import binarytree.BinNode;



public abstract class Traveler< TKey extends Number & Comparable<? super TKey>,
                                TNode extends BinNode<TKey,TNode>
                              >
{
    public abstract void traverse(TNode root, OrderTraverse order, List<?> result);
}
