package test;

import binarytree.AvlTree;


public class TestAvl01 extends TestBase {
    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>();

        for ( var value : new int[]{10, 20, 30, 40, 50, 25} )
            avl.insert(value);

        System.out.println("\n\n count: " + avl.count());

        System.out.println("\n\n min: " + avl.getMin());

        System.out.println("\n\n max: " + avl.getMax());

        System.out.println("\n\n contain: " + avl.contain(50));

        System.out.println("\n\n height: " + avl.height());

        printTree(avl);

        System.out.println();
    }
}
