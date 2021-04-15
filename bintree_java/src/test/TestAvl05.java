package test;


import binarytree.AvlTree;
import binarytree.CandidateRemoval;



public class TestAvl05 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Character>(CandidateRemoval.RIGHT);

        for ( var value : "INFORMATIONTECHNOLOGY".toCharArray() ) {
            System.out.println("\n\n\n\n insert " + value + "\n");
            avl.insert(value);
            displayTree(avl);
        }

        System.out.println();


        for ( var value : "ECI".toCharArray() ) {
            System.out.println("\n\n\n\n remove " + value + "\n");
            avl.remove(value);
            displayTree(avl);
        }

        System.out.println();
    }

}
