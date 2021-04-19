using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;
using my.extensions;


namespace my.binarytree
{
    class BinSearchTree<TKey, TNode> : BinTree<TKey, TNode>
        where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS & PROPERTIES
        //////////////////////////////////////////////////////////////



        public int Count { get; protected set; } = 0;
        protected CandidateRemoval OptionCanddRM = CandidateRemoval.RIGHT;

        protected bool SuccessState = false;



        //////////////////////////////////////////////////////////////
        //                        CONSTRUCTORS
        //////////////////////////////////////////////////////////////



        public BinSearchTree()
        {
        }



        public BinSearchTree(CandidateRemoval canddRM)
        {
            this.OptionCanddRM = canddRM;
        }



        public BinSearchTree(List<TKey> lst)
        {
            if (lst is null)
                throw new ArgumentNullException("lst must not be null");

            this.ConstructFromList(lst);
        }



        public BinSearchTree(List<TKey> lst, CandidateRemoval canddRM) : this(lst)
        {
            this.OptionCanddRM = canddRM;
        }



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public bool Contain(TKey key)
        {
            if (key is null)
                throw new ArgumentNullException("key must not be null");

            var temp = Search(this.Root, key);
            TNode node = temp.Item1;
            return node is not null;
        }



        public override bool Insert(TKey key)
        {
            if (key is null)
                throw new ArgumentNullException("key must not be null");

            this.SuccessState = false;

            this.Root = _Insert(this.Root, key);

            if (false == this.SuccessState)
            {
                return false;
            }

            this.Count += 1;
            return true;
        }



        public override bool Remove(TKey key)
        {
            if (key is null)
                throw new ArgumentNullException("key must not be null");

            if (this.Root is null)
                return false;

            if (false == Contain(key))
                return false;

            this.Root = _Remove(this.Root, key);

            this.Count -= 1;
            return true;
        }



        public TKey Min()
        {
            if (this.Empty)
                throw new InvalidOperationException("Tree is empty");

            var temp = SearchMin(this.Root, null);
            TNode res = temp.Item1;

            return res.Key;
        }



        public TKey Max()
        {
            if (this.Empty)
                throw new InvalidOperationException("Tree is empty");

            var temp = SearchMax(this.Root, null);
            TNode res = temp.Item1;

            return res.Key;
        }



        public override BinSearchTree<TKey, TNode> Clone() => this.DeepCopy();



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected virtual TNode _Insert(TNode node, TKey key)
        {
            if (node is null)
            {
                this.SuccessState = true;
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

            return node;
        }



        protected virtual TNode _Remove(TNode node, TKey key)
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

            return node;
        }



        protected void RemoveCandidate(TNode node)
        {
            Debug.Assert(node is not null);

            TNode candidate = null;

            switch (this.OptionCanddRM)
            {
                case CandidateRemoval.RIGHT:
                    candidate = SearchMin(node.Right, node).Item1;
                    node.Key = candidate.Key;
                    node.Right = this._Remove(node.Right, candidate.Key);
                    break;

                case CandidateRemoval.LEFT:
                    candidate = SearchMax(node.Left, node).Item1;
                    node.Key = candidate.Key;
                    node.Left = this._Remove(node.Left, candidate.Key);
                    break;

                default:
                    break;
            }
        }



        protected (TNode, TNode) Search(TNode node, TKey key)
        {
            TNode parent = null;

            while (true)
            {
                if (node is null)
                    return (null, null);

                int compareKey = key.CompareTo(node.Key);

                if (0 == compareKey)
                    return new (node, parent);

                parent = node;

                if (compareKey < 0)
                    node = node.Left;
                else if (compareKey > 0)
                    node = node.Right;
            }

            // return (null, null); // ensure a value to return, unreachable statement...
        }



        protected (TNode, TNode) SearchMin(TNode node, TNode parent)
        {
            if (node is null)
                return (null, null);

            while (node.Left is not null)
            {
                parent = node;
                node = node.Left;
            }

            return (node, parent);
        }



        protected (TNode, TNode) SearchMax(TNode node, TNode parent)
        {
            if (node is null)
                return (null, null);

            while (node.Right is not null)
            {
                parent = node;
                node = node.Right;
            }

            return new (node, parent);
        }



        protected void ConstructFromList(List<TKey> lst)
        {
            this.DisposeRoot(ref this.Root);

            lst = lst.Distinct().OrderBy(v => v).ToList();
            int lenLst = lst.Count;

            this.Root = BuildTreeFromSortedList(lst, 0, lenLst - 1);
            this.Count = lenLst;
        }



        protected TNode BuildTreeFromSortedList(List<TKey> lst, int indexStart, int indexEnd)
        {
            if (indexStart > indexEnd)
                return null;

            int indexMid = (indexStart + indexEnd) / 2;
            TNode node = this.CreateNode(lst[indexMid]);

            node.Left = BuildTreeFromSortedList(lst, indexStart, indexMid - 1);
            node.Right = BuildTreeFromSortedList(lst, indexMid + 1, indexEnd);

            BuildTreeFromSortedListNodeFunc(node);

            return node;
        }



        protected virtual void BuildTreeFromSortedListNodeFunc(TNode node)
        {
        }

    }
}
