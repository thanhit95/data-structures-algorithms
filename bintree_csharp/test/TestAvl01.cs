using System;
using my.binarytree;


namespace my.test
{
    class TestAvl01 : TestBase
    {
        public override void doTask()
        {
            var avl = new AvlTree<int>();

            foreach (var value in new int[] { 10, 20, 30, 40, 50, 25 })
                avl.Insert(value);

            Console.WriteLine("\n count: " + avl.Count);
            Console.WriteLine("\n min: " + avl.Min());
            Console.WriteLine("\n max: " + avl.Max());
            Console.WriteLine("\n contain: " + avl.Contain(50));
            Console.WriteLine("\n height: " + avl.Height());

            Console.WriteLine("\n print tree: ");
            PrintTree(avl);


            Console.WriteLine();
        }
    }
}
