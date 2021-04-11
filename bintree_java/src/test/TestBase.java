package test;


import java.util.List;

import binarytree.*;
import binarytree.traversal.OrderTraversal;
import binarytreedisp.*;



public abstract class TestBase {



    protected BinTreeDisplay disp;



    public TestBase() {
        disp = new BinTreeDisplay();
        disp.config('-', 1, 0, 2);
    }



    public void printTree(BinTree<?,?> tree) {

        List<?> res = tree.traverse(OrderTraversal.IN);

        System.out.println("\n\n print tree: ");

        for (var value: res) {
            System.out.print(value + "  ");
        }

        System.out.println();
    }



    public void displayTree(BinTree<?,?> tree) {
        var res = tree.display(disp);
        System.out.println(res);
    }



    public abstract void doTask();
}
