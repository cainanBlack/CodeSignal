/*
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].


Solution: Cainan Black
*/

bool solution(vector<int> s) {
    int fails = 0;
    int fails2 = 0;
    
    for(int i = 0; i < s.size()-1; i++){
        if(s[i] >= s[i+1]){
            fails++;
            cout << s[i] << " is greater than " << s[i+1] << endl;
        }
    }
    
    for(int c = 0; c < s.size()-2; c++){
        if(s[c] >= s[c+2]){
            fails2++;
            cout << s[c] << " is greater than " << s[c+2] << endl;
        }
    }
    
    if(fails < 2 && fails2 < 2){
        return true;
    } else {
        return false;
    }
}
