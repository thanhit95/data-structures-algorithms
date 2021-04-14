package test;


import binarytree.BinSearchTree;



public class TestBst02 extends TestBase {

    @Override
    public void doTask() {
        var bst = new BinSearchTree<Integer, BinNodeImp<Integer> >();

        for ( var value : new int[] {12, 39, 20, 7, 26, 45, 19, 8} )
            bst.insert(value);

        printTree(bst);
        System.out.println("height: " + bst.height());


        for ( var value : new int[] {12, 39, 20, 7, 26, 45, 19, 8} )
            bst.remove(value);

        printTree(bst);
        System.out.println("height: " + bst.height());


        System.out.println();
    }

}
