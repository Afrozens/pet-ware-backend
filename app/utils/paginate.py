import math

def converted_paginate_data(page: int, limit: int, query_search):
    offset_page = (page - 1) * limit
    total_record = query_search.count()
    total_page = math.ceil(total_record / limit)
    data_current = query_search.offset(offset_page).limit(limit).all()
    
    data = {
        "data": data_current,
        "page_number": page,
        "page_size": limit,
        "total_pages": total_page,
        "total_record": total_record
    }
    return data