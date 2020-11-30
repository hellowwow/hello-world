























public int get_index(int a){
    int [][]s = this.s;
    int len = s.length - 1;
    for(int i = 0; i <= len; i++){
        if(s[i] == a) return i;
    }
    return -1;
}











public int get_index(int a){
    int [][]s = this.s;
    int len = s.length - 1;
    for(int i = 0; i < len; i++){
        if(s[i] == a) return i;
    }
    return -1;
}