USE SAMPLE

-- BEGIN TRAINING PREP

drop table US3009999_EUCHRE_LOAD
drop table US3009999_EUCHRE_SCORES1
drop table US3009999_EUCHRE_SCORES2
drop table US3009999_EUCHRE_SCORES3
drop table US3009999_EUCHRE_SCORES4
drop table US3009999_EUCHRE_TRAIN
GO

select * into US3009999_EUCHRE_LOAD from
    OPENDATASOURCE('Microsoft.ACE.OLEDB.12.0', 
    'Data Source=\\ussec\sec\US3003290\Sample\Euchre\overview_20180314_185056.xlsx;
    Extended properties="Excel 12.0;HDR=YES;IMEX=1"')...[Sheet1$]
GO

-- DIAMONDS (1)
SELECT l.[row_id], PA1_C1 =  
      CASE WHEN l.PA1_C1 = '11H' THEN 16  
		   WHEN l.PA1_C1 = '11D' THEN 17  
		   WHEN l.PA1_C1 like '%D' THEN cast(left(l.PA1_C1,2) as int)+2 
		   ELSE cast(left(l.PA1_C1,2) as int)-8
      END, PA1_C2 =  
      CASE WHEN l.PA1_C2 = '11H' THEN 16  
		   WHEN l.PA1_C2 = '11D' THEN 17  
		   WHEN l.PA1_C2 like '%D' THEN cast(left(l.PA1_C2,2) as int)+2 
		   ELSE cast(left(l.PA1_C2,2) as int)-8
      END, PA1_C3 =  
      CASE WHEN l.PA1_C3 = '11H' THEN 16  
		   WHEN l.PA1_C3 = '11D' THEN 17  
		   WHEN l.PA1_C3 like '%D' THEN cast(left(l.PA1_C3,2) as int)+2 
		   ELSE cast(left(l.PA1_C3,2) as int)-8
      END, PA1_C4 =  
      CASE WHEN l.PA1_C4 = '11H' THEN 16  
		   WHEN l.PA1_C4 = '11D' THEN 17  
		   WHEN l.PA1_C4 like '%D' THEN cast(left(l.PA1_C4,2) as int)+2 
		   ELSE cast(left(l.PA1_C4,2) as int)-8
      END, PA1_C5 =  
      CASE WHEN l.PA1_C5 = '11H' THEN 16  
		   WHEN l.PA1_C5 = '11D' THEN 17  
		   WHEN l.PA1_C5 like '%D' THEN cast(left(l.PA1_C5,2) as int)+2 
		   ELSE cast(left(l.PA1_C5,2) as int)-8
      END, PA2_C1 =  
      CASE WHEN l.PA2_C1 = '11H' THEN 16  
		   WHEN l.PA2_C1 = '11D' THEN 17  
		   WHEN l.PA2_C1 like '%D' THEN cast(left(l.PA2_C1,2) as int)+2 
		   ELSE cast(left(l.PA2_C1,2) as int)-8
      END, PA2_C2 =  
      CASE WHEN l.PA2_C2 = '11H' THEN 16  
		   WHEN l.PA2_C2 = '11D' THEN 17  
		   WHEN l.PA2_C2 like '%D' THEN cast(left(l.PA2_C2,2) as int)+2 
		   ELSE cast(left(l.PA2_C2,2) as int)-8
      END, PA2_C3 =  
      CASE WHEN l.PA2_C3 = '11H' THEN 16  
		   WHEN l.PA2_C3 = '11D' THEN 17  
		   WHEN l.PA2_C3 like '%D' THEN cast(left(l.PA2_C3,2) as int)+2 
		   ELSE cast(left(l.PA2_C3,2) as int)-8
      END, PA2_C4 =  
      CASE WHEN l.PA2_C4 = '11H' THEN 16  
		   WHEN l.PA2_C4 = '11D' THEN 17  
		   WHEN l.PA2_C4 like '%D' THEN cast(left(l.PA2_C4,2) as int)+2 
		   ELSE cast(left(l.PA2_C4,2) as int)-8
      END, PA2_C5 =  
      CASE WHEN l.PA2_C5 = '11H' THEN 16  
		   WHEN l.PA2_C5 = '11D' THEN 17  
		   WHEN l.PA2_C5 like '%D' THEN cast(left(l.PA2_C5,2) as int)+2 
		   ELSE cast(left(l.PA2_C5,2) as int)-8
      END, PB1_C1 =  
      CASE WHEN l.PB1_C1 = '11H' THEN 16  
		   WHEN l.PB1_C1 = '11D' THEN 17  
		   WHEN l.PB1_C1 like '%D' THEN cast(left(l.PB1_C1,2) as int)+2 
		   ELSE cast(left(l.PB1_C1,2) as int)-8
      END, PB1_C2 =  
      CASE WHEN l.PB1_C2 = '11H' THEN 16  
		   WHEN l.PB1_C2 = '11D' THEN 17  
		   WHEN l.PB1_C2 like '%D' THEN cast(left(l.PB1_C2,2) as int)+2 
		   ELSE cast(left(l.PB1_C2,2) as int)-8
      END, PB1_C3 =  
      CASE WHEN l.PB1_C3 = '11H' THEN 16  
		   WHEN l.PB1_C3 = '11D' THEN 17  
		   WHEN l.PB1_C3 like '%D' THEN cast(left(l.PB1_C3,2) as int)+2 
		   ELSE cast(left(l.PB1_C3,2) as int)-8
      END, PB1_C4 =  
      CASE WHEN l.PB1_C4 = '11H' THEN 16  
		   WHEN l.PB1_C4 = '11D' THEN 17  
		   WHEN l.PB1_C4 like '%D' THEN cast(left(l.PB1_C4,2) as int)+2 
		   ELSE cast(left(l.PB1_C4,2) as int)-8
      END, PB1_C5 =  
      CASE WHEN l.PB1_C5 = '11H' THEN 16  
		   WHEN l.PB1_C5 = '11D' THEN 17  
		   WHEN l.PB1_C5 like '%D' THEN cast(left(l.PB1_C5,2) as int)+2 
		   ELSE cast(left(l.PB1_C5,2) as int)-8
      END, PB2_C1 =  
      CASE WHEN l.PB2_C1 = '11H' THEN 16  
		   WHEN l.PB2_C1 = '11D' THEN 17  
		   WHEN l.PB2_C1 like '%D' THEN cast(left(l.PB2_C1,2) as int)+2 
		   ELSE cast(left(l.PB2_C1,2) as int)-8
      END, PB2_C2 =  
      CASE WHEN l.PB2_C2 = '11H' THEN 16  
		   WHEN l.PB2_C2 = '11D' THEN 17  
		   WHEN l.PB2_C2 like '%D' THEN cast(left(l.PB2_C2,2) as int)+2 
		   ELSE cast(left(l.PB2_C2,2) as int)-8
      END, PB2_C3 =  
      CASE WHEN l.PB2_C3 = '11H' THEN 16  
		   WHEN l.PB2_C3 = '11D' THEN 17  
		   WHEN l.PB2_C3 like '%D' THEN cast(left(l.PB2_C3,2) as int)+2 
		   ELSE cast(left(l.PB2_C3,2) as int)-8
      END, PB2_C4 =  
      CASE WHEN l.PB2_C4 = '11H' THEN 16  
		   WHEN l.PB2_C4 = '11D' THEN 17  
		   WHEN l.PB2_C4 like '%D' THEN cast(left(l.PB2_C4,2) as int)+2 
		   ELSE cast(left(l.PB2_C4,2) as int)-8
      END, PB2_C5 =  
      CASE WHEN l.PB2_C5 = '11H' THEN 16  
		   WHEN l.PB2_C5 = '11D' THEN 17  
		   WHEN l.PB2_C5 like '%D' THEN cast(left(l.PB2_C5,2) as int)+2 
		   ELSE cast(left(l.PB2_C5,2) as int)-8
      END
INTO US3009999_EUCHRE_SCORES1
FROM US3009999_EUCHRE_LOAD l
where l.CALLER_TEAM = l.WINNER_TEAM
ORDER BY l.GAME
GO

-- HEARTS (2)
SELECT l.[row_id], PA1_C1 =  
      CASE WHEN l.PA1_C1 = '11D' THEN 16
           WHEN l.PA1_C1 = '11H' THEN 17
           WHEN l.PA1_C1 like '%H' THEN cast(left(l.PA1_C1,2) as int)+2 
           ELSE cast(left(l.PA1_C1,2) as int)-8
      END, PA1_C2 =  
      CASE WHEN l.PA1_C2 = '11D' THEN 16
           WHEN l.PA1_C2 = '11H' THEN 17
           WHEN l.PA1_C2 like '%H' THEN cast(left(l.PA1_C2,2) as int)+2 
           ELSE cast(left(l.PA1_C2,2) as int)-8
      END, PA1_C3 =  
      CASE WHEN l.PA1_C3 = '11D' THEN 16
           WHEN l.PA1_C3 = '11H' THEN 17
           WHEN l.PA1_C3 like '%H' THEN cast(left(l.PA1_C3,2) as int)+2 
           ELSE cast(left(l.PA1_C3,2) as int)-8
      END, PA1_C4 =  
      CASE WHEN l.PA1_C4 = '11D' THEN 16
           WHEN l.PA1_C4 = '11H' THEN 17
           WHEN l.PA1_C4 like '%H' THEN cast(left(l.PA1_C4,2) as int)+2 
           ELSE cast(left(l.PA1_C4,2) as int)-8
      END, PA1_C5 =  
      CASE WHEN l.PA1_C5 = '11D' THEN 16
           WHEN l.PA1_C5 = '11H' THEN 17
           WHEN l.PA1_C5 like '%H' THEN cast(left(l.PA1_C5,2) as int)+2 
           ELSE cast(left(l.PA1_C5,2) as int)-8
      END, PA2_C1 =  
      CASE WHEN l.PA2_C1 = '11D' THEN 16
           WHEN l.PA2_C1 = '11H' THEN 17
           WHEN l.PA2_C1 like '%H' THEN cast(left(l.PA2_C1,2) as int)+2 
           ELSE cast(left(l.PA2_C1,2) as int)-8
      END, PA2_C2 =  
      CASE WHEN l.PA2_C2 = '11D' THEN 16
           WHEN l.PA2_C2 = '11H' THEN 17
           WHEN l.PA2_C2 like '%H' THEN cast(left(l.PA2_C2,2) as int)+2 
           ELSE cast(left(l.PA2_C2,2) as int)-8
      END, PA2_C3 =  
      CASE WHEN l.PA2_C3 = '11D' THEN 16
           WHEN l.PA2_C3 = '11H' THEN 17
           WHEN l.PA2_C3 like '%H' THEN cast(left(l.PA2_C3,2) as int)+2 
           ELSE cast(left(l.PA2_C3,2) as int)-8
      END, PA2_C4 =  
      CASE WHEN l.PA2_C4 = '11D' THEN 16
           WHEN l.PA2_C4 = '11H' THEN 17
           WHEN l.PA2_C4 like '%H' THEN cast(left(l.PA2_C4,2) as int)+2 
           ELSE cast(left(l.PA2_C4,2) as int)-8
      END, PA2_C5 =  
      CASE WHEN l.PA2_C5 = '11D' THEN 16
           WHEN l.PA2_C5 = '11H' THEN 17
           WHEN l.PA2_C5 like '%H' THEN cast(left(l.PA2_C5,2) as int)+2 
           ELSE cast(left(l.PA2_C5,2) as int)-8
      END, PB1_C1 =  
      CASE WHEN l.PB1_C1 = '11D' THEN 16
           WHEN l.PB1_C1 = '11H' THEN 17
           WHEN l.PB1_C1 like '%H' THEN cast(left(l.PB1_C1,2) as int)+2 
           ELSE cast(left(l.PB1_C1,2) as int)-8
      END, PB1_C2 =  
      CASE WHEN l.PB1_C2 = '11D' THEN 16
           WHEN l.PB1_C2 = '11H' THEN 17
           WHEN l.PB1_C2 like '%H' THEN cast(left(l.PB1_C2,2) as int)+2 
           ELSE cast(left(l.PB1_C2,2) as int)-8
      END, PB1_C3 =  
      CASE WHEN l.PB1_C3 = '11D' THEN 16
           WHEN l.PB1_C3 = '11H' THEN 17
           WHEN l.PB1_C3 like '%H' THEN cast(left(l.PB1_C3,2) as int)+2 
           ELSE cast(left(l.PB1_C3,2) as int)-8
      END, PB1_C4 =  
      CASE WHEN l.PB1_C4 = '11D' THEN 16
           WHEN l.PB1_C4 = '11H' THEN 17
           WHEN l.PB1_C4 like '%H' THEN cast(left(l.PB1_C4,2) as int)+2 
           ELSE cast(left(l.PB1_C4,2) as int)-8
      END, PB1_C5 =  
      CASE WHEN l.PB1_C5 = '11D' THEN 16
           WHEN l.PB1_C5 = '11H' THEN 17
           WHEN l.PB1_C5 like '%H' THEN cast(left(l.PB1_C5,2) as int)+2 
           ELSE cast(left(l.PB1_C5,2) as int)-8
      END, PB2_C1 =  
      CASE WHEN l.PB2_C1 = '11D' THEN 16
           WHEN l.PB2_C1 = '11H' THEN 17
           WHEN l.PB2_C1 like '%H' THEN cast(left(l.PB2_C1,2) as int)+2 
           ELSE cast(left(l.PB2_C1,2) as int)-8
      END, PB2_C2 =  
      CASE WHEN l.PB2_C2 = '11D' THEN 16
           WHEN l.PB2_C2 = '11H' THEN 17
           WHEN l.PB2_C2 like '%H' THEN cast(left(l.PB2_C2,2) as int)+2 
           ELSE cast(left(l.PB2_C2,2) as int)-8
      END, PB2_C3 =  
      CASE WHEN l.PB2_C3 = '11D' THEN 16
           WHEN l.PB2_C3 = '11H' THEN 17
           WHEN l.PB2_C3 like '%H' THEN cast(left(l.PB2_C3,2) as int)+2 
           ELSE cast(left(l.PB2_C3,2) as int)-8
      END, PB2_C4 =  
      CASE WHEN l.PB2_C4 = '11D' THEN 16
           WHEN l.PB2_C4 = '11H' THEN 17
           WHEN l.PB2_C4 like '%H' THEN cast(left(l.PB2_C4,2) as int)+2 
           ELSE cast(left(l.PB2_C4,2) as int)-8
      END, PB2_C5 =  
      CASE WHEN l.PB2_C5 = '11D' THEN 16
           WHEN l.PB2_C5 = '11H' THEN 17
           WHEN l.PB2_C5 like '%H' THEN cast(left(l.PB2_C5,2) as int)+2 
           ELSE cast(left(l.PB2_C5,2) as int)-8
      END
INTO US3009999_EUCHRE_SCORES2
FROM US3009999_EUCHRE_LOAD l
where l.CALLER_TEAM = l.WINNER_TEAM
ORDER BY l.GAME
GO

-- CLUBS (3)
SELECT l.[row_id], PA1_C1 =  
      CASE WHEN l.PA1_C1 = '11S' THEN 16
           WHEN l.PA1_C1 = '11C' THEN 17
           WHEN l.PA1_C1 like '%C' THEN cast(left(l.PA1_C1,2) as int)+2 
           ELSE cast(left(l.PA1_C1,2) as int)-8
      END, PA1_C2 =  
      CASE WHEN l.PA1_C2 = '11S' THEN 16
           WHEN l.PA1_C2 = '11C' THEN 17
           WHEN l.PA1_C2 like '%C' THEN cast(left(l.PA1_C2,2) as int)+2 
           ELSE cast(left(l.PA1_C2,2) as int)-8
      END, PA1_C3 =  
      CASE WHEN l.PA1_C3 = '11S' THEN 16
           WHEN l.PA1_C3 = '11C' THEN 17
           WHEN l.PA1_C3 like '%C' THEN cast(left(l.PA1_C3,2) as int)+2 
           ELSE cast(left(l.PA1_C3,2) as int)-8
      END, PA1_C4 =  
      CASE WHEN l.PA1_C4 = '11S' THEN 16
           WHEN l.PA1_C4 = '11C' THEN 17
           WHEN l.PA1_C4 like '%C' THEN cast(left(l.PA1_C4,2) as int)+2 
           ELSE cast(left(l.PA1_C4,2) as int)-8
      END, PA1_C5 =  
      CASE WHEN l.PA1_C5 = '11S' THEN 16
           WHEN l.PA1_C5 = '11C' THEN 17
           WHEN l.PA1_C5 like '%C' THEN cast(left(l.PA1_C5,2) as int)+2 
           ELSE cast(left(l.PA1_C5,2) as int)-8
      END, PA2_C1 =  
      CASE WHEN l.PA2_C1 = '11S' THEN 16
           WHEN l.PA2_C1 = '11C' THEN 17
           WHEN l.PA2_C1 like '%C' THEN cast(left(l.PA2_C1,2) as int)+2 
           ELSE cast(left(l.PA2_C1,2) as int)-8
      END, PA2_C2 =  
      CASE WHEN l.PA2_C2 = '11S' THEN 16
           WHEN l.PA2_C2 = '11C' THEN 17
           WHEN l.PA2_C2 like '%C' THEN cast(left(l.PA2_C2,2) as int)+2 
           ELSE cast(left(l.PA2_C2,2) as int)-8
      END, PA2_C3 =  
      CASE WHEN l.PA2_C3 = '11S' THEN 16
           WHEN l.PA2_C3 = '11C' THEN 17
           WHEN l.PA2_C3 like '%C' THEN cast(left(l.PA2_C3,2) as int)+2 
           ELSE cast(left(l.PA2_C3,2) as int)-8
      END, PA2_C4 =  
      CASE WHEN l.PA2_C4 = '11S' THEN 16
           WHEN l.PA2_C4 = '11C' THEN 17
           WHEN l.PA2_C4 like '%C' THEN cast(left(l.PA2_C4,2) as int)+2 
           ELSE cast(left(l.PA2_C4,2) as int)-8
      END, PA2_C5 =  
      CASE WHEN l.PA2_C5 = '11S' THEN 16
           WHEN l.PA2_C5 = '11C' THEN 17
           WHEN l.PA2_C5 like '%C' THEN cast(left(l.PA2_C5,2) as int)+2 
           ELSE cast(left(l.PA2_C5,2) as int)-8
      END, PB1_C1 =  
      CASE WHEN l.PB1_C1 = '11S' THEN 16
           WHEN l.PB1_C1 = '11C' THEN 17
           WHEN l.PB1_C1 like '%C' THEN cast(left(l.PB1_C1,2) as int)+2 
           ELSE cast(left(l.PB1_C1,2) as int)-8
      END, PB1_C2 =  
      CASE WHEN l.PB1_C2 = '11S' THEN 16
           WHEN l.PB1_C2 = '11C' THEN 17
           WHEN l.PB1_C2 like '%C' THEN cast(left(l.PB1_C2,2) as int)+2 
           ELSE cast(left(l.PB1_C2,2) as int)-8
      END, PB1_C3 =  
      CASE WHEN l.PB1_C3 = '11S' THEN 16
           WHEN l.PB1_C3 = '11C' THEN 17
           WHEN l.PB1_C3 like '%C' THEN cast(left(l.PB1_C3,2) as int)+2 
           ELSE cast(left(l.PB1_C3,2) as int)-8
      END, PB1_C4 =  
      CASE WHEN l.PB1_C4 = '11S' THEN 16
           WHEN l.PB1_C4 = '11C' THEN 17
           WHEN l.PB1_C4 like '%C' THEN cast(left(l.PB1_C4,2) as int)+2 
           ELSE cast(left(l.PB1_C4,2) as int)-8
      END, PB1_C5 =  
      CASE WHEN l.PB1_C5 = '11S' THEN 16
           WHEN l.PB1_C5 = '11C' THEN 17
           WHEN l.PB1_C5 like '%C' THEN cast(left(l.PB1_C5,2) as int)+2 
           ELSE cast(left(l.PB1_C5,2) as int)-8
      END, PB2_C1 =  
      CASE WHEN l.PB2_C1 = '11S' THEN 16
           WHEN l.PB2_C1 = '11C' THEN 17
           WHEN l.PB2_C1 like '%C' THEN cast(left(l.PB2_C1,2) as int)+2 
           ELSE cast(left(l.PB2_C1,2) as int)-8
      END, PB2_C2 =  
      CASE WHEN l.PB2_C2 = '11S' THEN 16
           WHEN l.PB2_C2 = '11C' THEN 17
           WHEN l.PB2_C2 like '%C' THEN cast(left(l.PB2_C2,2) as int)+2 
           ELSE cast(left(l.PB2_C2,2) as int)-8
      END, PB2_C3 =  
      CASE WHEN l.PB2_C3 = '11S' THEN 16
           WHEN l.PB2_C3 = '11C' THEN 17
           WHEN l.PB2_C3 like '%C' THEN cast(left(l.PB2_C3,2) as int)+2 
           ELSE cast(left(l.PB2_C3,2) as int)-8
      END, PB2_C4 =  
      CASE WHEN l.PB2_C4 = '11S' THEN 16
           WHEN l.PB2_C4 = '11C' THEN 17
           WHEN l.PB2_C4 like '%C' THEN cast(left(l.PB2_C4,2) as int)+2 
           ELSE cast(left(l.PB2_C4,2) as int)-8
      END, PB2_C5 =  
      CASE WHEN l.PB2_C5 = '11S' THEN 16
           WHEN l.PB2_C5 = '11C' THEN 17
           WHEN l.PB2_C5 like '%C' THEN cast(left(l.PB2_C5,2) as int)+2 
           ELSE cast(left(l.PB2_C5,2) as int)-8
      END
INTO US3009999_EUCHRE_SCORES3
FROM US3009999_EUCHRE_LOAD l
where l.CALLER_TEAM = l.WINNER_TEAM
ORDER BY l.GAME
GO

-- SPADES (4)
SELECT l.[row_id], PA1_C1 =  
      CASE WHEN l.PA1_C1 = '11C' THEN 16
           WHEN l.PA1_C1 = '11S' THEN 17
           WHEN l.PA1_C1 like '%S' THEN cast(left(l.PA1_C1,2) as int)+2 
           ELSE cast(left(l.PA1_C1,2) as int)-8
      END, PA1_C2 =  
      CASE WHEN l.PA1_C2 = '11C' THEN 16
           WHEN l.PA1_C2 = '11S' THEN 17
           WHEN l.PA1_C2 like '%S' THEN cast(left(l.PA1_C2,2) as int)+2 
           ELSE cast(left(l.PA1_C2,2) as int)-8
      END, PA1_C3 =  
      CASE WHEN l.PA1_C3 = '11C' THEN 16
           WHEN l.PA1_C3 = '11S' THEN 17
           WHEN l.PA1_C3 like '%S' THEN cast(left(l.PA1_C3,2) as int)+2 
           ELSE cast(left(l.PA1_C3,2) as int)-8
      END, PA1_C4 =  
      CASE WHEN l.PA1_C4 = '11C' THEN 16
           WHEN l.PA1_C4 = '11S' THEN 17
           WHEN l.PA1_C4 like '%S' THEN cast(left(l.PA1_C4,2) as int)+2 
           ELSE cast(left(l.PA1_C4,2) as int)-8
      END, PA1_C5 =  
      CASE WHEN l.PA1_C5 = '11C' THEN 16
           WHEN l.PA1_C5 = '11S' THEN 17
           WHEN l.PA1_C5 like '%S' THEN cast(left(l.PA1_C5,2) as int)+2 
           ELSE cast(left(l.PA1_C5,2) as int)-8
      END, PA2_C1 =  
      CASE WHEN l.PA2_C1 = '11C' THEN 16
           WHEN l.PA2_C1 = '11S' THEN 17
           WHEN l.PA2_C1 like '%S' THEN cast(left(l.PA2_C1,2) as int)+2 
           ELSE cast(left(l.PA2_C1,2) as int)-8
      END, PA2_C2 =  
      CASE WHEN l.PA2_C2 = '11C' THEN 16
           WHEN l.PA2_C2 = '11S' THEN 17
           WHEN l.PA2_C2 like '%S' THEN cast(left(l.PA2_C2,2) as int)+2 
           ELSE cast(left(l.PA2_C2,2) as int)-8
      END, PA2_C3 =  
      CASE WHEN l.PA2_C3 = '11C' THEN 16
           WHEN l.PA2_C3 = '11S' THEN 17
           WHEN l.PA2_C3 like '%S' THEN cast(left(l.PA2_C3,2) as int)+2 
           ELSE cast(left(l.PA2_C3,2) as int)-8
      END, PA2_C4 =  
      CASE WHEN l.PA2_C4 = '11C' THEN 16
           WHEN l.PA2_C4 = '11S' THEN 17
           WHEN l.PA2_C4 like '%S' THEN cast(left(l.PA2_C4,2) as int)+2 
           ELSE cast(left(l.PA2_C4,2) as int)-8
      END, PA2_C5 =  
      CASE WHEN l.PA2_C5 = '11C' THEN 16
           WHEN l.PA2_C5 = '11S' THEN 17
           WHEN l.PA2_C5 like '%S' THEN cast(left(l.PA2_C5,2) as int)+2 
           ELSE cast(left(l.PA2_C5,2) as int)-8
      END, PB1_C1 =  
      CASE WHEN l.PB1_C1 = '11C' THEN 16
           WHEN l.PB1_C1 = '11S' THEN 17
           WHEN l.PB1_C1 like '%S' THEN cast(left(l.PB1_C1,2) as int)+2 
           ELSE cast(left(l.PB1_C1,2) as int)-8
      END, PB1_C2 =  
      CASE WHEN l.PB1_C2 = '11C' THEN 16
           WHEN l.PB1_C2 = '11S' THEN 17
           WHEN l.PB1_C2 like '%S' THEN cast(left(l.PB1_C2,2) as int)+2 
           ELSE cast(left(l.PB1_C2,2) as int)-8
      END, PB1_C3 =  
      CASE WHEN l.PB1_C3 = '11C' THEN 16
           WHEN l.PB1_C3 = '11S' THEN 17
           WHEN l.PB1_C3 like '%S' THEN cast(left(l.PB1_C3,2) as int)+2 
           ELSE cast(left(l.PB1_C3,2) as int)-8
      END, PB1_C4 =  
      CASE WHEN l.PB1_C4 = '11C' THEN 16
           WHEN l.PB1_C4 = '11S' THEN 17
           WHEN l.PB1_C4 like '%S' THEN cast(left(l.PB1_C4,2) as int)+2 
           ELSE cast(left(l.PB1_C4,2) as int)-8
      END, PB1_C5 =  
      CASE WHEN l.PB1_C5 = '11C' THEN 16
           WHEN l.PB1_C5 = '11S' THEN 17
           WHEN l.PB1_C5 like '%S' THEN cast(left(l.PB1_C5,2) as int)+2 
           ELSE cast(left(l.PB1_C5,2) as int)-8
      END, PB2_C1 =  
      CASE WHEN l.PB2_C1 = '11C' THEN 16
           WHEN l.PB2_C1 = '11S' THEN 17
           WHEN l.PB2_C1 like '%S' THEN cast(left(l.PB2_C1,2) as int)+2 
           ELSE cast(left(l.PB2_C1,2) as int)-8
      END, PB2_C2 =  
      CASE WHEN l.PB2_C2 = '11C' THEN 16
           WHEN l.PB2_C2 = '11S' THEN 17
           WHEN l.PB2_C2 like '%S' THEN cast(left(l.PB2_C2,2) as int)+2 
           ELSE cast(left(l.PB2_C2,2) as int)-8
      END, PB2_C3 =  
      CASE WHEN l.PB2_C3 = '11C' THEN 16
           WHEN l.PB2_C3 = '11S' THEN 17
           WHEN l.PB2_C3 like '%S' THEN cast(left(l.PB2_C3,2) as int)+2 
           ELSE cast(left(l.PB2_C3,2) as int)-8
      END, PB2_C4 =  
      CASE WHEN l.PB2_C4 = '11C' THEN 16
           WHEN l.PB2_C4 = '11S' THEN 17
           WHEN l.PB2_C4 like '%S' THEN cast(left(l.PB2_C4,2) as int)+2 
           ELSE cast(left(l.PB2_C4,2) as int)-8
      END, PB2_C5 =  
      CASE WHEN l.PB2_C5 = '11C' THEN 16
           WHEN l.PB2_C5 = '11S' THEN 17
           WHEN l.PB2_C5 like '%S' THEN cast(left(l.PB2_C5,2) as int)+2 
           ELSE cast(left(l.PB2_C5,2) as int)-8
      END
INTO US3009999_EUCHRE_SCORES4
FROM US3009999_EUCHRE_LOAD l
where l.CALLER_TEAM = l.WINNER_TEAM
ORDER BY l.GAME
GO

select l.row_id as [ID], l.TRUMP as [SUIT_TARGET],
SUIT_SCORE_1 = case 
	when WINNER_TEAM = 'A' then s1.PA1_C1+s1.PA1_C2+s1.PA1_C3+s1.PA1_C4+s1.PA1_C5+s1.PA2_C1+s1.PA2_C2+s1.PA2_C3+s1.PA2_C4+s1.PA2_C5
	when WINNER_TEAM = 'B' then s1.PB1_C1+s1.PB1_C2+s1.PB1_C3+s1.PB1_C4+s1.PB1_C5+s1.PB2_C1+s1.PB2_C2+s1.PB2_C3+s1.PB2_C4+s1.PB2_C5
	else NULL end,
SUIT_SCORE_2 = case 
	when WINNER_TEAM = 'A' then s2.PA1_C1+s2.PA1_C2+s2.PA1_C3+s2.PA1_C4+s2.PA1_C5+s2.PA2_C1+s2.PA2_C2+s2.PA2_C3+s2.PA2_C4+s2.PA2_C5
	when WINNER_TEAM = 'B' then s2.PB1_C1+s2.PB1_C2+s2.PB1_C3+s2.PB1_C4+s2.PB1_C5+s2.PB2_C1+s2.PB2_C2+s2.PB2_C3+s2.PB2_C4+s2.PB2_C5
	else NULL end,
SUIT_SCORE_3 = case 
	when WINNER_TEAM = 'A' then s3.PA1_C1+s3.PA1_C2+s3.PA1_C3+s3.PA1_C4+s3.PA1_C5+s3.PA2_C1+s3.PA2_C2+s3.PA2_C3+s3.PA2_C4+s3.PA2_C5
	when WINNER_TEAM = 'B' then s3.PB1_C1+s3.PB1_C2+s3.PB1_C3+s3.PB1_C4+s3.PB1_C5+s3.PB2_C1+s3.PB2_C2+s3.PB2_C3+s3.PB2_C4+s3.PB2_C5
	else NULL end,
SUIT_SCORE_4 = case 
	when WINNER_TEAM = 'A' then s4.PA1_C1+s4.PA1_C2+s4.PA1_C3+s4.PA1_C4+s4.PA1_C5+s4.PA2_C1+s4.PA2_C2+s4.PA2_C3+s4.PA2_C4+s4.PA2_C5
	when WINNER_TEAM = 'B' then s4.PB1_C1+s4.PB1_C2+s4.PB1_C3+s4.PB1_C4+s4.PB1_C5+s4.PB2_C1+s4.PB2_C2+s4.PB2_C3+s4.PB2_C4+s4.PB2_C5
	else NULL end,
SUIT_RED = case 
	when WINNER_TEAM = 'A' then s1.PA1_C1+s1.PA1_C2+s1.PA1_C3+s1.PA1_C4+s1.PA1_C5+s1.PA2_C1+s1.PA2_C2+s1.PA2_C3+s1.PA2_C4+s1.PA2_C5+s2.PA1_C1+s2.PA1_C2+s2.PA1_C3+s2.PA1_C4+s2.PA1_C5+s2.PA2_C1+s2.PA2_C2+s2.PA2_C3+s2.PA2_C4+s2.PA2_C5
	when WINNER_TEAM = 'B' then s1.PB1_C1+s1.PB1_C2+s1.PB1_C3+s1.PB1_C4+s1.PB1_C5+s1.PB2_C1+s1.PB2_C2+s1.PB2_C3+s1.PB2_C4+s1.PB2_C5+s2.PB1_C1+s2.PB1_C2+s2.PB1_C3+s2.PB1_C4+s2.PB1_C5+s2.PB2_C1+s2.PB2_C2+s2.PB2_C3+s2.PB2_C4+s2.PB2_C5
	else NULL end,
SUIT_BLACK = case 
	when WINNER_TEAM = 'A' then s3.PA1_C1+s3.PA1_C2+s3.PA1_C3+s3.PA1_C4+s3.PA1_C5+s3.PA2_C1+s3.PA2_C2+s3.PA2_C3+s3.PA2_C4+s3.PA2_C5+s4.PA1_C1+s4.PA1_C2+s4.PA1_C3+s4.PA1_C4+s4.PA1_C5+s4.PA2_C1+s4.PA2_C2+s4.PA2_C3+s4.PA2_C4+s4.PA2_C5
	when WINNER_TEAM = 'B' then s3.PB1_C1+s3.PB1_C2+s3.PB1_C3+s3.PB1_C4+s3.PB1_C5+s3.PB2_C1+s3.PB2_C2+s3.PB2_C3+s3.PB2_C4+s3.PB2_C5+s4.PB1_C1+s4.PB1_C2+s4.PB1_C3+s4.PB1_C4+s4.PB1_C5+s4.PB2_C1+s4.PB2_C2+s4.PB2_C3+s4.PB2_C4+s4.PB2_C5
	else NULL end
into US3009999_EUCHRE_TRAIN
from US3009999_EUCHRE_SCORES1 s1,
	 US3009999_EUCHRE_SCORES2 s2,
	 US3009999_EUCHRE_SCORES3 s3,
	 US3009999_EUCHRE_SCORES4 s4,
	 US3009999_EUCHRE_LOAD l
where l.[row_id] = s1.[row_id]
and s1.[row_id] = s2.[row_id]
and s2.[row_id] = s3.[row_id]
and s3.[row_id] = s4.[row_id]
GO

SELECT * FROM US3009999_EUCHRE_LOAD

--select * from US3009999_EUCHRE_SCORES1
--select * from US3009999_EUCHRE_SCORES2
--select * from US3009999_EUCHRE_SCORES3
--select * from US3009999_EUCHRE_SCORES4

select * from US3009999_EUCHRE_TRAIN

--DROP TABLE US3009999_EUCHRE_TRAINING
--DROP TABLE US3009999_EUCHRE_CARDS

--CREATE TABLE US3009999_EUCHRE_TRAINING (
--	[ID]            INT NOT NULL, -- PK
--	[SUIT_TARGET]   INT NOT NULL, -- VALUES:  [1=D, 2=H, 3=C, 4=S]
--	[SUIT_SCORE_1]  INT NOT NULL, -- DIAMONDS (D)
--	[SUIT_SCORE_2]  INT NOT NULL, -- HEARTS   (H)
--	[SUIT_SCORE_3]  INT NOT NULL, -- CLUBS    (C)
--	[SUIT_SCORE_4]  INT NOT NULL  -- SPADES   (S)
--)
--GO

--ALTER TABLE US3009999_EUCHRE_TRAINING
--ADD CONSTRAINT [PK_US3009999_EUCHRE_TRAINING] PRIMARY KEY CLUSTERED 
--([ID] ASC) WITH (PAD_INDEX = OFF, 
--				 STATISTICS_NORECOMPUTE = OFF, 
--				 SORT_IN_TEMPDB = OFF, 
--				 IGNORE_DUP_KEY = OFF, 
--				 ONLINE = OFF, 
--				 ALLOW_ROW_LOCKS = ON, 
--				 ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
--GO

--CREATE TABLE US3009999_EUCHRE_CARDS (
--	[ID]      NVARCHAR(64) NOT NULL,
--	[SUIT]    INT, 
--	[COLOR]   INT, 
--	[RANK]    INT
--)
--GO

--ALTER TABLE US3009999_EUCHRE_CARDS
--ADD CONSTRAINT [PK_US3009999_EUCHRE_CARDS] PRIMARY KEY CLUSTERED 
--([ID] ASC) WITH (PAD_INDEX = OFF, 
--				 STATISTICS_NORECOMPUTE = OFF, 
--				 SORT_IN_TEMPDB = OFF, 
--				 IGNORE_DUP_KEY = OFF, 
--				 ONLINE = OFF, 
--				 ALLOW_ROW_LOCKS = ON, 
--				 ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
--GO

--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('9C',3,2,1)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('10C',3,2,2)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('11C',3,2,3)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('12C',3,2,4)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('13C',3,2,5)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('14C',3,2,6)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('9D',1,1,1)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('10D',1,1,2)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('11D',1,1,3)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('12D',1,1,4)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('13D',1,1,5)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('14D',1,1,6)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('9H',2,1,1)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('10H',2,1,2)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('11H',2,1,3)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('12H',2,1,4)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('13H',2,1,5)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('14H',2,1,6)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('9S',4,2,1)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('10S',4,2,2)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('11S',4,2,3)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('12S',4,2,4)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('13S',4,2,5)
--insert into US3009999_EUCHRE_CARDS ([ID], [SUIT], [COLOR], [RANK]) values ('14S',4,2,6)
--GO
