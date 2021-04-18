using System;
using System.Collections.Generic;
using my.binarytree;


namespace my.test
{
    class TestAvl02 : TestBase
    {
        public override void doTask()
        {
            var avl = new AvlTree<int>(new List<int>(new int[] { 10, 20, 30, 40, 50, 25 }));

            Console.WriteLine("\n count: " + avl.Count);
            Console.WriteLine("\n min: " + avl.Min());
            Console.WriteLine("\n max: " + avl.Max());
            Console.WriteLine("\n contain: " + avl.Contain(50));
            Console.WriteLine("\n height: " + avl.Height);

            Console.WriteLine("\n print tree: ");
            PrintTree(avl);

            Console.WriteLine();
        }
    }
}
