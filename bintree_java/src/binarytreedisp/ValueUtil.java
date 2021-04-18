package binarytreedisp;


import java.text.NumberFormat;



public class ValueUtil {
    private int floatPrecision = 2;
    private NumberFormat nf = NumberFormat.getInstance();



    public ValueUtil() {
        this(2);
    }



    public ValueUtil(int floatPrecision) {
        setFloatPrecision(floatPrecision);
    }



    public int getFloatPrecision() {
        return floatPrecision;
    }



    public void setFloatPrecision(int precision) {
        if (precision < 0)
            throw new IllegalArgumentException("float precision must be a non-negative integer");

        this.floatPrecision = precision;
        nf.setMaximumFractionDigits(precision);
    }



    public String getStr(int value) {
        return String.valueOf(value);
    }

    public String getStr(long value) {
        return String.valueOf(value);
    }

    public String getStr(float value) {
        //return String.valueOf(value);
        return nf.format(value);
    }

    public String getStr(double value) {
        //return String.valueOf(value);
        return nf.format(value);
    }

    public String getStr(char value) {
        return String.valueOf(value);
    }

    public String getStr(boolean value) {
        return String.valueOf(value);
    }

    public String getStr(Object value) {
        return String.valueOf(value);
    }
}
