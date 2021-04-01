#ifndef __DISPLAY_HPP__
#define __DISPLAY_HPP__


#include <string>
#include <vector>
#include <stdexcept>
#include <cassert>
#include "valueutil.hpp"
#include "displayparser.hpp"
#include "parsingnode.hpp"
#include "matrixbuffer.hpp"



namespace my
{
namespace btdisp
{



template <typename TNode>
class BinTreeDisplay
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
protected:
    ValueUtil _vutil;
    DisplayParser<TNode> _parser;

    MatrixBuffer * _buffer = nullptr;

    int _marginLeft = 0;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    BinTreeDisplay(): _parser(&_vutil)
    {

    }



public:
    std::string get(TNode *inputRoot)
    {
        if (nullptr == inputRoot)
            return "";

        process(inputRoot);
        assert(nullptr != this->_buffer);

        auto res = this->_buffer->getStr();

        delete this->_buffer;
        this->_buffer = nullptr;

        return res;
    }



    std::vector<std::string> getLstRows(TNode *inputRoot)
    {
        if (nullptr == inputRoot)
            return std::vector<std::string>();

        process(inputRoot);
        assert(nullptr != this->_buffer);

        auto res = this->_buffer->getLstRows();

        delete this->_buffer;
        this->_buffer = nullptr;

        return res;
    }



    void config(char line_char = '-', int line_brsp = 1, int marginLeft = 0, int floatPre = 2)
    {
        if (marginLeft < 0)
            throw std::invalid_argument("marginLeft must be non-negative integer");

        if (line_brsp < 1)
            throw std::invalid_argument("line_brsp must be positive integer");

        if (floatPre < 0)
            throw std::invalid_argument("floatPre must be non-negative integer");

        // Finish arguments validation

        this->_parser.configLine(line_char, line_brsp);
        this->_vutil.setFloatPrecision(floatPre);
        this->_marginLeft = marginLeft;
    }



protected:
    void process(TNode *inputRoot)
    {
        int heightInpRoot = this->_parser.getHeight(inputRoot);
        int height = heightInpRoot * 3 - 2;

        ParsingNode *parserTree = this->_parser.buildTree(inputRoot);

        this->_buffer = new MatrixBuffer(parserTree->width + this->_marginLeft, height);

        fillBuffer(parserTree, 1, this->_marginLeft);
    }



    void fillBuffer(ParsingNode *node, int depth, int marginGlobal)
    {
        if (nullptr == node)
            return;

        int marginKey = marginGlobal + node->marginKey;
        int marginLeft = marginGlobal + node->marginLeftChild;
        int marginRight = marginGlobal + node->marginRightChild;
        int marginGlobalRight = marginKey + 1 + node->sizeRightLine;

        this->_buffer->fill(marginKey, depth * 3 - 3, node->key);

        if (nullptr != node->left || nullptr != node->right)
            this->_buffer->fill(marginKey, depth * 3 - 2, "|");

        if (nullptr != node->left)
        {
            fillLine("left", node->left->key, depth * 3 - 1, marginLeft, marginKey);
            fillBuffer(node->left, depth + 1, marginGlobal);
        }

        if (nullptr != node->right)
        {
            fillLine("right", node->right->key, depth * 3 - 1, marginKey, marginRight);
            fillBuffer(node->right, depth + 1, marginGlobalRight);
        }
    }



    void fillLine(std::string direction, std::string childKey, int y, int margina, int marginb)
    {
        if ("right" == direction)
        {
            fillLineCoord(y, margina, marginb);
        }
        else if ("left" == direction)
        {
            margina += childKey.length() - 1;
            fillLineCoord(y, margina, marginb);
        }
        else
        {
            throw std::invalid_argument("direction");
        }
    }



    void fillLineCoord(int y, int startx, int endx)
    {
        auto &a = this->_buffer->_a;
        char lineChar = this->_parser.line_char;

        for (int x = startx; x <= endx; ++x)
        {
            a[y][x] = lineChar;
        }
    }
};



} // btdisp
} // my



#endif // __DISPLAY_HPP__
