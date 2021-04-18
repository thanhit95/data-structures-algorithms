using System;
using System.Collections.Generic;
using my.binarytree;
using my.binarytree.traversal;


namespace my.test
{
    class TestTraversal01 : TestBase
    {
        public override void doTask()
        {
            var bst = new BinSearchTree<int, BinNodeImp<int>>();

            foreach (var value in new int[] { 12, 39, 20, 7, 26, 45, 19, 8 })
                bst.Insert(value);


            Console.WriteLine("\n display tree:");
            DisplayTree(bst);


            Console.WriteLine("\n\n in-order traversal:");
            PrintList(bst.Traverse(OrderTraversal.IN));

            Console.WriteLine("\n\n pre-order traversal:");
            PrintList(bst.Traverse(OrderTraversal.PRE));

            Console.WriteLine("\n\n post-order traversal:");
            PrintList(bst.Traverse(OrderTraversal.POST));
        }



        private void PrintList<T>(List<T> lst)
        {
            foreach (var value in lst)
            {
                Console.Write($"{value}  ");
            }

            Console.WriteLine();
        }
    }
}
