#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char *file_name = getenv("HASH");
    FILE *fp  = fopen(file_name,"r");
    char md5_file[80], bcrypt_file[80], md5_cracked_file[80], bcrypt_cracked_file[80];
    sprintf(md5_file,"%s.md5",file_name);
    sprintf(bcrypt_file,"%s.bcr",file_name);
    sprintf(md5_cracked_file,"%s.md5.cracked",file_name);
    sprintf(bcrypt_cracked_file,"%s.bcr.cracked",file_name);
    FILE *md5            = fopen(md5_file,"w");
    FILE *bcrypt         = fopen(bcrypt_file,"w");
    FILE *md5_cracked    = fopen(md5_cracked_file,"w");
    FILE *bcrypt_cracked = fopen(bcrypt_cracked_file,"w");
    char hash[80];
    while(fscanf(fp,"%s",hash)!=-1){
        int length = strlen(hash);
        if(length > 25)
            if(hash[1]!='2'){
                fprintf(md5,"%s\n",hash);
                fprintf(md5_cracked,"%s:::::::::::::::::::::::::::::::::::::\n",hash);
            }
            else{
                fprintf(bcrypt,"%s\n",hash);
                fprintf(bcrypt_cracked,"%s:::::::::::::::::::::::::::::::::::::\n",hash);
            }
    }
    fclose(fp);
    fclose(md5);
    fclose(bcrypt);
    fclose(md5_cracked);
    fclose(bcrypt_cracked);
    return 0;
}

