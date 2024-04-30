SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS P, ECOLI_DATA AS C
WHERE C.PARENT_ID = P.ID
AND (C.GENOTYPE & P.GENOTYPE = P.GENOTYPE)