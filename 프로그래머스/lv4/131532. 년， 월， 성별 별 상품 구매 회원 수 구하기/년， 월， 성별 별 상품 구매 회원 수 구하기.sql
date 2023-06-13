-- 코드를 입력하세요
SELECT DATE_FORMAT(S.SALES_DATE,'%Y') AS YEAR, DATE_FORMAT(S.SALES_DATE,'%m') AS MONTH, 
GENDER, COUNT(DISTINCT I.USER_ID) AS USERS
FROM USER_INFO I
JOIN ONLINE_SALE S
ON I.USER_ID = S.USER_ID
WHERE I.GENDER IS NOT NULL
GROUP BY 1,2,3
ORDER BY 1,2,3;