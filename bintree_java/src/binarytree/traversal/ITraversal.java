package binarytree.traversal;


import binarytree.BinNode;
import java.util.List;



public interface ITraversal< TKey extends Comparable<? super TKey>,
                                     TNode extends BinNode<TKey, TNode>
                                   >
{
    public abstract List<TKey> traverse(TNode root, OrderTraversal order);
}
