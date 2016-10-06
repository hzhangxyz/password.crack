#include <stdio.h>
#include <string.h>

int split_md5_and_bcrypt(char *file_name){
    FILE *fp  = fopen(file_name,"r");
    char md5_file[80], bcrypt_file[80], md5_cracked_file[80], bcrypt_cracked_file[80];
    sprintf(md5_file,"%s.md5",file_name);
    sprintf(bcrypt_file,"%s.bcrypt",file_name);
    sprintf(md5_cracked_file,"%s.md5.cracked",file_name);
    sprintf(bcrypt_cracked_file,"%s.bcrypt.cracked",file_name);
    FILE *md5            = fopen(md5_file,"w");
    FILE *bcrypt         = fopen(bcrypt_file,"w");
    FILE *md5_cracked    = fopen(md5_cracked_file,"w");
    FILE *bcrypt_cracked = fopen(bcrypt_cracked_file,"w");
    char hash[80];
    while(fgets(hash,80,fp)){
        int length = strlen(hash);
        if(length > 25)
            if(hash[1]!='2'){
                fprintf(md5,"%s",hash);
                fprintf(md5_cracked,"%s\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",hash);
            }
            else{
                fprintf(bcrypt,"%s",hash);
                fprintf(bcrypt_cracked,"%s\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n",hash);
            }
    }
    fclose(fp);
    fclose(md5);
    fclose(bcrypt);
    fclose(md5_cracked);
    fclose(bcrypt_cracked);
}

#ifdef DEBUG
int main(int argc,char** argv){
    if(argc>1)
        split_md5_and_bcrypt(argv[1]);
}
#endif
