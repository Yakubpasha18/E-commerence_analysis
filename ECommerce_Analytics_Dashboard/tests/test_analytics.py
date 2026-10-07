import pandas as pd
from src.analytics import kpis, category_performance

def sample():
    return pd.DataFrame({
        "order_id":["O1","O2","O3"],
        "revenue":[100,200,50],
        "profit":[20,40,5],
        "quantity":[1,2,1],
        "category":["A","A","B"]
    })

def test_kpis():
    m = kpis(sample())
    assert m["revenue"] == 350
    assert m["profit"] == 65
    assert m["orders"] == 3
    assert round(m["aov"], 2) == 116.67

def test_category_performance():
    result = category_performance(sample())
    assert set(result["category"]) == {"A","B"}
    assert result.iloc[0]["category"] == "A"
