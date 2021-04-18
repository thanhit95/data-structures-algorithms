package test;


import binarytree.BinSearchTree;
import binarytreedisp.BinTreeDisplay;



public class TestDisplay01 extends TestBase {

    @Override
    public void doTask() {
        var bst = new BinSearchTree<Double, BinNodeConcrete<Double   > >();

        for ( var value : new double[] {100, 50, 70000, 10, 88.523816, 20000, 90000, -123456, 14.78, 62, 500, 30000.19, 40000} )
            bst.insert(value);

        var disp = new BinTreeDisplay();
        disp.config(
                '-',    // lineChar
                1,      // lineBrsp
                0,      // marginLeft
                2       // floatPre
        );

        var res = bst.display(disp);

        System.out.println(res);
        System.out.println();
    }

}
