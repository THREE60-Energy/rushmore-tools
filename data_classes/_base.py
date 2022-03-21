from pydantic import BaseModel


class _RushmoreBaseModel(BaseModel):
    class Config:
        extra = "ignore"
        validate_assignment = True
