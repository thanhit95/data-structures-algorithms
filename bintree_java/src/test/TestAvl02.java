package test;


import java.util.List;
import binarytree.AvlTree;



public class TestAvl02 extends TestBase {

    @Override
    public void doTask() {
        var avl = new AvlTree<Integer>(List.of(10, 20, 30, 40, 50, 25));

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
