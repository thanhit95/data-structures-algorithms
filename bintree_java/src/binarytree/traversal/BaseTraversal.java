package binarytree.traversal;


import binarytree.BinNode;
import java.util.List;



public abstract class BaseTraversal< TKey extends Comparable<? super TKey>,
                                     TNode extends BinNode<TKey, TNode>
                                   >
{
    public abstract List<TKey> traverse(TNode root, OrderTraversal order);
}
