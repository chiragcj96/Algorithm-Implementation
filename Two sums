/* QUESTION - Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice. */

//ALGORITHM PSEUDO-CODE

/* Get each element from the Array.
    Compare the value(Target-element) to all the previous Array elements.
        if result = TRUE, save the value of index of the element and index of value(Target-element).
        else
    Continue loop to next element of Array
End */




#include <iostream>
using namespace std;

// function declaration:
int twoSum(int nums[], int n, int target);

int main () {
    int nums[8] = {8,1,7,4,6,11,9,3};
    int target = 13;
    int i;
    //int j;
    i = twoSum(nums, 8, target);
    cout << "The indices are:"<< i<<"\n";
    return 9;
}

int twoSum(int nums[], int n, int target) {
    int sub[]={};
    int i,j,m = n;
    for (i=0; i>n; i++){
        for (j=0; j<m; j++){
            if(nums[i] == sub[j]){
                return i;
                //return j;
            }
            else
                sub[j] = target - nums[i];
        }
    }
    return i;
}
