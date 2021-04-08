package binarytree;



public class AvlTree< TKey extends Number & Comparable<? super TKey> >
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
        theClone.assign(this);
        theClone.root = this._clone(this.root);
        return theClone;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    @Override
    protected AvlNode<TKey> _insert(AvlNode<TKey> node, TKey key) {
        if (null == node) {
            this.successState = true;
            return createNode(key);
        }

        int compareKey = key.compareTo(node.key);

        if (compareKey < 0) {
            node.left = _insert(node.left, key);
        }
        else if (compareKey > 0) {
            node.right = _insert(node.right, key);
        }

        node = adjustBalance(node);
        return node;
    }



    @Override
    protected AvlNode<TKey> _remove(AvlNode<TKey> node, TKey key) {
        int compareKey = key.compareTo(node.key);

        if (compareKey < 0) {
            node.left = _remove(node.left, key);
        }
        else if (compareKey > 0) {
            node.right = _remove(node.right, key);
        }
        else {
            if (null == node.left)
                return node.right;

            if (null == node.right)
                return node.left;

            removeCandidate(node);
        }

        node = adjustBalance(node);
        return node;
    }



    protected AvlNode<TKey> adjustBalance(AvlNode<TKey> node) {
        // STEP 1. Updates the height of the node
        node.updateHeight();

        // STEP 2. Gets the balance factor
        int balance = node.balance();
        int balanceLe = node.balanceLeft();
        int balanceRi = node.balanceRight();

        // STEP 3. Processes if the node is unbalanced ==> 4 cases

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
           ..   P
               / \
              a   b
        */
        var P = node.right;
        var a = P.left;

        P.left = node;
        node.right = a;

        node.updateHeight();
        P.updateHeight();

        return P;
    }



    protected AvlNode<TKey> rotateRight(AvlNode<TKey> node) {
        /*
            node
            /  \
           P   ..
          / \
         a   b
        */
        var P = node.left;
        var b = P.right;

        P.right = node;
        node.left = b;

        node.updateHeight();
        P.updateHeight();

        return P;
    }



    @Override
    protected AvlNode<TKey> createNode(TKey key) {
        return new AvlNode<TKey>(key);
    }
}
