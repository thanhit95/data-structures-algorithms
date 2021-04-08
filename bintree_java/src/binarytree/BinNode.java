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
}
