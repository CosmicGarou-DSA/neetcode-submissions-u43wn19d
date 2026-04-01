class Solution {
    public static boolean isAnagram(String s, String t) {
        char[] chra=s.toCharArray();
        char[] chra2=t.toCharArray();
        Arrays.sort(chra);
        Arrays.sort(chra2);

        if(Arrays.equals(chra,chra2)){
            return true;
        }else{
            return false;
        }

        }
        public static void main(String args[]){
            System.out.println(isAnagram("racecar", "carrace"));
        }
    }

