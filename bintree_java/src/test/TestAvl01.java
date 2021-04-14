package test;


import binarytree.AvlTree;



public class TestAvl01 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>();

        for ( var value : new int[] {10, 20, 30, 40, 50, 25} )
            avl.insert(value);

        System.out.println("\n\n count: " + avl.count());
        System.out.println("\n\n min: " + avl.min());
        System.out.println("\n\n max: " + avl.max());
        System.out.println("\n\n contain: " + avl.contain(50));
        System.out.println("\n\n height: " + avl.height());

        System.out.println("\n\n print tree: ");
        printTree(avl);

        System.out.println();
    }

}
