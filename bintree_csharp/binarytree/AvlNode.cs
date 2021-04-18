using System;


namespace my.binarytree
{
    class AvlNode<TKey> : BinNode<TKey, AvlNode<TKey>>
        where TKey : IComparable
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS & PROPERTIES
        //////////////////////////////////////////////////////////////



        public int Height { get; protected set; } = 1;



        public int HeightLeft => (this.Left is null) ? 0 : this.Left.Height;

        public int HeightRight => (this.Right is null) ? 0 : this.Right.Height;



        public int Balance => HeightLeft - HeightRight;

        public int BalanceLeft => (this.Left is null) ? 0 : this.Left.Balance;

        public int BalanceRight => (this.Right is null) ? 0 : this.Right.Balance;



        //////////////////////////////////////////////////////////////
        //                        METHODS
        //////////////////////////////////////////////////////////////



        public AvlNode() : base(default)
        {
        }



        public AvlNode(TKey key) : base(key)
        {
        }



        public void UpdateHeight() => Height = 1 + Math.Max(HeightLeft, HeightRight);
    }
}
