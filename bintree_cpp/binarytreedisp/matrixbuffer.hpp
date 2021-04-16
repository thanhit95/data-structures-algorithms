#ifndef __MATRIX_BUFFER_HPP__
#define __MATRIX_BUFFER_HPP__


#include <string>
#include <cstring>
#include <vector>
#include <stdexcept>



namespace my
{
namespace btdisp
{



class MatrixBuffer
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



private:
    int _width = 0;
    int _height = 0;
    std::vector< std::vector<char> > a;



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



public:
    MatrixBuffer(const int &width, const int &height): _width(width), _height(height)
    {
        if (width < 1)
            throw std::invalid_argument("width must be a positive integer");

        if (height < 1)
            throw std::invalid_argument("height must be a positive integer");

        // init matrix
        this->a.resize(_height);

        for (auto &row : this->a)
            row.resize(_width, ' ');
    }



    int width() const
    {
        return _width;
    }



    int height() const
    {
        return _height;
    }



    void fill(int posx, int posy, const std::string &value)
    {
        if (posx < 0 || posx >= this->_width)
            throw std::invalid_argument("posx");

        if (posy < 0 || posy >= this->_height)
            throw std::invalid_argument("posy");

        int posxStart = posx;
        int lenValue = value.length();

        for (int i = 0; i < lenValue; ++i)
        {
            posx = posxStart + i;

            if (posx >= this->_width)
                break;

            this->a[posy][posx] = value[i];
        }
    }



    void fillLine(char character, int y, int startx, int endx)
    {
        for (int x = startx; x <= endx; ++x)
        {
            this->a[y][x] = character;
        }
    }



    std::string getStr() const
    {
        std::string res;
        std::vector<std::string> lstRows = getLstRows();

        for (auto &&row : lstRows)
            res += row + '\n';

        if (false == res.empty())
            res.pop_back();

        return res;
    }



    std::vector<std::string> getLstRows() const
    {
        std::vector<std::string> res;

        for (auto &&row : this->a)
        {
            std::string lineout(row.begin(), row.end());
            res.push_back(lineout);
        }

        return res;
    }
};



} // btdisp
} // my



#endif // __MATRIX_BUFFER_HPP__
