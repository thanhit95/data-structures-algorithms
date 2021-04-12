package binarytreedisp;


import java.util.ArrayList;
import java.util.List;

import binarytree.BinNode;



public class BinTreeDisplay {

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    protected ValueUtil vutil = null;
    protected DisplayParser parser = null;

    protected MatrixBuffer buffer = null;

    protected int marginLeft = 0;



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    public BinTreeDisplay() {
        this.vutil = new ValueUtil();
        this.parser = new DisplayParser(this.vutil);
    }



    public < TNode extends BinNode<?,TNode> >
    String
    get(TNode inputRoot) {
        if (null == inputRoot)
            return "";

        process(inputRoot);
        assert null != this.buffer;

        var res = this.buffer.getStr();

        this.buffer = null;
        return res;
    }



    public < TNode extends BinNode<?,TNode> >
    List<String>
    getLstRows(TNode inputRoot) {
        if (null == inputRoot)
            return new ArrayList<>();

        process(inputRoot);
        assert null != this.buffer;

        var res = this.buffer.getLstRows();

        this.buffer = null;
        return res;
    }



    public void config(char lineChar, int lineBrsp, int marginLeft, int floatPre) {
        if (marginLeft < 0)
            throw new IllegalArgumentException("marginLeft must be a non-negative integer");

        if (lineBrsp < 1)
            throw new IllegalArgumentException("lineBrsp must be a positive integer");

        if (floatPre < 0)
            throw new IllegalArgumentException("floatPre must be a non-negative integer");

        // Finish arguments validation

        this.parser.configLine(lineChar, lineBrsp);
        this.vutil.setFloatPrecision(floatPre);
        this.marginLeft = marginLeft;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    protected < TNode extends BinNode<?,TNode> >
    void
    process(TNode inputRoot) {
        int heightInpRoot = this.parser.getHeight(inputRoot);
        int height = heightInpRoot * 3 - 2;

        ParsingNode parsingTree = this.parser.buildTree(inputRoot);

        this.buffer = new MatrixBuffer(parsingTree.width + this.marginLeft, height);

        fillBuffer(parsingTree, 1, this.marginLeft);

        this.parser.destroyTree(parsingTree);
    }



    protected void fillBuffer(ParsingNode node, int depth, int marginGlobal) {
        if (null == node)
            return;

        int marginKey = marginGlobal + node.marginKey;
        int marginLeft = marginGlobal + node.marginLeftChild;
        int marginRight = marginGlobal + node.marginRightChild;
        int marginGlobalRight = marginKey + 1 + node.sizeRightLine;

        this.buffer.fill(marginKey, depth * 3 - 3, node.key);

        if (null != node.left || null != node.right)
            this.buffer.fill(marginKey, depth * 3 - 2, "|");

        if (null != node.left) {
            fillLine(FillDirection.LEFT, node.left.key, depth * 3 - 1, marginLeft, marginKey);
            fillBuffer(node.left, depth + 1, marginGlobal);
        }

        if (null != node.right) {
            fillLine(FillDirection.RIGHT, node.right.key, depth * 3 - 1, marginKey, marginRight);
            fillBuffer(node.right, depth + 1, marginGlobalRight);
        }
    }



    protected void fillLine(FillDirection direction, String childKey, int y, int margina, int marginb) {
        if (FillDirection.LEFT == direction) {
            margina += childKey.length() - 1;
        }

        this.buffer.fillLine(this.parser.lineChar, y, margina, marginb);
    }
}



//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////



enum FillDirection {
    LEFT,
    RIGHT
}
