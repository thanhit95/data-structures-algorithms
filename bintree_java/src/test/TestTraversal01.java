package test;


import java.util.List;
import binarytree.BinSearchTree;
import binarytree.traversal.OrderTraversal;



public class TestTraversal01 extends TestBase {

    @Override
    public void doTask() {
        var bst = new BinSearchTree<Integer, BinNodeImp<Integer> >();

        for ( var value : new int[] {12, 39, 20, 7, 26, 45, 19, 8} )
            bst.insert(value);


        System.out.println("\n display tree:");
        displayTree(bst);


        System.out.println("\n\n in-order traversal:");
        printList(bst.traverse(OrderTraversal.IN));

        System.out.println("\n\n pre-order traversal:");
        printList(bst.traverse(OrderTraversal.PRE));

        System.out.println("\n\n post-order traversal:");
        printList(bst.traverse(OrderTraversal.POST));
    }


    private void printList(List<?> lst) {
        for (var value : lst) {
            System.out.print(value + "  ");
        }

        System.out.println();
    }
}
