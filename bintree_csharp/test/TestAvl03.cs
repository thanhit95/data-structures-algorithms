using System;
using my.binarytree;


namespace my.test
{
    class TestAvl03 : TestBase
    {
        public override void doTask()
        {
            var avl = new AvlTree<int>();

            foreach (var value in new int[] { 10, 20, 30, 40, 50, 25, 100, 28, 140 })
            {
                Console.WriteLine($"\n\n\n insert {value}");
                avl.Insert(value);
                Console.WriteLine($" height: {avl.Height()}");
                PrintTree(avl);
            }

            Console.WriteLine();


            foreach (var value in new int[] { 30, 50, 140, 25, 20, 10, 40, 100, 28 })
            {
                Console.WriteLine($"\n\n\n remove {value}");
                avl.Remove(value);
                Console.WriteLine($" height: {avl.Height()}");
                PrintTree(avl);
            }

            Console.WriteLine();
        }
    }
}
