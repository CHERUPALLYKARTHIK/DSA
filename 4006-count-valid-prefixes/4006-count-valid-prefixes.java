class Solution {
    public int countValidPrefixes(String s) {
        int len=s.length();
        int cnt=0;
        int one=0,zero=0;
        char ch[]=s.toCharArray();
        for(char c:ch){
            if(c=='0') zero++;
            else one++;
            if(Math.abs(one-zero)<=1) cnt++;
        }
        // Set<String> al=new HashSet<>();
        // for(int i=0;i<len;i++){
        //     for(int j=i;j<len;j++){
        //         // System.out.println(s.substring(i,j+1));
        //         if(check(s.substring(i,j+1))){
        //             if(al.add(s.substring(i,j+1))){
        //                 cnt++;
        //             }
        //             }
                    
        //         }
        //     }
        
        // // System.out.print(al);
        return cnt;
    }
    public static boolean check(String str){
       
        int one=0,zero=0;
        for(int i=0;i<str.length();i++){
            if(str.charAt(i)=='0') zero++;
            else one++;
        }
        if(Math.abs(one-zero)==1){
            return true;
        }
        
        return false;
    }
}