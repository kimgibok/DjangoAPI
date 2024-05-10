import json

# 딕셔너리 형태로 변환
def serialize_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "in_stock": product.in_stock
    }