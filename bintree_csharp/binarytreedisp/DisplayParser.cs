using System;
using my.binarytree;


namespace my.binarytreedisp
{
    class DisplayParser
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS
        //////////////////////////////////////////////////////////////



        public ValueUtil ValueUtil = null;
        public char LineChar;
        public int LineBrsp;



        //////////////////////////////////////////////////////////////
        //                        METHODS
        //////////////////////////////////////////////////////////////



        public DisplayParser(ValueUtil valueUtil, char character = '-', int branchSpacing = 1)
        {
            if (valueUtil is null)
                throw new ArgumentException("valueUtil cannot be null");

            this.ValueUtil = valueUtil;
            ConfigLine(character, branchSpacing);
        }



        public void ConfigLine(char character, int branchSpacing)
        {
            if (branchSpacing < 1)
                throw new ArgumentException("branchSpacing must be a positive integer");

            this.LineChar = character;
            this.LineBrsp = branchSpacing;
        }



        public ParsingNode BuildTree<TKey, TNode>(TNode inputRoot)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            if (inputRoot is null)
                return null;

            var node = new ParsingNode(this.ValueUtil.GetStr(inputRoot.Key));
            int lenKey = node.Key.Length;

            node.Left = BuildTree<TKey, TNode>(inputRoot.Left);
            node.Right = BuildTree<TKey, TNode>(inputRoot.Right);

            bool nodeLeftNull = (node.Left is null);
            bool nodeRightNull = (node.Right is null);

            int widthLeftBranch = nodeLeftNull ? 0 : node.Left.Width;
            int widthRightBranch = nodeRightNull ? 0 : node.Right.Width;

            int sizeLeftLine = nodeLeftNull ? 0 : this.LineBrsp;
            int sizeRightLine = nodeRightNull ? 0 : this.LineBrsp;

            int fullWidth = widthLeftBranch + widthRightBranch + sizeLeftLine + sizeRightLine;

            int sizeRightOverflow = lenKey - (widthRightBranch + sizeRightLine);
            fullWidth += Math.Max(1, sizeRightOverflow);

            int marginKey = widthLeftBranch + sizeLeftLine;
            int marginLeftChild = nodeLeftNull ? 0 : node.Left.MarginKey;
            int marginRightChild = nodeRightNull ? 0 : marginKey + node.Right.MarginKey + sizeRightLine + 1;

            node.Width = fullWidth;
            node.WidthLeftBranch = widthLeftBranch;
            node.WidthRightBranch = widthRightBranch;
            node.SizeLeftLine = sizeLeftLine;
            node.SizeRightLine = sizeRightLine;

            node.MarginKey = marginKey;
            node.MarginLeftChild = marginLeftChild;
            node.MarginRightChild = marginRightChild;

            return node;
        }



        public void DestroyTree(ref ParsingNode node)
        {
            if (node is null)
                return;

            DestroyTree(ref node.Left);
            node.Left = null;

            DestroyTree(ref node.Right);
            node.Right = null;

            node.Key = null;
            node = null;
        }



        public int GetHeight<TKey, TNode>(TNode node)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            if (node is null)
                return 0;

            int heightLe = GetHeight<TKey, TNode>(node.Left);
            int heightRi = GetHeight<TKey, TNode>(node.Right);

            return 1 + Math.Max(heightLe, heightRi);
        }
    }
}
