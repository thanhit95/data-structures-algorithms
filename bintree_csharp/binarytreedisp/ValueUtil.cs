using System;


namespace my.binarytreedisp
{
    class ValueUtil
    {
        private int _FloatPrecision;
        private string FormatString;


        public ValueUtil(int floatPrecision = 2)
        {
            this.FloatPrecision = floatPrecision;
        }



        public int FloatPrecision
        {
            get
            {
                return _FloatPrecision;
            }

            set
            {
                if (value < 0)
                    throw new ArgumentException("FloatPrecision must be a non-negative integer");

                this._FloatPrecision = value;
                this.FormatString = "0." + new string('#', value);
            }
        }



        public string GetStr<T>(T value)
        {
            if (value is null)
                return string.Empty;

            if (value is float valueF) return valueF.ToString(this.FormatString);
            if (value is double valueD) return valueD.ToString(this.FormatString);
            if (value is decimal valueM) return valueM.ToString(this.FormatString);

            return value.ToString();
        }
    }
}
