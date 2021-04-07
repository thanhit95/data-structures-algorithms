package test;

import java.util.ArrayList;
import java.util.List;

import binarytree.*;
import binarytree.traveler.OrderTraverse;



public abstract class TestBase {

    public void printTree(BinTree<?,?> tree) {

        List<?> res = new ArrayList<>();
        tree.traverse(OrderTraverse.IN, res);

        System.out.println("\n\n print tree: ");

        for (var value: res) {
            System.out.print(value + "  ");
        }

        System.out.println();
    }



    public void displayTree(BinTree<?,?> tree) {

    }



    public abstract void doTask();
}
