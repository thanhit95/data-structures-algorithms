using System;
using System.Collections.Generic;


namespace my.binarytree.traversal
{
    class RecurTraversal<TKey, TNode> : BaseTraversal<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {
        protected List<TKey> ResPath = null;



        public override List<TKey> Traverse(TNode root, OrderTraversal order)
        {
            ResPath = new List<TKey>();

            switch (order)
            {
                case OrderTraversal.PRE:
                    TraversePre(root);
                    break;

                case OrderTraversal.IN:
                    TraverseIn(root);
                    break;

                case OrderTraversal.POST:
                    TraversePost(root);
                    break;

                default:
                    break;
            }

            return ResPath;
        }



        protected void TraversePre(TNode node)
        {
            if (null == node)
                return;

            ResPath.Add(node.Key);
            TraversePre(node.Left);
            TraversePre(node.Right);
        }



        protected void TraverseIn(TNode node)
        {
            if (null == node)
                return;

            TraverseIn(node.Left);
            ResPath.Add(node.Key);
            TraverseIn(node.Right);
        }



        protected void TraversePost(TNode node)
        {
            if (null == node)
                return;

            TraversePost(node.Left);
            TraversePost(node.Right);
            ResPath.Add(node.Key);
        }
    }
}
