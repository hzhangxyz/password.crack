#include <stdio.h>
#include <stdlib.h>

int main(){
    char *src = getenv("HASH");
    char *dst = getenv("ANSFILE");
    char md5[80],bcr[80];
    sprintf(md5,"%s.md5.cracked",src);
    sprintf(bcr,"%s.bcr.cracked",src);
    FILE *SRC = fopen(src,"r");
    FILE *MD5 = fopen(md5,"r");
    FILE *BCR = fopen(bcr,"r");
    FILE *DST = fopen(dst,"w");

    char md5_t[100],bcr_t[100],tmp[100];
    fscanf(MD5,"%s",md5_t);
    fscanf(BCR,"%s",bcr_t);

    while(fscanf(SRC,"%s",tmp)!=-1){
        if(tmp[1] != '2'){
            int i = 2;char *p = md5_t;
            for(;i!=0;){
                fputc(*p,DST);
                i-=(*(++p)==':');
            }
            fputc('\n',DST);
            fscanf(MD5,"%s",md5_t);
        }else{
            int i = 2;char *p = bcr_t;
            for(;i!=0;){
                fputc(*p,DST);
                i-=(*(++p)==':');
            }
            fputc('\n',DST);
            fscanf(BCR,"%s",bcr_t);
        }
    }
    return 0;
}
