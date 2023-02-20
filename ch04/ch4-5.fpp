10       	 <--SHAPES
12       	 <--LINES
id1
2       	 <--TYPE
286       	 <--LEFT
86       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
START



id2
2       	 <--TYPE
286       	 <--LEFT
464       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
STOP



id3
91       	 <--TYPE
239       	 <--LEFT
131       	 <--TOP
164       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
輸入選項值
choice

id4
92       	 <--TYPE
259       	 <--LEFT
186       	 <--TOP
124       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
choice
1

id5
91       	 <--TYPE
254       	 <--LEFT
302       	 <--TOP
133       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
輸入選項值是1


id7
92       	 <--TYPE
405       	 <--LEFT
250       	 <--TOP
124       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
choice
2

id11
91       	 <--TYPE
400       	 <--LEFT
346       	 <--TOP
133       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
輸入選項值是2


id12
91       	 <--TYPE
545       	 <--LEFT
403       	 <--TOP
133       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
輸入選項值是3


id10
92       	 <--TYPE
556       	 <--LEFT
310       	 <--TOP
112       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
choice
3

id16
91       	 <--TYPE
683       	 <--LEFT
404       	 <--TOP
148       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
請輸入1~3選項值


  
---- LINES ---- from,to ----
id3,id4
0

id7,id11
0
YES
id5,id2
0

id1,id3
0

id4,id5
0
YES
id10,id12
0
YES
id4,id7
0
NO
id7,id10
0
NO
id10,id16
0
NO
id11,id2
0

id12,id2
0

id16,id2
0

