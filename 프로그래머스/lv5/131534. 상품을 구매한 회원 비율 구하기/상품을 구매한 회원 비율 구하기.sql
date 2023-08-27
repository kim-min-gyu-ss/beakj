SELECT YEAR(sales_date),
    MONTH(sales_date), 
    count(DISTINCT O.USER_ID), 
    ROUND(count(DISTINCT O.USER_ID)/(SELECT COUNT(USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021),1)
FROM ONLINE_SALE O
INNER JOIN USER_INFO U ON U.USER_ID = O.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY 1,2
ORDER BY 1,2