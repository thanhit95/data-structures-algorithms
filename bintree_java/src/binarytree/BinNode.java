package binarytree;


public class BinNode< TKey extends Number & Comparable<? super TKey>,
                      TNode extends BinNode<TKey,TNode>
                    >
             implements Cloneable
{


    public TKey key = null;
    public TNode left = null;
    public TNode right = null;



    public BinNode() {
    }



    public BinNode(TKey key) {
        this.key = key;
    }



    @SuppressWarnings("unchecked")
    @Override
    public TNode clone() {
        TNode theClone = (TNode)new BinNode<>(this.key);

        if (null != this.left)
            theClone.left = this.left.clone();

        if (null != this.right)
            theClone.right = this.right.clone();

        return theClone;
    }
}
