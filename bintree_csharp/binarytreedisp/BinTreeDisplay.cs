using System;
using System.Collections.Generic;
using System.Diagnostics;
using my.binarytree;


namespace my.binarytreedisp
{
    class BinTreeDisplay
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS
        //////////////////////////////////////////////////////////////



        protected ValueUtil Vutil = null;
        protected DisplayParser Parser = null;
        protected MatrixBuffer Buffer = null;

        protected int MarginLeft = 0;



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public BinTreeDisplay()
        {
            this.Vutil = new ValueUtil();
            this.Parser = new DisplayParser(this.Vutil);
        }



        public string Get<TKey, TNode>(TNode inputRoot)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            if (inputRoot is null)
                return string.Empty;

            process<TKey, TNode>(inputRoot);
            Debug.Assert(this.Buffer is not null);

            var res = this.Buffer.GetStr();

            this.Buffer = null;
            return res;
        }



        public List<string> GetLstRows<TKey, TNode>(TNode inputRoot)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            if (null == inputRoot)
                return new List<string>();

            process<TKey, TNode>(inputRoot);
            Debug.Assert(this.Buffer is not null);

            var res = this.Buffer.GetLstRows();

            this.Buffer = null;
            return res;
        }



        public void Config(char lineChar, int lineBrsp, int marginLeft, int floatPre)
        {
            if (marginLeft < 0)
                throw new ArgumentException("marginLeft must be a non-negative integer");

            if (lineBrsp < 1)
                throw new ArgumentException("lineBrsp must be a positive integer");

            if (floatPre < 0)
                throw new ArgumentException("floatPre must be a non-negative integer");

            // Finish arguments validation

            this.Parser.ConfigLine(lineChar, lineBrsp);
            this.Vutil.FloatPrecision = floatPre;
            this.MarginLeft = marginLeft;
        }



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected void process<TKey, TNode>(TNode inputRoot)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            int heightInpRoot = this.Parser.GetHeight<TKey, TNode>(inputRoot);
            int height = heightInpRoot * 3 - 2;

            ParsingNode parsingTree = this.Parser.BuildTree<TKey, TNode>(inputRoot);

            this.Buffer = new MatrixBuffer(parsingTree.Width + this.MarginLeft, height);

            FillBuffer(parsingTree, 1, this.MarginLeft);

            this.Parser.DestroyTree(ref parsingTree);
        }



        protected void FillBuffer(ParsingNode node, int depth, int marginGlobal)
        {
            if (node is null)
                return;

            int marginKey = marginGlobal + node.MarginKey;
            int marginLeft = marginGlobal + node.MarginLeftChild;
            int marginRight = marginGlobal + node.MarginRightChild;
            int marginGlobalRight = marginKey + 1 + node.SizeRightLine;

            this.Buffer.Fill(marginKey, depth * 3 - 3, node.Key);

            if (node.Left is not null || node.Right is not null)
                this.Buffer.Fill(marginKey, depth * 3 - 2, "|");

            if (node.Left is not null)
            {
                FillLine(FillDirection.LEFT, node.Left.Key, depth * 3 - 1, marginLeft, marginKey);
                FillBuffer(node.Left, depth + 1, marginGlobal);
            }

            if (node.Right is not null)
            {
                FillLine(FillDirection.RIGHT, node.Right.Key, depth * 3 - 1, marginKey, marginRight);
                FillBuffer(node.Right, depth + 1, marginGlobalRight);
            }
        }



        protected void FillLine(FillDirection direction, string childKey, int y, int margina, int marginb)
        {
            if (FillDirection.LEFT == direction)
            {
                margina += childKey.Length - 1;
            }

            this.Buffer.FillLine(this.Parser.LineChar, y, margina, marginb);
        }
    }



    //////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////



    enum FillDirection
    {
        LEFT,
        RIGHT
    }
}
