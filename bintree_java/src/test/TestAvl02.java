package test;


import binarytree.AvlTree;



public class TestAvl02 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} ) {
            System.out.println("\n\n insert " + value);
            avl.insert(value);
            printTree(avl);
            System.out.println("\n height: " + avl.height());
        }

        System.out.println();


        for ( var value : new int[] {30, 50, 140, 25, 20, 10, 40, 100, 28} ) {
            System.out.println("\n\n remove " + value);
            avl.remove(value);
            printTree(avl);
            System.out.println("\n height: " + avl.height());
        }


        System.out.println();
    }

}
