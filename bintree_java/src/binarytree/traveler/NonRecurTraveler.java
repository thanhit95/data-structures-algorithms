package binarytree.traveler;


import binarytree.BinNode;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;



public class NonRecurTraveler< TKey extends Number & Comparable<? super TKey>,
                               TNode extends BinNode<TKey, TNode>
                             >
             extends Traveler<TKey, TNode>
{


    @Override
    public List<TKey> traverse(TNode root, OrderTraverse order) {
        var resPath = new ArrayList<TKey>();

        switch (order) {
        case PRE:
            traversePre(root, resPath);
            break;

        case IN:
            traverseIn(root, resPath);
            break;

        case POST:
            traversePost(root, resPath);
            break;

        default:
            break;
        }

        return resPath;
    }



    protected void traversePre(TNode node, List<TKey> resPath) {
        resPath.clear();
        var stack = new Stack<TNode>();

        stack.push(node);

        while (false == stack.empty()) {
            node = stack.pop();
            resPath.add(node.key);

            if (null != node.right)
                stack.push(node.right);

            if (null != node.left)
                stack.push(node.left);
        }
    }



    protected void traverseIn(TNode node, List<TKey> resPath) {
        resPath.clear();
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
    }



    protected void traversePost(TNode node, List<TKey> resPath) {
        resPath.clear();
        var stack = new Stack<TNode>();

        stack.push(node);

        while (false == stack.empty()) {
            node = stack.pop();
            resPath.add(node.key);

            if (null != node.left)
                stack.push(node.left);

            if (null != node.right)
                stack.push(node.right);
        }

        Collections.reverse(resPath);
    }
}
