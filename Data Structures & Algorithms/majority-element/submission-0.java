class Solution {
    public int majorityElement(int[] nums) {
     HashMap<Integer, Integer>hm=new HashMap<>();
     for(int n:nums){
        hm.put(n,hm.getOrDefault(n,0)+1);
     }
     int maxval=Collections.max(hm.values());
    for(HashMap.Entry<Integer,Integer>hmentry:hm.entrySet()){
        if(hmentry.getValue().equals(maxval)){
            return hmentry.getKey();
        }
    }
    return -1;
    }
}