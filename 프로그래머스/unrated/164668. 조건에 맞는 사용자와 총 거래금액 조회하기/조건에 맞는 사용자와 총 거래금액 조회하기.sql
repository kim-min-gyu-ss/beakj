-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U
ON U.USER_ID = B.WRITER_ID
WHERE B.STATUS = 'done'
GROUP BY U.USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY 3;