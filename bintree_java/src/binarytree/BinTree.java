package binarytree;


import java.util.List;

import binarytree.traversal.*;
import binarytreedisp.BinTreeDisplay;



public abstract class BinTree< TKey extends Comparable<? super TKey>,
                      		   TNode extends BinNode<TKey,TNode>
                    		 >
					  implements Cloneable
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected TNode root = null;
    protected ITraversal<TKey, TNode> traversal = new RecurTraversal<>();
    
   
    
//////////////////////////////////////////////////////////////
//                        ABSTRACT METHODS
//////////////////////////////////////////////////////////////
    
    
    
    public abstract boolean insert(TKey key);
    public abstract boolean remove(TKey key);
    


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
        disposeRoot(this.root);
        this.root = null;
    }



    public List<TKey> traverse(OrderTraversal order) {
        var res = traversal.traverse(this.root, order);
        return res;
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



    protected void disposeRoot(TNode node)
    {
        if (null == node)
            return;

        disposeRoot(node.left);
        node.left = null;

        disposeRoot(node.right);
        node.right = null;

        node.key = null;
    }
}
