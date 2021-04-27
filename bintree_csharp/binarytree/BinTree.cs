using System;
using System.Collections.Generic;
using my.binarytree.traversal;
using my.binarytreedisp;
using my.extensions;


namespace my.binarytree
{
    abstract class BinTree<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS
        //////////////////////////////////////////////////////////////



        protected TNode Root = null;
        protected ITraversal<TKey, TNode> Traversal = new RecurTraversal<TKey, TNode>();



        //////////////////////////////////////////////////////////////
        //                        ABSTRACT METHODS & PROPERTIES
        //////////////////////////////////////////////////////////////



        public abstract int Size { get; protected set; }
        public abstract bool Insert(TKey key);
        public abstract bool Remove(TKey key);



        //////////////////////////////////////////////////////////////
        //                        PROPERTIES
        //////////////////////////////////////////////////////////////



        public bool Empty => this.Root is null;
        public virtual int Height => this._Height(this.Root);



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public virtual void Clear() => DisposeRoot(ref this.Root);



        public List<TKey> Traverse(OrderTraversal order) => this.Traversal.Traverse(this.Root, order);



        public virtual BinTree<TKey, TNode> Clone() => this.DeepCopy();



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



        protected void DisposeRoot(ref TNode node)
        {
            if (node is null)
                return;

            DisposeRoot(ref node.Left);
            //node.Left = null;

            DisposeRoot(ref node.Right);
            //node.Right = null;

            node.Key = default;
            node = null;
        }
    }
}
