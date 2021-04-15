package binarytree.traversal;


import binarytree.BinNode;
import java.util.List;
import java.util.ArrayList;



public class RecurTraversal< TKey extends Comparable<? super TKey>,
                             TNode extends BinNode<TKey, TNode>
                           >
             extends BaseTraversal<TKey, TNode>
{


    protected List<TKey> resPath;



    @Override
    public List<TKey> traverse(TNode root, OrderTraversal order) {
        resPath = new ArrayList<>();

        switch (order) {
        case PRE:
            traversePre(root);
            break;

        case IN:
            traverseIn(root);
            break;

        case POST:
            traversePost(root);
            break;

        default:
            break;
        }

        return resPath;
    }



    protected void traversePre(TNode node) {
        if (null == node)
            return;

        resPath.add(node.key);
        traversePre(node.left);
        traversePre(node.right);
    }



    protected void traverseIn(TNode node) {
        if (null == node)
            return;

        traverseIn(node.left);
        resPath.add(node.key);
        traverseIn(node.right);
    }



    protected void traversePost(TNode node) {
        if (null == node)
            return;

        traversePost(node.left);
        traversePost(node.right);
        resPath.add(node.key);
    }
}
