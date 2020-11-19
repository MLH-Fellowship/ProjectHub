
def parse_project_query(query):
    if query is None:
        return query

    return {"id": query[0],
            "name": query[1],
            "description": query[2],
            "source_link": query[3],
            "demo_link": query[4],
            "images": query[5],
            "tags": query[6],
            "authors": query[7]
            }


def parse_user_query(query):
    if query is None:
        return query

    pods = query[2]
    skills = query[5]
    interests = query[6]

    return {"username": query[0],
            "name": query[1],
            "pods": pods.split(','),
            "timezone": query[3],
            "bio": query[4],
            "skills": skills.split(','),
            "interests": interests.split(',')
            }
