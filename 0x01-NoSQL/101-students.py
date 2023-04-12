#!/usr/bin/env python3
""" To return all student sorted by average score
"""


def top_students(mongo_collection):
    """now returns all students that are sorted by average score
    """
    student_tops = mongo_collection.aggregate([
            {
                "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
        ])
    return student_tops
