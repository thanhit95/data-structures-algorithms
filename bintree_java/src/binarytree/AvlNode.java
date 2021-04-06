package binarytree;



public class AvlNode< TKey extends Number & Comparable<? super TKey> >
             extends BinNode< TKey, AvlNode<TKey> >
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected int _height = 1;



//////////////////////////////////////////////////////////////
//                        METHODS
//////////////////////////////////////////////////////////////



    public AvlNode() {
        super();
    }



    public AvlNode(TKey key) {
        super();
        this.key = key;
    }



    public int height() {
        return this._height;
    }



    public int heightLeft() {
        return (null == this.left) ? 0 : this.left.height();
    }



    public int heightRight() {
        return (null == this.right) ? 0 : this.right.height();
    }



    void updateHeight() {
        this._height = 1 + Math.max(heightLeft(), heightRight());
    }



    int balance() {
        int heightLe = heightLeft();
        int heightRi = heightRight();
        return heightLe - heightRi;
    }



    int balanceLeft() {
        return (null == this.left) ? 0 : this.left.balance();
    }



    int balanceRight() {
        return (null == this.right) ? 0 : this.right.balance();
    }
}
