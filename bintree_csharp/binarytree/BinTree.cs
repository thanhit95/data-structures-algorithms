using System;
using System.Collections.Generic;
using my.binarytree.traversal;
using my.binarytreedisp;
using my.extensions;


namespace my.binarytree
{
    class BinTree<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS
        //////////////////////////////////////////////////////////////



        protected TNode Root = null;
        protected BaseTraversal<TKey, TNode> Traversal = new RecurTraversal<TKey, TNode>();



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public bool Empty() => this.Root is null;



        public virtual int Height() => this._Height(this.Root);



        public void Clear() => FreeMemory(ref this.Root);



        public List<TKey> Traverse(OrderTraversal order) => this.Traversal.Traverse(this.Root, order);



        public virtual BinTree<TKey, TNode> Clone()
        {
            var theClone = this.DeepCopy();
            return theClone;
        }



        // Adapter method connecting BinTreeDisplay and BinTree
        public string Display(BinTreeDisplay disp)
        {
            var res = disp.Get<TKey, TNode>(this.Root);
            return res;
        }



        // Adapter method connecting BinTreeDisplay and BinTree
        public List<string> DisplayLstRows(BinTreeDisplay disp)
        {
            var res = disp.GetLstRows<TKey, TNode>(this.Root);
            return res;
        }



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected int _Height(TNode node)
        {
            if (node is null)
                return 0;

            int heightLe = _Height(node.Left);
            int heightRi = _Height(node.Right);

            return 1 + Math.Max(heightLe, heightRi);
        }



        protected virtual TNode CreateNode(TKey key)
        {
            var node = new TNode();
            node.Key = key;
            return node;
        }



        protected void FreeMemory(ref TNode node)
        {
            if (node is null)
                return;

            FreeMemory(ref node.Left);
            FreeMemory(ref node.Right);

            node.Key = default;
            node.Left = null;
            node.Right = null;
            node = null;
        }
    }
}
