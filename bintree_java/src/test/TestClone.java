package test;

import binarytree.AvlTree;



public class TestClone extends TestBase {

    @Override
    public void doTask() {
        var a = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} )
            a.insert(value);


        var b = a.clone();

        displayTree(b);

        System.out.println();
    }

}
