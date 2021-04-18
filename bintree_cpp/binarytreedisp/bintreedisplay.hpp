#ifndef __BIN_TREE_DISPLAY_HPP__
#define __BIN_TREE_DISPLAY_HPP__


#include <string>
#include <vector>
#include <stdexcept>
#include <cassert>
#include "valueutil.hpp"
#include "matrixbuffer.hpp"
#include "parsingnode.hpp"
#include "displayparser.hpp"



namespace my
{
namespace btdisp
{



enum class FillDirection
{
    LEFT,
    RIGHT
};



//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////



class BinTreeDisplay
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



protected:
    ValueUtil vutil;
    DisplayParser parser;
    MatrixBuffer *buffer = nullptr;

    int marginLeft = 0;



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



public:
    BinTreeDisplay(): parser(&vutil)
    {

    }



    template <typename TNode>
    std::string get(TNode *inputRoot)
    {
        if (nullptr == inputRoot)
            return "";

        process(inputRoot);
        assert(nullptr != this->buffer);

        auto res = this->buffer->getStr();

        delete this->buffer;
        this->buffer = nullptr;

        return res;
    }



    template <typename TNode>
    std::vector<std::string> getLstRows(TNode *inputRoot)
    {
        if (nullptr == inputRoot)
            return std::vector<std::string>();

        process(inputRoot);
        assert(nullptr != this->buffer);

        auto res = this->buffer->getLstRows();

        delete this->buffer;
        this->buffer = nullptr;

        return res;
    }



    void config(char lineChar = '-', int lineBrsp = 1, int marginLeft = 0, int floatPre = 2)
    {
        if (marginLeft < 0)
            throw std::invalid_argument("marginLeft must be a non-negative integer");

        if (lineBrsp < 1)
            throw std::invalid_argument("lineBrsp must be a positive integer");

        if (floatPre < 0)
            throw std::invalid_argument("floatPre must be a non-negative integer");

        // Finish arguments validation

        this->parser.configLine(lineChar, lineBrsp);
        this->vutil.setFloatPrecision(floatPre);
        this->marginLeft = marginLeft;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



protected:
    template <typename TNode>
    void process(TNode *inputRoot)
    {
        int heightInpRoot = this->parser.getHeight(inputRoot);
        int height = heightInpRoot * 3 - 2;

        ParsingNode *parsingTree = this->parser.buildTree(inputRoot);

        this->buffer = new MatrixBuffer(parsingTree->width + this->marginLeft, height);

        fillBuffer(parsingTree, 1, this->marginLeft);

        this->parser.destroyTree(parsingTree);
    }



    void fillBuffer(ParsingNode *node, int depth, int marginGlobal)
    {
        if (nullptr == node)
            return;

        int marginKey = marginGlobal + node->marginKey;
        int marginLeft = marginGlobal + node->marginLeftChild;
        int marginRight = marginGlobal + node->marginRightChild;
        int marginGlobalRight = marginKey + 1 + node->sizeRightLine;

        this->buffer->fill(marginKey, depth * 3 - 3, node->key);

        if (nullptr != node->left || nullptr != node->right)
            this->buffer->fill(marginKey, depth * 3 - 2, "|");

        if (nullptr != node->left)
        {
            fillLine(FillDirection::LEFT, node->left->key, depth * 3 - 1, marginLeft, marginKey);
            fillBuffer(node->left, depth + 1, marginGlobal);
        }

        if (nullptr != node->right)
        {
            fillLine(FillDirection::RIGHT, node->right->key, depth * 3 - 1, marginKey, marginRight);
            fillBuffer(node->right, depth + 1, marginGlobalRight);
        }
    }



    void fillLine(FillDirection direction, std::string childKey, int y, int margina, int marginb)
    {
        if (FillDirection::LEFT == direction)
        {
            margina += childKey.length() - 1;
        }

        this->buffer->fillLine(this->parser.lineChar, y, margina, marginb);
    }
};



} // btdisp
} // my



#endif // __BIN_TREE_DISPLAY_HPP__
