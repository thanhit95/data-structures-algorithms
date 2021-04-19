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
        //                        PROPERTIES
        //////////////////////////////////////////////////////////////



        public override int Height => (this.Root is null) ? 0 : this.Root.Height;



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public override AvlTree<TKey> Clone() => this.DeepCopy();



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected override AvlNode<TKey> _Insert(AvlNode<TKey> node, TKey key)
        {
            node = base._Insert(node, key);
            node = AdjustBalance(node);
            return node;
        }



        protected override AvlNode<TKey> _Remove(AvlNode<TKey> node, TKey key)
        {
            node = base._Remove(node, key);

            if (node is not null)
            {
                node = AdjustBalance(node);
            }

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
