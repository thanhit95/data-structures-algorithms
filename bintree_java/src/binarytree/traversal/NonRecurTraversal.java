package binarytree.traversal;


import binarytree.BinNode;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;



public class NonRecurTraversal< TKey extends Comparable<? super TKey>,
                                TNode extends BinNode<TKey, TNode>
                              >
             extends BaseTraversal<TKey, TNode>
{


    @Override
    public List<TKey> traverse(TNode root, OrderTraversal order) {
        var resPath = new ArrayList<TKey>();

        if (null == root)
            return resPath;

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

            TNode pickedNode = stack.pop();
            resPath.add(pickedNode.key);

            node = pickedNode.right;
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
