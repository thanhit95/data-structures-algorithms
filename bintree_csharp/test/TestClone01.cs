using System;
using my.binarytree;


namespace my.test
{
    class TestClone01 : TestBase
    {
        public override void doTask()
        {
            var a = new AvlTree<int>();

            foreach (var value in new int[] { 10, 20, 30, 40, 50, 25, 100, 28, 140 })
                a.Insert(value);


            Console.WriteLine(" display tree a:");
            DisplayTree(a);


            var b = a.Clone();
            b.Insert(22);
            b.Insert(29);
            Console.WriteLine("\n\n\n display tree b:");
            DisplayTree(b);
            Console.WriteLine("\n\n height tree b: " + b.Height());



            Console.WriteLine("\n\n\n display tree a (again):");
            DisplayTree(a);


            var c = a.Clone();
            c.Clear();
            Console.WriteLine("\n\n\n display tree c:");
            DisplayTree(c);


            Console.WriteLine();
        }
    }
}
