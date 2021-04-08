package test;


import binarytree.BinSearchTree;



public class TestBst01 extends TestBase {

    @Override
    public void doTask() {
        var bst = new BinSearchTree<Integer, BinNodeImp<Integer> >();

        for ( var value : new int[] {12, 39, 20, 7, 26, 45, 19, 8} )
            bst.insert(value);

        System.out.println("\n\n count: " + bst.count());

        System.out.println("\n\n min: " + bst.min());

        System.out.println("\n\n max: " + bst.max());

        System.out.println("\n\n contain: " + bst.contain(20));

        printTree(bst);


        bst.remove(800);
        bst.remove(12);

        System.out.println("\n\n count: " + bst.count());

        printTree(bst);


        System.out.println();
    }

}
