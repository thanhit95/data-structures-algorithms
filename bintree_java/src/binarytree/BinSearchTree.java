package binarytree;



public class BinSearchTree< TKey extends Number & Comparable<? super TKey>,
                            TNode extends BinNode<TKey,TNode>
                          >
             extends BinTree<TKey,TNode>
{


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected int _count = 0;
    protected CandidateRemoval optionCanddRM = CandidateRemoval.RIGHT;

    protected boolean successState = false;



//////////////////////////////////////////////////////////////
//                        CONSTRUCTORS
//////////////////////////////////////////////////////////////



    public BinSearchTree() {
    }



    public BinSearchTree(CandidateRemoval canddRM) {
        this.optionCanddRM = canddRM;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    public int count() {
        return this._count;
    }



    public boolean contain(TKey key) {
        var temp = search(this.root, key);
        TNode node = temp.first;
        return null != node;
    }



    public boolean insert(TKey key) {
        if (null == key)
            throw new IllegalArgumentException("key is null");

        this.successState = false;

        this.root = _insert(this.root, key);

        if (false == this.successState) {
            return false;
        }

        this._count += 1;
        return true;
    }



    public boolean remove(TKey key) {
        if (null == key)
            throw new IllegalArgumentException("key is null");

        if (null == this.root)
            return false;

        if (false == contain(key))
            return false;

        this.root = _remove(this.root, key);

        this._count -= 1;
        return true;
    }



    public TKey min() {
        if (empty())
            throw new IllegalStateException("Tree is empty");

        var temp = searchMin(this.root, null);
        TNode res = temp.first;

        return res.key;
    }



    public TKey max() {
        if (empty())
            throw new IllegalStateException("Tree is empty");

        var temp = searchMax(this.root, null);
        TNode res = temp.first;

        return res.key;
    }



    @Override
    public BinSearchTree<TKey, TNode> clone() {
        var theClone = new BinSearchTree<TKey, TNode>();
        theClone.assign(this);
        theClone.root = this._clone(this.root);
        return theClone;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    protected TNode _insert(TNode node, TKey key) {
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

        return node;
    }



    protected TNode _remove(TNode node, TKey key) {
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

        return node;
    }



    protected void removeCandidate(TNode node) {
        assert null != node;

        TNode candidate = null;

        switch (this.optionCanddRM) {
        case RIGHT:
            candidate = searchMin(node.right, node).first;
            node.key = candidate.key;
            node.right = this._remove(node.right, candidate.key);
            break;

        case LEFT:
            candidate = searchMax(node.left, node).first;
            node.key = candidate.key;
            node.left = this._remove(node.left, candidate.key);
            break;

        default:
            break;
        }
    }



    protected Tuple<TNode, TNode> search(TNode node, TKey key) {
        TNode parent = null;

        while (true) {
            if (null == node)
                return new Tuple<>(null, null);

            int compareKey = key.compareTo(node.key);

            if (0 == compareKey)
                return new Tuple<>(node, parent);

            parent = node;

            if (compareKey < 0)
                node = node.left;
            else if (compareKey > 0)
                node = node.right;
        }

        // return new Tuple<>(null, null); // ensures a value to return, unreachable statement...
    }



    protected Tuple<TNode, TNode> searchMin(TNode node, TNode parent) {
        if (null == node)
            return new Tuple<>(null, null);

        while (null != node.left) {
            parent = node;
            node = node.left;
        }

        return new Tuple<>(node, parent);
    }



    protected Tuple<TNode, TNode> searchMax(TNode node, TNode parent) {
        if (null == node)
            return new Tuple<>(null, null);

        while (null != node.right) {
            parent = node;
            node = node.right;
        }

        return new Tuple<>(node, parent);
    }



    protected void assign(BinSearchTree<TKey, TNode> other) {
        this._count = other._count;
        this.optionCanddRM = other.optionCanddRM;
    }



    protected TNode _clone(TNode node) {
        if (null == node)
            return null;

        TNode theClone = createNode(node.key);

        theClone.left = this._clone(node.left);
        theClone.right = this._clone(node.right);

        return theClone;
    }



    @SuppressWarnings("unchecked")
    protected TNode createNode(TKey key) {
        return (TNode) new BinNode<TKey, TNode>(key);
    }
}
