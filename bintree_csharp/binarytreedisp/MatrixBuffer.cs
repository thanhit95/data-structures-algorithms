using System;
using System.Collections.Generic;
using System.Linq;


namespace my.binarytreedisp
{
    class MatrixBuffer
    {

        //////////////////////////////////////////////////////////////
        //                        FIELDS & PROPERTIES
        //////////////////////////////////////////////////////////////



        public int Width { get; private set; } = 0;
        public int Height { get; private set; } = 0;

        private char[][] A;



        //////////////////////////////////////////////////////////////
        //                        METHODS (PUBLIC)
        //////////////////////////////////////////////////////////////



        public MatrixBuffer(int width, int height)
        {
            if (width < 1)
                throw new ArgumentException("width must be a positive integer");

            if (height < 1)
                throw new ArgumentException("height must be a positive integer");

            this.Width = width;
            this.Height = height;

            InitMatrix();
        }



        public void Fill(int posx, int posy, string value)
        {
            if (posx < 0 || posx >= this.Width)
                throw new ArgumentException("posx");

            if (posy < 0 || posy >= this.Height)
                throw new ArgumentException("posy");

            int posxStart = posx;
            int lenValue = value.Length;

            for (int i = 0; i < lenValue; ++i)
            {
                posx = posxStart + i;

                if (posx >= this.Width)
                    break;

                A[posy][posx] = value[i];
            }
        }



        public void FillLine(char character, int y, int startx, int endx)
        {
            for (int x = startx; x <= endx; ++x)
            {
                A[y][x] = character;
            }
        }



        public string GetStr() => string.Join(Environment.NewLine, this.GetLstRows());



        public List<string> GetLstRows() => (from row in this.A select new string(row)).ToList();



        //////////////////////////////////////////////////////////////
        //                        METHODS (PROTECTED)
        //////////////////////////////////////////////////////////////



        protected void InitMatrix()
        {
            this.A = new char[this.Height][];

            for (int i = 0; i < this.Height; ++i)
            {
                this.A[i] = Enumerable.Repeat(' ', this.Width).ToArray();
            }
        }
    }
}
