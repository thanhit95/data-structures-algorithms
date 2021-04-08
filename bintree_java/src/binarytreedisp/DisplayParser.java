package binarytreedisp;


import binarytree.BinNode;



class DisplayParser {

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    public ValueUtil valueUtil = null;
    public char lineChar;
    public int lineBrsp;



//////////////////////////////////////////////////////////////
//                        METHODS
//////////////////////////////////////////////////////////////



    public DisplayParser(ValueUtil valueUtil) {
        this(valueUtil, '-', 1);
    }



    public DisplayParser(ValueUtil valueUtil, char character, int branchSpacing) {
        if (null == valueUtil)
            throw new IllegalArgumentException("valueUtil cannot be null");

        this.valueUtil = valueUtil;
        configLine(character, branchSpacing);
    }



    public void configLine(char character, int branchSpacing) {
        if (branchSpacing < 1)
            throw new IllegalArgumentException("branchSpacing must be a positive integer");

        this.lineChar = character;
        this.lineBrsp = branchSpacing;
    }



    public < TNode extends BinNode<?,TNode> >
    ParsingNode
    buildTree(TNode inputRoot)
    {
        if (null == inputRoot)
            return null;

        var node = new ParsingNode(this.valueUtil.getStr(inputRoot.key));
        int lenKey = node.key.length();

        node.left = buildTree(inputRoot.left);
        node.right = buildTree(inputRoot.right);

        boolean nodeLeftNull = (null == node.left);
        boolean nodeRightNull = (null == node.right);

        int widthLeftBranch = nodeLeftNull ? 0 : node.left.width;
        int widthRightBranch = nodeRightNull ? 0 : node.right.width;

        int sizeLeftLine = nodeLeftNull ? 0 : this.lineBrsp;
        int sizeRightLine = nodeRightNull ? 0 : this.lineBrsp;

        int fullWidth = widthLeftBranch + widthRightBranch + sizeLeftLine + sizeRightLine;

        int sizeRightOverflow = lenKey - (widthRightBranch + sizeRightLine);
        fullWidth += Math.max(1, sizeRightOverflow);

        int marginKey = widthLeftBranch + sizeLeftLine;
        int marginLeftChild = nodeLeftNull ? 0 : node.left.marginKey;
        int marginRightChild = nodeRightNull ? 0 : marginKey + node.right.marginKey + sizeRightLine + 1;

        node.width = fullWidth;
        node.widthLeftBranch = widthLeftBranch;
        node.widthRightBranch = widthRightBranch;
        node.sizeLeftLine = sizeLeftLine;
        node.sizeRightLine = sizeRightLine;

        node.marginKey = marginKey;
        node.marginLeftChild = marginLeftChild;
        node.marginRightChild = marginRightChild;

        return node;
    }



    public void destroyTree(ParsingNode node) {
        if (null == node)
            return;

        destroyTree(node.left);
        node.left = null;

        destroyTree(node.right);
        node.right = null;
    }



    public < TNode extends BinNode<?,TNode> >
    int
    getHeight(TNode node) {
        if (null == node)
            return 0;

        int heightLe = getHeight(node.left);
        int heightRi = getHeight(node.right);

        return 1 + Math.max(heightLe, heightRi);
    }
}
