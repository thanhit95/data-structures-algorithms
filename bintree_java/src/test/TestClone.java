package test;

import binarytree.AvlTree;



public class TestClone extends TestBase {

    @Override
    public void doTask() {
        var a = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} )
            a.insert(value);


        System.out.println("display tree a:");
        displayTree(a);


        var b = a.clone();
        System.out.println("\n\n\n display tree b:");
        displayTree(b);
        System.out.println("\n\n height tree b: " + b.height());


        var c = a.clone();
        c.clear();
        System.out.println("\n\n\n display tree c:");
        displayTree(c);


        System.out.println();
    }

}
