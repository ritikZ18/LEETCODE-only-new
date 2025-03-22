// Last updated: 3/22/2025, 1:16:17 PM
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {

        // two sets for storing the resultant array or output


        /**
        Steps:

        Build two sets out of our passed in arrays.
        Iterate through the first set. If the second set contains a number in the first set, we remove it from the second set (cause it is a dupe). Otherwise, we add it to our resulting list.
        All remaining numbers in the second set are unique to array 2, so we can add them to our result. */
        List<List<Integer>> result = new ArrayList<>();

        Set<Integer> list1 = new HashSet<>();
        for (int n : nums1) {
            list1.add(n);
        }

        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();


        Set<Integer> list2 = new HashSet<>();
        for (int n : nums2) {
            list2.add(n);
        }

        for( int item : list1){
            if(list2.contains(item)){
                list2.remove(item);
            }
            else { 
                l1.add(item) ;
            }

        }

        for( int item : list2){
            if(list1.contains(item)){
                list1.remove(item);
            }
            else{
                l2.add(item);
            }
        }

        result.add(l1);
        result.add(l2);

        return result ; 

    }
}