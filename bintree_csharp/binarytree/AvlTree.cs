using System;
using System.Collections.Generic;
using my.extensions;


namespace my.binarytree
{
    class AvlTree<TKey> : BinSearchTree<TKey, AvlNode<TKey>>
        where TKey : IComparable
    {

        //////////////////////////////////////////////////////////////
        //                        CONSTRUCTORS
        //////////////////////////////////////////////////////////////



        public AvlTree()
        {
        }



        public AvlTree(CandidateRemoval canddRM) : base(canddRM)
        {
        }



        public AvlTree(List<TKey> lst) : base(lst)
        {
        }



        public AvlTree(List<TKey> lst, CandidateRemoval canddRM) : base(lst, canddRM)
        {
        }



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public override int Height() => (this.Root is null) ? 0 : this.Root.Height;



        public override AvlTree<TKey> Clone()
        {
            var theClone = this.DeepCopy();
            return theClone;
        }



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected override AvlNode<TKey> _Insert(AvlNode<TKey> node, TKey key)
        {
            if (node is null)
            {
                this.successState = true;
                return this.CreateNode(key);
            }

            int compareKey = key.CompareTo(node.Key);

            if (compareKey < 0)
            {
                node.Left = _Insert(node.Left, key);
            }
            else if (compareKey > 0)
            {
                node.Right = _Insert(node.Right, key);
            }

            node = AdjustBalance(node);
            return node;
        }



        protected override AvlNode<TKey> _Remove(AvlNode<TKey> node, TKey key)
        {
            if (node is null)
                return null;

            int compareKey = key.CompareTo(node.Key);

            if (compareKey < 0)
            {
                node.Left = _Remove(node.Left, key);
            }
            else if (compareKey > 0)
            {
                node.Right = _Remove(node.Right, key);
            }
            else
            {
                if (node.Left is null)
                    return node.Right;

                if (node.Right is null)
                    return node.Left;

                RemoveCandidate(node);
            }

            node = AdjustBalance(node);
            return node;
        }



        protected AvlNode<TKey> AdjustBalance(AvlNode<TKey> node)
        {
            // STEP 1. Update the height of the node
            node.UpdateHeight();

            // STEP 2. Get the balance factor
            int balance = node.Balance;
            int balanceLe = node.BalanceLeft;
            int balanceRi = node.BalanceRight;

            // STEP 3. Process if the node is unbalanced ==> 4 cases

            // Case 1: left-left
            if (balance > 1 && balanceLe >= 0)
                return RotateRight(node);

            // Case 2: right-right
            if (balance < -1 && balanceRi <= 0)
                return RotateLeft(node);

            // Case 3: left-right
            if (balance > 1 && balanceLe < 0)
            {
                node.Left = RotateLeft(node.Left);
                return RotateRight(node);
            }

            // Case 4: right-left
            if (balance < -1 && balanceRi > 0)
            {
                node.Right = RotateRight(node.Right);
                return RotateLeft(node);
            }

            return node;
        }



        protected AvlNode<TKey> RotateLeft(AvlNode<TKey> node)
        {
            /*
                node
                /  \
               ..   V
                   / \
                  a   b
            */
            var V = node.Right;
            var a = V.Left;

            V.Left = node;
            node.Right = a;

            node.UpdateHeight();
            V.UpdateHeight();

            return V;
        }



        protected AvlNode<TKey> RotateRight(AvlNode<TKey> node)
        {
            /*
                node
                /  \
               V   ..
              / \
             a   b
            */
            var V = node.Left;
            var b = V.Right;

            V.Right = node;
            node.Left = b;

            node.UpdateHeight();
            V.UpdateHeight();

            return V;
        }



        protected override void BuildTreeFromSortedListNodeFunc(AvlNode<TKey> node) => node.UpdateHeight();
    }
}
