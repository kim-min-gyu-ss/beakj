SELECT CONCAT("/home/grep/src/",F.board_id, "/",F.file_id,F.file_name,F.file_ext)
FROM USED_GOODS_FILE F
JOIN USED_GOODS_BOARD B ON F.board_id = B.board_id
WHERE B.views = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY F.file_id DESC;