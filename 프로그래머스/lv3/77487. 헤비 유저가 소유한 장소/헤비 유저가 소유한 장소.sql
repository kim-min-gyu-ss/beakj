-- 코드를 입력하세요
SELECT I.ID, NAME, I.HOST_ID
FROM PLACES I
JOIN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(*) > 1) D
ON I.HOST_ID = D.HOST_ID
ORDER BY I.ID;