using System;
using System.Collections.Generic;
using my.binarytree;
using my.binarytree.traversal;
using my.binarytreedisp;


namespace my.test
{
    abstract class TestBase
    {
        protected BinTreeDisplay disp;



        public TestBase()
        {
            disp = new BinTreeDisplay();
            disp.Config(
                '-',    // lineChar
                1,      // lineBrsp
                0,      // marginLeft
                2       // floatPre
            );
        }



        public void PrintTree<TKey, TNode>(BinTree<TKey, TNode> tree, OrderTraversal order = OrderTraversal.IN)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            List<TKey> res = tree.Traverse(order);

            foreach (var value in res)
            {
                Console.Write(value + "  ");
            }

            Console.WriteLine();
        }



        public void DisplayTree<TKey, TNode>(BinTree<TKey, TNode> tree)
            where TKey : IComparable where TNode : BinNode<TKey, TNode>, new()
        {
            var res = tree.Display(disp);
            Console.WriteLine(res);
        }



        public abstract void doTask();
    }
}
