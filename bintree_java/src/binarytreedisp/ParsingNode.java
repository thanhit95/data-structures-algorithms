package binarytreedisp;



class ParsingNode {
    public String key = "";
    public ParsingNode left = null;
    public ParsingNode right = null;

    public int width = 0;
    public int widthLeftBranch = 0;
    public int widthRightBranch = 0;
    public int sizeLeftLine = 0;
    public int sizeRightLine = 0;

    public int marginKey = 0;
    public int marginLeftChild = 0;
    public int marginRightChild = 0;



    public ParsingNode() {
    }



    public ParsingNode(String key) {
        this.key = key;
    }
}
