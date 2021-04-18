package test;


import binarytree.AvlTree;



public class TestClone01 extends TestBase {

    @Override
    public void doTask() {
        var a = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25, 100, 28, 140} )
            a.insert(value);


        System.out.println(" display tree a:");
        displayTree(a);


        var b = a.clone();
        b.insert(22);
        b.insert(29);
        System.out.println("\n\n\n display tree b:");
        displayTree(b);
        System.out.println("\n\n height tree b: " + b.height());


        System.out.println("\n\n\n display tree a (again):");
        displayTree(a);


        var c = a.clone();
        c.clear();
        System.out.println("\n\n\n display tree c:");
        displayTree(c);


        System.out.println();
    }

}
