
-- Billing Table 
SELECT 
c.FNAME 
,c.LNAME
,sum(
    (CASE 
        WHEN cast(us.riding_time AS INT) <= 10 THEN .5
        WHEN cast(us.riding_time AS INT) > 10 THEN .35 END )

) AS COSTS


INTO usecase.billing
FROM USECASE.CustomerTable as c 
JOIN USECASE.Usagetable as us on 1=1
    and us.user_id = c.user_id 
group by c.fname,c.Lname

-- Top_Riders
SELECT TOP 10 
    CONCAT (CUST.FNAME,' ',CUST.LNAME) AS NAME
    ,COUNT(US.USER_ID) AS RIDES
INTO usecase.Top_Riders
FROM usecase.CUSTOMERTable AS CUST 
JOIN usecase.USAGETable AS US ON 1=1 
    AND CUST.USER_ID = US.USER_ID
GROUP BY CONCAT  (CUST.FNAME,' ',CUST.LNAME)
ORDER BY COUNT (US.USER_ID) DESC

-- Sum_by_zip
SELECT 
COUNT(*) AS NUMBER 
,ZIP 
INTO sum_by_zip
FROM usecase.CustomerTable
GROUP BY ZIP 
ORDER BY ZIP ASC