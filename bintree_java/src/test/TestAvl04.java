package test;


import binarytree.AvlTree;
import binarytree.CandidateRemoval;



public class TestAvl04 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>(CandidateRemoval.RIGHT);

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} ) {
            System.out.println("\n\n\n insert " + value);
            avl.insert(value);
            displayTree(avl);
        }

        System.out.println();


        for ( var value : new int[] {30, 50, 140, 25, 20, 10, 40, 100, 28} ) {
            System.out.println("\n\n\n remove " + value);
            avl.remove(value);
            displayTree(avl);
        }


        System.out.println();
    }

}
