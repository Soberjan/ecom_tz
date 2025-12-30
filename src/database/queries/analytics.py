more_than_3_twos_query = """
SELECT full_name, count_twos
FROM (
    SELECT full_name, COUNT(*) count_twos
    FROM students
    WHERE grade = 2
    GROUP BY full_name
)
WHERE count_twos > 3
"""

less_than_5_twos_query = """
SELECT full_name, count_twos
FROM (
    SELECT full_name, COUNT(*) count_twos
    FROM students
    WHERE grade = 2
    GROUP BY full_name
)
WHERE count_twos < 5
"""
