package binarytree;


import java.util.List;

import binarytree.traversal.*;
import binarytreedisp.BinTreeDisplay;



public class BinTree< TKey extends Comparable<? super TKey>,
                      TNode extends BinNode<TKey,TNode>
                    >
             implements Cloneable
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected TNode root = null;
    protected BaseTraversal<TKey, TNode> traversal = new RecurTraversal<>();



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    public boolean empty() {
        return null == root;
    }



    public int height() {
        return this._height(this.root);
    }



    public void clear() {
        freeMemory(this.root);
        this.root = null;
    }



    public List<TKey> traverse(OrderTraversal order) {
        var res = traversal.traverse(this.root, order);
        return res;
    }



    public BinTree<TKey, TNode> clone() {
        var theClone = new BinTree<TKey, TNode>();

        if (null != this.root) {
            theClone.root = this.root.cloneBranch();
        }

        theClone.traversal = this.traversal;

        return theClone;
    }



    // Adapter method connecting BinTreeDisplay and BinTree
    public String display(BinTreeDisplay disp) {
        var res = disp.get(this.root);
        return res;
    }



    // Adapter method connecting BinTreeDisplay and BinTree
    public List<String> displayLstRows(BinTreeDisplay disp) {
        var res = disp.getLstRows(this.root);
        return res;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    protected int _height(TNode node) {
        if (null == node)
            return 0;

        int heightLe = _height(node.left);
        int heightRi = _height(node.right);

        return 1 + Math.max(heightLe, heightRi);
    }



    @SuppressWarnings("unchecked")
    protected TNode createNode(TKey key) {
        return (TNode) new BinNode<TKey, TNode>(key);
    }



    protected void freeMemory(TNode node)
    {
        if (null == node)
            return;

        freeMemory(node.left);
        freeMemory(node.right);

        node.left = null;
        node.right = null;
    }
}
