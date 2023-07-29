SELECT J.FLAVOR
FROM JULY J
JOIN FIRST_HALF F ON J.flavor = F.flavor
GROUP BY J.flavor
ORDER BY SUM(J.total_order) + F.total_order DESC
LIMIT 3;