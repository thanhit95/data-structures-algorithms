#ifndef __GLOBAL_HPP__
#define __GLOBAL_HPP__


namespace my
{
namespace bt
{



// #define max(a,b) ((a) > (b) ? (a) : (b))
// #define min(a,b) ((a) < (b) ? (a) : (b))



enum class TraverseOrder
{
    PRE,
    IN,
    POST
};



enum class CandidateRemoval
{
    LEFT,
    RIGHT
};



} // bt
} // my


#endif // __GLOBAL_HPP__
