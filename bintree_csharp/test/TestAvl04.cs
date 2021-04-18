using System;
using my.binarytree;


namespace my.test
{
    class TestAvl04 : TestBase
    {
        public override void doTask()
        {
            var avl = new AvlTree<int>(CandidateRemoval.RIGHT);

            foreach (var value in new int[] { 10, 20, 30, 40, 50, 25, 100, 28, 140 })
            {
                Console.WriteLine($"\n\n\n\n insert {value}\n");
                avl.Insert(value);
                DisplayTree(avl);
            }

            Console.WriteLine();


            foreach (var value in new int[] { 30, 50, 140, 25, 20, 10, 40, 100, 28 })
            {
                Console.WriteLine($"\n\n\n\n remove {value}\n");
                avl.Remove(value);
                DisplayTree(avl);
            }

            Console.WriteLine();
        }
    }
}
