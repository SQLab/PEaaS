OG
=====
    autocompiler.py is compile AC codes automatically.
    outputgen.py is generate outputs.
    globalvar.py is define global var  here. # need import it
        EX : 執行路徑..... 等等
    two others are no use.
        But its context are about JAVA.



    How to run it ? This is linux version and absolute path. 
    First. # autocompiler
    1. put 某題號 AC codes in problist/code_file/某題號/
    2. cd to the same path where you put files in.
    3. type "python3.3 autocompiler.py 'pid' 'path' 'cpath'".  
      # 'pid' will be replace by 題號(1040X...)
      # 'path' 代表code的位置
      # 'cpath' 代表compile "program 放的位置"

    Second. # output generate
    1. put all files/dir in the same path.
    2. ctrl + alt + t to open terminal
    3. cd to the same path where you put files in.
    4. type "python3.3 outputgen.py 'pid'".  # 'pid' will be replace by 題號(1040X...)
