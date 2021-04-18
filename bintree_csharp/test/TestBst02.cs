using System;
using my.binarytree;


namespace my.test
{
    class TestBst02 : TestBase
    {
        public override void doTask()
        {
            var bst = new BinSearchTree<int, BinNodeConcrete<int>>();

            foreach (var value in new int[] { 12, 39, 20, 7, 26, 45, 19, 8 })
                bst.Insert(value);

            PrintTree(bst);
            Console.WriteLine("\n height: " + bst.Height);


            foreach (var value in new int[] { 12, 39, 20, 7, 26, 45, 19, 8 })
                bst.Remove(value);

            PrintTree(bst);
            Console.WriteLine("\n height: " + bst.Height);


            Console.WriteLine();
        }
    }
}
