using System;
using my.binarytree;
using my.binarytreedisp;


namespace my.test
{
    class TestDisplay01 : TestBase
    {
        public override void doTask()
        {
            var bst = new BinSearchTree<double, BinNodeImp<double>>();

            foreach (var value in new double[] { 100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000 })
                bst.Insert(value);

            var disp = new BinTreeDisplay();
            disp.Config(
                '-',    // lineChar
                1,      // lineBrsp
                0,      // marginLeft
                2       // floatPre
            );

            var res = bst.Display(disp);

            Console.WriteLine(res);
            Console.WriteLine();
        }
    }
}
