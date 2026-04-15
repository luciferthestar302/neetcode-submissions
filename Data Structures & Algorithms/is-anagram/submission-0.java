class Solution {
    public boolean isAnagram(String s, String t) {
        int m = s.length();
        int n = t.length();
        if(m!=n)
            return false;
    //AGAR EQUAL HONGE TABHI TOH CODE AAGE BADHEGA NA
        int count_Char[] = new int[26];
        for(int i=0;i<m;i++){
            count_Char[s.charAt(i)-'a']++;
            count_Char[t.charAt(i)-'a']--;
        }
        for(int count:count_Char){
            if(count!=0){
                return false;
            }
        } 
        return true;  
    }
}
