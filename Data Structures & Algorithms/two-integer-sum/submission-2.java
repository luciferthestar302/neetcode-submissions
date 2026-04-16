class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> h_map = new HashMap<>(); //using hashmap
        for (int i=0;i<nums.length;i++){
            // int complement = target-nums[i]; //this is the main logic which will give the logic to think
            if(h_map.containsKey(target-nums[i]))
                return new int[] {h_map.get(target-nums[i]), i}; 
        h_map.put(nums[i],i);
        }
    throw new IllegalArgumentException("no match found");       
    } 
}
