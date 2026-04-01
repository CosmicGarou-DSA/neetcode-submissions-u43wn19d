
class Solution {
    public static boolean hasDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        return s.size() != nums.length; // true if duplicates exist
    }

public static void main(String[] args) {
    System.out.println(hasDuplicate(new int[]{1, 2, 3, 3}));
    }
}