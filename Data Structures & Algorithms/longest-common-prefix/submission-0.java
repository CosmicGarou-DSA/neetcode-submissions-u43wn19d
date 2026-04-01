class Solution {
    public static String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int i=0;
        String prefix=strs[0];
        String last=strs[strs.length-1];
        while (i<prefix.length() && i<last.length()){
            if(prefix.charAt(i)==last.charAt(i)){
            i++;
        }else{
        break;
    }
        }
        return prefix.substring(0,i);
        
    }
}
    
            