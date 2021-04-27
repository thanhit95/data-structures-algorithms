package binarytree;


import java.util.List;



public class AvlTree< TKey extends Comparable<? super TKey> >
             extends BinSearchTree< TKey, AvlNode<TKey> >
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////
//                        CONSTRUCTORS
//////////////////////////////////////////////////////////////



    public AvlTree() {
    }



    public AvlTree(CandidateRemoval canddRM) {
        super(canddRM);
    }



    public AvlTree(List<TKey> lst) {
        super(lst);
    }



    public AvlTree(List<TKey> lst, CandidateRemoval canddRM) {
        super(lst, canddRM);
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    @Override
    public int height() {
        return (null == this.root) ? 0 : this.root.height();
    }



    @Override
    public AvlTree<TKey> clone() {
        var theClone = new AvlTree<TKey>();

        if (null != this.root) {
            theClone.root = this.root.cloneBranch();
        }

        theClone.traversal = this.traversal;
        theClone._count = this._count;
        theClone.optionCanddRM = this.optionCanddRM;

        return theClone;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    @Override
    protected AvlNode<TKey> _insert(AvlNode<TKey> node, TKey key) {
        node = super._insert(node, key);
        node = adjustBalance(node);
        return node;
    }



    @Override
    protected AvlNode<TKey> _remove(AvlNode<TKey> node, TKey key) {
        node = super._remove(node, key);

        if (null != node) {
            node = adjustBalance(node);
        }

        return node;
    }



    protected AvlNode<TKey> adjustBalance(AvlNode<TKey> node) {
        // STEP 1. Update the height of the node
        node.updateHeight();

        // STEP 2. Get the balance factor
        int balance = node.balance();
        int balanceLe = node.balanceLeft();
        int balanceRi = node.balanceRight();

        // STEP 3. Process if the node is unbalanced ==> 4 cases

        // Case 1: left-left
        if (  balance > 1 && balanceLe >= 0  )
            return rotateRight(node);

        // Case 2: right-right
        if (  balance < -1 && balanceRi <= 0  )
            return rotateLeft(node);

        // Case 3: left-right
        if (  balance > 1 && balanceLe < 0  ) {
            node.left = rotateLeft(node.left);
            return rotateRight(node);
        }

        // Case 4: right-left
        if (  balance < -1 && balanceRi > 0  ) {
            node.right = rotateRight(node.right);
            return rotateLeft(node);
        }

        return node;
    }



    protected AvlNode<TKey> rotateLeft(AvlNode<TKey> node) {
        /*
            node
            /  \
           ..   V
               / \
              a   b
        */
        var V = node.right;
        var a = V.left;

        V.left = node;
        node.right = a;

        node.updateHeight();
        V.updateHeight();

        return V;
    }



    protected AvlNode<TKey> rotateRight(AvlNode<TKey> node) {
        /*
            node
            /  \
           V   ..
          / \
         a   b
        */
        var V = node.left;
        var b = V.right;

        V.right = node;
        node.left = b;

        node.updateHeight();
        V.updateHeight();

        return V;
    }



    @Override
    protected AvlNode<TKey> createNode(TKey key) {
        return new AvlNode<TKey>(key);
    }



    @Override
    protected void buildTreeFromSortedListNodeFunc(AvlNode<TKey> node) {
        node.updateHeight();
    }
}
