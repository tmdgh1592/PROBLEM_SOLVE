SELECT a.DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT AS a
JOIN HR_EMPLOYEES AS b
ON a.DEPT_ID = b.DEPT_ID
GROUP BY DEPT_ID
ORDER BY AVG(SAL) DESC