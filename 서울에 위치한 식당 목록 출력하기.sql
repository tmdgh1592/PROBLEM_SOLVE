SELECT REST.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS REST
INNER JOIN REST_REVIEW AS REVIEW ON REST.REST_ID = REVIEW.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY REST.REST_ID
ORDER BY AVG(REVIEW_SCORE) DESC, FAVORITES DESC