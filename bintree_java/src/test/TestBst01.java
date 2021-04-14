package test;


import binarytree.BinSearchTree;



public class TestBst01 extends TestBase {

    @Override
    public void doTask() {
        var bst = new BinSearchTree<Integer, BinNodeImp<Integer> >();

        for ( var value : new int[] {12, 39, 20, 7, 26, 45, 19, 8} )
            bst.insert(value);

        System.out.println("\n count: " + bst.count());
        System.out.println("\n min: " + bst.min());
        System.out.println("\n max: " + bst.max());
        System.out.println("\n contain: " + bst.contain(20));
        System.out.println("\n height: " + bst.height());

        System.out.println("\n print tree: ");
        printTree(bst);


        System.out.println("\n");


        bst.remove(800);
        bst.remove(12);

        System.out.println("\n count: " + bst.count());
        System.out.println("\n height: " + bst.height());

        System.out.println("\n print tree: ");
        printTree(bst);


        System.out.println();
    }

}
