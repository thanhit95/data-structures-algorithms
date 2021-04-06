package binarytree;


import java.util.List;



public abstract class Traveler< TKey extends Number & Comparable<? super TKey>,
                                TNode extends BinNode<TKey,TNode>
                              >
{
    public abstract void traverse(TNode root, OrderTraverse order, List<?> result);
}



//////////////////////////////////////////////////////////////



class TravelerRecur< TKey extends Number & Comparable<? super TKey>,
                     TNode extends BinNode<TKey,TNode>
                   >
      extends Traveler<TKey, TNode>
{


    protected List<TKey> resPath;



    @SuppressWarnings("unchecked")
    @Override
    public void traverse(TNode root, OrderTraverse order, List<?> result) {
        resPath = (List<TKey>)result;
        resPath.clear();

        switch (order) {
        case PRE:
            traversePre(root);
            break;

        case IN:
            traverseIn(root);
            break;

        case POST:
            traversePost(root);
            break;

        default:
            break;
        }
    }



    protected void traversePre(TNode node) {
        if (null == node)
            return;

        resPath.add(node.key);
        traversePre(node.left);
        traversePre(node.right);
    }



    protected void traverseIn(TNode node) {
        if (null == node)
            return;

        traverseIn(node.left);
        resPath.add(node.key);
        traverseIn(node.right);
    }



    protected void traversePost(TNode node) {
        if (null == node)
            return;

        traversePost(node.left);
        traversePost(node.right);
        resPath.add(node.key);
    }
}
