SET @RATE = 1;

SELECT
    H.HISTORY_ID
    , ROUND( ((DATEDIFF(H.END_DATE,H.START_DATE)+1) * R.DAILY_FEE ) * @RATE := (
    SELECT
    CASE
        WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 < 7
            THEN 1
        WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 < 30 AND DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 7
            THEN 0.95
        WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 < 90 AND DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 30
            THEN 0.92
        WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 90
            THEN 0.85   
        END
    ), 0) FEE
FROM CAR_RENTAL_COMPANY_CAR R
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
ON R.CAR_ID=H.CAR_ID
WHERE 1=1
AND R.CAR_TYPE = '트럭'
ORDER BY FEE DESC, H.HISTORY_ID DESC