#ifndef __VALUE_UTIL_HPP__
#define __VALUE_UTIL_HPP__


#include <string>
#include <iomanip>
#include <sstream>
#include <stdexcept>


namespace my
{
namespace btdisp
{



class ValueUtil
{
private:
    int _floatPrecision = 2;
    bool _floatFixed = true;


public:
    ValueUtil(const int &floatPrecision = 2, const bool &floatFixed = true)
    {
        if (floatPrecision >= 0)
        {
            this->_floatPrecision = floatPrecision;
        }

        this->_floatFixed = floatFixed;
    }



public:
    int getFloatPrecision() const
    {
        return this->_floatPrecision;
    }



    void setFloatPrecision(int precision)
    {
        if (precision < 0)
            throw std::invalid_argument("precision must be non-negative integer");

        this->_floatPrecision = precision;
    }



public:
    std::string getStr(short value) const
    {
        return std::to_string(value);
    }

    std::string getStr(int value) const
    {
        return std::to_string(value);
    }

    std::string getStr(long value) const
    {
        return std::to_string(value);
    }

    std::string getStr(long long value) const
    {
        return std::to_string(value);
    }


    std::string getStr(char const *str) const
    {
        return std::string(str);
    }

    std::string getStr(const std::string &str) const
    {
        return str;
    }



    std::string getStr(double value) const
    {
        std::ostringstream ss;

        if (this->_floatFixed)
            ss << std::fixed;

        ss << std::setprecision(this->_floatPrecision);

        ss << value;

        return ss.str();
    }
};



} // btdisp
} // my


#endif // __VALUE_UTIL_HPP__
