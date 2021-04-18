using System;
using my.binarytree;


namespace my.test
{
    class TestAvl05 : TestBase
    {
        public override void doTask()
        {
            var avl = new AvlTree<char>(CandidateRemoval.RIGHT);

            foreach (var value in "INFORMATIONTECHNOLOGY")
            {
                Console.WriteLine($"\n\n\n\n insert {value}\n");
                avl.Insert(value);
                DisplayTree(avl);
            }

            Console.WriteLine();


            foreach (var value in "ECI")
            {
                Console.WriteLine($"\n\n\n\n remove {value}\n");
                avl.Remove(value);
                DisplayTree(avl);
            }

            Console.WriteLine();
        }
    }
}
