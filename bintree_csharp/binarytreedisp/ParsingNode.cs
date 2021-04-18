namespace my.binarytreedisp
{
    class ParsingNode
    {
        public string Key = string.Empty;
        public ParsingNode Left = null;
        public ParsingNode Right = null;

        public int Width = 0;
        public int WidthLeftBranch = 0;
        public int WidthRightBranch = 0;
        public int SizeLeftLine = 0;
        public int SizeRightLine = 0;

        public int MarginKey = 0;
        public int MarginLeftChild = 0;
        public int MarginRightChild = 0;



        public ParsingNode()
        {
        }



        public ParsingNode(string key)
        {
            this.Key = key;
        }
    }
}
