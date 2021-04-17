using System;
using System.Collections.Generic;


namespace my.binarytree.traversal
{
    class NonRecurTraversal<TKey, TNode> : BaseTraversal<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>
    {
        public override List<TKey> Traverse(TNode root, OrderTraversal order)
        {
            var resPath = new List<TKey>();

            if (root is null)
                return resPath;

            switch (order)
            {
                case OrderTraversal.PRE:
                    TraversePre(root, ref resPath);
                    break;

                case OrderTraversal.IN:
                    TraverseIn(root, ref resPath);
                    break;

                case OrderTraversal.POST:
                    TraversePost(root, ref resPath);
                    break;

                default:
                    break;
            }

            return resPath;
        }



        protected void TraversePre(TNode node, ref List<TKey> resPath)
        {
            resPath.Clear();
            var stack = new Stack<TNode>();

            stack.Push(node);

            while (stack.Count > 0)
            {
                node = stack.Pop();
                resPath.Add(node.Key);

                if (node.Right is not null)
                    stack.Push(node.Right);

                if (node.Left is not null)
                    stack.Push(node.Left);
            }
        }



        protected void TraversePost(TNode node, ref List<TKey> resPath)
        {
            resPath.Clear();
            var stack = new Stack<TNode>();

            stack.Push(node);

            while (stack.Count > 0)
            {
                node = stack.Pop();
                resPath.Add(node.Key);

                if (node.Left is not null)
                    stack.Push(node.Left);

                if (node.Right is not null)
                    stack.Push(node.Right);
            }

            resPath.Reverse();
        }



        protected void TraverseIn(TNode node, ref List<TKey> resPath)
        {
            resPath.Clear();
            var stack = new Stack<TNode>();

            while (true)
            {
                while (node is not null)
                {
                    stack.Push(node);
                    node = node.Left;
                }

                if (0 == stack.Count)
                    break;

                var pickedNode = stack.Pop();
                resPath.Add(pickedNode.Key);

                node = pickedNode.Right;
            }
        }
    }
}
