package binarytree;


import java.util.List;
import binarytree.traveler.*;
import binarytreedisp.BinTreeDisplay;



public class BinTree< TKey extends Number & Comparable<? super TKey>,
                      TNode extends BinNode<TKey,TNode>
                    >
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected TNode root = null;
    protected Traveler<TKey, TNode> traveler = new RecurTraveler<>();



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



    public List<TKey> traverse(OrderTraverse order) {
        var res = traveler.traverse(this.root, order);
        return res;
    }



    public String display(BinTreeDisplay disp) {
        String res = disp.get(this.root);
        return res;
    }



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
