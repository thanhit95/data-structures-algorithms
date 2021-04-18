package binarytreedisp;


import java.util.List;
import java.util.ArrayList;
import java.lang.StringBuffer;



class MatrixBuffer {


//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



    private int _width = 0;
    private int _height = 0;

    private List<StringBuffer> a;



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



    public MatrixBuffer(int width, int height) {
        if (width < 1)
            throw new IllegalArgumentException("width must be a positive integer");

        if (height < 1)
            throw new IllegalArgumentException("height must be a positive integer");

        this._width = width;
        this._height = height;

        initMatrix();
    }



    public int width() {
        return this._width;
    }



    public int height() {
        return this._height;
    }



    public void fill(int posx, int posy, String value) {
        if (posx < 0 || posx >= this._width)
            throw new IllegalArgumentException("posx");

        if (posy < 0 || posy >= this._height)
            throw new IllegalArgumentException("posy");

        int posxStart = posx;
        int lenValue = value.length();

        for (int i = 0; i < lenValue; ++i) {
            posx = posxStart + i;

            if (posx >= this._width)
                break;

            // a[posy][posx] = value[i];
            a.get(posy).setCharAt(posx, value.charAt(i));
        }
    }



    public void fillLine(char character, int y, int startx, int endx) {
        for (int x = startx; x <= endx; ++x) {
            a.get(y).setCharAt(x, character);
        }
    }



    public String getStr() {
        String res = String.join(System.lineSeparator(), this.a);
        return res;
    }



    public List<String> getLstRows() {
        List<String> res = new ArrayList<>();

        for (var row : this.a) {
            String lineout = row.toString();
            res.add(lineout);
        }

        return res;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



    protected void initMatrix() {
        this.a = new ArrayList<>(this._height);

        for (int i = 0; i < this._height; ++i) {
            var row = new StringBuffer(this._width);

            for (int j = 0; j < this._width; ++j)
                row.append(' ');

            a.add(row);
        }
    }
}
