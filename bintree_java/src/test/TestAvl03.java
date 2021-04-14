package test;


import binarytree.AvlTree;



public class TestAvl03 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} ) {
            System.out.println("\n\n\n insert " + value);
            avl.insert(value);
            System.out.println(" height: " + avl.height());
            printTree(avl);
        }

        System.out.println();


        for ( var value : new int[] {30, 50, 140, 25, 20, 10, 40, 100, 28} ) {
            System.out.println("\n\n\n remove " + value);
            avl.remove(value);
            System.out.println(" height: " + avl.height());
            printTree(avl);
        }


        System.out.println();
    }

}
