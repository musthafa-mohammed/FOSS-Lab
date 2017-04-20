administrator@administrator:~/mum$ nano marks.txt
------------------------------------------------------
1) Amit     Physics   80
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89

-----------------------------------------------------
administrator@administrator:~/mum$ awk '{print $3 "\t" $4}' marks.txt
Physics	80
Maths	90
Biology	87
English	85
History	89
administrator@administrator:~/mum$ awk '{print $2 "\t" $4}' marks.txt
Amit	80
Rahul	90
Shyam	87
Kedar	85
Hari	89
administrator@administrator:~/mum$ awk '/a/' marks.txt 
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
administrator@administrator:~/mum$ awk '/p/' marks.txt 
administrator@administrator:~/mum$ awk '/B/' marks.txt 
3) Shyam    Biology   87
administrator@administrator:~/mum$ awk 'length($0)>10' marks.txt
1) Amit     Physics   80
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
administrator@administrator:~/mum$ 
