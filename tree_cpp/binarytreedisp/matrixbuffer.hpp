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
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
protected:
    int _width = 0;
    int _height = 0;

public:
    std::vector< std::vector<char> > _a;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    MatrixBuffer(const int &width, const int &height): _width(width), _height(height)
    {
        if (width < 1)
            throw std::invalid_argument("width must be positive integer");

        if (height < 1)
            throw std::invalid_argument("height must be positive integer");

        this->_a.resize(_height);

        for (auto &row : this->_a)
            row.resize(_width, ' ');
    }



public:
    int width() const
    {
        return _width;
    }

    int height() const
    {
        return _height;
    }



public:
    void fill(int posx, int posy, const std::string &value)
    {
        if (posx < 0 || posx >= this->_width)
            throw std::invalid_argument("posx");

        if (posy < 0 || posy >= this->_height)
            throw std::invalid_argument("posy");

        int lenValue = value.length();

        for (int i = 0; i< lenValue; ++i)
        {
            int idx = posx + i;

            if (idx >= this->_width)
                break;

            this->_a[posy][idx] = value[i];
        }
    }



public:
    std::string getStr() const
    {
        std::vector<std::string> lstRows = getLstRows();

        std::string res;

        for (auto &&row : lstRows)
            res += row + '\n';

        return res;
    }



    std::vector<std::string> getLstRows() const
    {
        std::vector<std::string> res;

        for (auto &&row : this->_a)
        {
            std::string srow(this->_width, ' ');

            for (int i = 0; i < row.size(); ++i)
                srow[i] = row[i];

            res.push_back(srow);
        }

        return res;
    }
};



} // btdisp
} // my


#endif // __MATRIX_BUFFER_HPP__
