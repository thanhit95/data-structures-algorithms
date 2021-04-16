#ifndef __INTERFACE_CLONE_BRANCH_HPP__
#define __INTERFACE_CLONE_BRANCH_HPP__



namespace my
{
namespace bt
{




template < typename TNode >
class ICloneBranch
{
public:
    virtual ~ICloneBranch() { }



public:
    virtual TNode* cloneBranch() const = 0;
};



} // bt
} // my



#endif // __INTERFACE_CLONE_BRANCH_HPP__
