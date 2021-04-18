#ifndef __DISPLAY_PARSER_HPP__
#define __DISPLAY_PARSER_HPP__


#include <algorithm>
#include <stdexcept>
#include "valueutil.hpp"
#include "parsingnode.hpp"



namespace my
{
namespace btdisp
{



class DisplayParser
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



public:
    ValueUtil *valueUtil = nullptr;
    char lineChar;
    int lineBrsp;



//////////////////////////////////////////////////////////////
//                        METHODS
//////////////////////////////////////////////////////////////



public:
    DisplayParser(ValueUtil *valueUtil, char character = '-', int branchSpacing = 1): valueUtil(valueUtil)
    {
        if (nullptr == valueUtil)
            throw std::invalid_argument("valueUtil cannot be nullptr");

        configLine(character, branchSpacing);
    }



    void configLine(char character, int branchSpacing)
    {
        if (branchSpacing < 1)
            throw std::invalid_argument("branchSpacing must be a positive integer");

        this->lineChar = character;
        this->lineBrsp = branchSpacing;
    }



    template <typename TNode>
    ParsingNode* buildTree(TNode *inputRoot) const
    {
        if (nullptr == inputRoot)
            return nullptr;

        auto *node = new ParsingNode(this->valueUtil->getStr(inputRoot->key));
        int lenKey = node->key.length();

        node->left = buildTree(inputRoot->left);
        node->right = buildTree(inputRoot->right);

        bool nodeLeftNull = (nullptr == node->left);
        bool nodeRightNull = (nullptr == node->right);

        int widthLeftBranch = nodeLeftNull ? 0 : node->left->width;
        int widthRightBranch = nodeRightNull ? 0 : node->right->width;

        int sizeLeftLine = nodeLeftNull ? 0 : this->lineBrsp;
        int sizeRightLine = nodeRightNull ? 0 : this->lineBrsp;

        int fullWidth = widthLeftBranch + widthRightBranch + sizeLeftLine + sizeRightLine;

        int sizeRightOverflow = lenKey - (widthRightBranch + sizeRightLine);
        fullWidth += std::max(1, sizeRightOverflow);

        int marginKey = widthLeftBranch + sizeLeftLine;
        int marginLeftChild = nodeLeftNull ? 0 : node->left->marginKey;
        int marginRightChild = nodeRightNull ? 0 : marginKey + node->right->marginKey + sizeRightLine + 1;

        node->width = fullWidth;
        node->widthLeftBranch = widthLeftBranch;
        node->widthRightBranch = widthRightBranch;
        node->sizeLeftLine = sizeLeftLine;
        node->sizeRightLine = sizeRightLine;

        node->marginKey = marginKey;
        node->marginLeftChild = marginLeftChild;
        node->marginRightChild = marginRightChild;

        return node;
    }



    void destroyTree(ParsingNode *&node) const
    {
        if (nullptr == node)
            return;

        destroyTree(node->left);
        destroyTree(node->right);

        delete node;
        node = nullptr;
    }



    template <typename TNode>
    int getHeight(TNode *node) const
    {
        if (nullptr == node)
            return 0;

        int heightLe = getHeight(node->left);
        int heightRi = getHeight(node->right);

        return 1 + std::max(heightLe, heightRi);
    }
};



} // btdisp
} // my



#endif // __DISPLAY_PARSER_HPP__
