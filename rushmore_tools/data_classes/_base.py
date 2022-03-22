from typing import Any, Dict, List, Optional, TypedDict

from pydantic import BaseModel


class RushmoreResponse(TypedDict):
    TotalWells: Optional[int]
    TotalPages: Optional[int]
    PageInfo: Optional[Dict[str, Any]]
    Data: Optional[List[Dict[str, Any]]]


class RushmoreBaseModel(BaseModel):
    class Config:
        extra = "ignore"
        validate_assignment = True
