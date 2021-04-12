package binarytree;



public class BinNode< TKey extends Number & Comparable<? super TKey>,
                      TNode extends BinNode<TKey,TNode>
                    >
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
    public TNode cloneBranch() {
        var theClone = new BinNode<TKey, TNode>(this.key);

        if (null != this.left)
            theClone.left = this.left.cloneBranch();

        if (null != this.right)
            theClone.right = this.right.cloneBranch();

        return (TNode) theClone;
    }
}
