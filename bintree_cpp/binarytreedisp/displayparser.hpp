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



template <typename TNode>
class DisplayParser
{
public:
    ValueUtil * valueUtil = nullptr;
    char line_char = '-';
    int  line_brsp = 1;


public:
    DisplayParser(ValueUtil *valueUtil, char character = '-', int branchSpacing = 1) : valueUtil(valueUtil)
    {
        if (nullptr == valueUtil)
            throw std::invalid_argument("valueUtil cannot be nullptr");

        // configLine(character, branchSpacing);
    }



public:
    void configLine(char character, int branchSpacing)
    {
        if (branchSpacing < 1)
            throw std::invalid_argument("branchSpacing must be positive integer");

        this->line_char = character;
        this->line_brsp = branchSpacing;
    }



public:
    int getHeight(TNode *node) const
    {
        if (nullptr == node)
            return 0;

        int heightLeBranch = getHeight(node->left);
        int heightRiBranch = getHeight(node->right);

        return 1 + std::max(heightLeBranch, heightRiBranch);
    }



public:
    ParsingNode* buildTree(TNode *inputRoot)
    {
        if (nullptr == inputRoot)
            return nullptr;

        ParsingNode *node = new ParsingNode(this->valueUtil->getStr(inputRoot->key));
        int lenKey = node->key.length();

        node->left = buildTree(inputRoot->left);
        node->right = buildTree(inputRoot->right);

        bool nodeLeftNull = (nullptr == node->left);
        bool nodeRightNull = (nullptr == node->right);

        int widthLeftBranch = nodeLeftNull ? 0 : node->left->width;
        int widthRightBranch = nodeRightNull ? 0 : node->right->width;

        int sizeLeftLine = nodeLeftNull ? 0 : this->line_brsp;
        int sizeRightLine = nodeRightNull ? 0 : this->line_brsp;

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



public:
    void destroyParsingTree(ParsingNode *node)
    {
        if (nullptr == node)
            return;

        if (nullptr != node->left)
        {
            destroyParsingTree(node->left);
            node->left = nullptr;
        }

        if (nullptr != node->right)
        {
            destroyParsingTree(node->right);
            node->right = nullptr;
        }

        delete node;
        node = nullptr;
    }
};



} // btdisp
} // my


#endif // __DISPLAY_PARSER_HPP__
