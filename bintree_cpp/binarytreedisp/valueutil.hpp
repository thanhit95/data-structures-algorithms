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
    int floatPrecision = 2;
    bool floatFixed = true;



public:
    ValueUtil(const int &floatPrecision = 2, const bool &floatFixed = true)
    {
        this->floatFixed = floatFixed;
        setFloatPrecision(floatPrecision);
    }



public:
    int getFloatPrecision() const
    {
        return this->floatPrecision;
    }



    void setFloatPrecision(int precision)
    {
        if (precision < 0)
            throw std::invalid_argument("float precision must be a non-negative integer");

        this->floatPrecision = precision;
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

    std::string getStr(char value) const
    {
        return std::string(1, value);
    }

    std::string getStr(const char *str) const
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
        configStringStream(ss);
        ss << value;
        return ss.str();
    }



    std::string getStr(long double value) const
    {
        std::ostringstream ss;
        configStringStream(ss);
        ss << value;
        return ss.str();
    }



    void configStringStream(std::ostringstream &ss) const
    {
        if (this->floatFixed)
            ss << std::fixed;

        ss << std::setprecision(this->floatPrecision);
    }
};



} // btdisp
} // my



#endif // __VALUE_UTIL_HPP__
