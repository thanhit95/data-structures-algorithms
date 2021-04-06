package binarytree;


import java.util.List;



public class BinTree< TKey extends Number & Comparable<? super TKey>,
                      TNode extends BinNode<TKey,TNode>
                    >
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected TNode root = null;
    protected Traveler<TKey, TNode> traveler = new TravelerRecur<TKey, TNode>();



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    public boolean empty() {
        return null == root;
    }



    public int height() {
        return 0;
    }



    public void clear() {
        freeMemory(this.root);
    }



    public BinTree<TKey, TNode> clone() {
        var theClone = new BinTree<TKey, TNode>();
        theClone.root = theClone.root.clone();
        return theClone;
    }



    public void traverse(OrderTraverse order, List<?> result) {
        traveler.traverse(this.root, order, result);
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
