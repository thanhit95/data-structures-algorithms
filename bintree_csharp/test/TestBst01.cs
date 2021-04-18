using System;
using my.binarytree;


namespace my.test
{
    class TestBst01 : TestBase
    {
        public override void doTask()
        {
            var bst = new BinSearchTree<int, BinNodeConcrete<int>>();

            foreach (var value in new int[] { 12, 39, 20, 7, 26, 45, 19, 8 })
                bst.Insert(value);

            Console.WriteLine("\n count: " + bst.Count);
            Console.WriteLine("\n min: " + bst.Min());
            Console.WriteLine("\n max: " + bst.Max());
            Console.WriteLine("\n contain: " + bst.Contain(20));
            Console.WriteLine("\n height: " + bst.Height);

            Console.WriteLine("\n print tree: ");
            PrintTree(bst);


            Console.WriteLine("\n");


            bst.Remove(800);
            bst.Remove(12);

            Console.WriteLine("\n count: " + bst.Count);
            Console.WriteLine("\n height: " + bst.Height);

            Console.WriteLine("\n print tree: ");
            PrintTree(bst);


            Console.WriteLine();
        }
    }
}
