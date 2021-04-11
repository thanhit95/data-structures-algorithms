package binarytree.traveler;


import binarytree.BinNode;
import java.util.List;
import java.util.ArrayList;
import java.util.Stack;



public class NonRecurTraveler< TKey extends Number & Comparable<? super TKey>,
                               TNode extends BinNode<TKey, TNode>
                             >
             extends Traveler<TKey, TNode>
{


    protected List<TKey> resPath;



    @Override
    public List<TKey> traverse(TNode root, OrderTraverse order) {
        resPath = new ArrayList<>();

        switch (order) {
        case PRE:

            break;

        case IN:
            traverseIn(root);
            break;

        case POST:

            break;

        default:
            break;
        }

        return resPath;
    }



    protected void traversePre(TNode node) {
        // not implemented yet
    }



    protected void traverseIn(TNode node) {
        var stack = new Stack<TNode>();

        while (true) {
            while (null != node) {
                stack.add(node);
                node = node.left;
            }

            if (stack.empty()) {
                break;
            }

            TNode resultNode = stack.pop();
            resPath.add(resultNode.key);

            node = resultNode.right;
        }

        return;
    }



    protected void traversePost(TNode node) {
        // not implemented yet
    }
}
