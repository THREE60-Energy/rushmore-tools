from datetime import datetime
from typing import Any, List, Optional

from pydantic import Field

from ._base import RushmoreBaseModel


class _Location(RushmoreBaseModel):
    Region: str
    Country: str


class _PreparatoryWork(RushmoreBaseModel):
    PreWorkscopeOperations: Optional[str]
    RigType: Optional[str]
    Days: Optional[float]
    NPT: Optional[float]
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveTime")
    Cost: Optional[float]


class _CostsVariant(RushmoreBaseModel):
    PerDay: Optional[float]
    Total: Optional[float]


class _Subdivision(RushmoreBaseModel):
    Days: Optional[float]
    NPT: Optional[float]
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveTime")
    Costs: _CostsVariant


class _Costs(RushmoreBaseModel):
    ExchangeRate: float
    Currency: str
    FinalCosts: str
    CompletenessOfCosts: str


class _Deepwater(RushmoreBaseModel):
    DeviationFromGuidlines: Optional[bool]  # Likely typo in column def
    Phase3OperationsIntended: Optional[bool]


class _Dates(RushmoreBaseModel):
    WorkscopeCompleted: str
    Published: datetime
    LastUpdated: datetime


class _DES(RushmoreBaseModel):
    WorkFacilityUsed: Optional[str]
    Days: Optional[float]
    NPT: Optional[float]
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveTime")


class _NonDES(RushmoreBaseModel):
    Equipment: Optional[str] = Field(alias="HeavyRotatingEquipmentUsed")
    Days: Optional[float]
    NPT: Optional[float]
    WOW: Optional[float] = Field(alias="Wow")
    PT: Optional[float] = Field(alias="ProductiveTime")


class _Phase1(RushmoreBaseModel):
    # Own
    AngleAtDeepestCementPlug: Optional[int]
    IsCombinationBarrierSet: Optional[bool]
    IsDiverInWater: Optional[bool]
    IsDiverSupport: Optional[bool]
    MaximumAngleAboveDeepestCementPlug: Optional[float]
    DepthOfDeepestCementPlug: Optional[float]
    IsThroughTubingAbandonment: Optional[bool]
    NumPermanentCementPlugsSet: Optional[int]
    NumCasingStringsCutAndRecovered: Optional[int]
    NumCasingSectionsMilled: Optional[int]
    NumPlugsOverLinerTopsCasingStubs: Optional[int]
    NumPackersRemovedByMilling: Optional[int]
    IsComplete: Optional[bool]
    ComplexityCategory: Optional[str]
    IsWorkFacilityBroughtInSpecifically: Optional[bool]
    NumCementPlugs: Optional[int]
    IsDeepestCementPlugAngleGreater60: Optional[bool]
    AnnulusRemediationTechniques: Optional[str]
    BreakdownOfPreparatoryWorkTimePerWorkFacility: Optional[str]
    PlugBarrierTypeSet: Optional[str]
    # Shared
    DES: _DES
    NonDES: _NonDES
    PreparatoryWork: _PreparatoryWork
    ExcludingPrep: _Subdivision
    IncludingPrep: _Subdivision


class _Phase2(RushmoreBaseModel):
    # Own
    IsWorkFacilityBroughtInSpecifically: Optional[bool]
    NumCementPlugs: Optional[int]
    IsDeepestCementPlugAngleGreater60: Optional[bool]
    AnnulusRemediationTechniques: Optional[str]
    BreakdownOfPreparatoryWorkTimePerWorkFacility: Optional[str]
    PlugBarrierTypeSet: Optional[str]
    DepthOfDeepestIntermediateCementPlug: Optional[float]
    IsThroughTubingAbandonment: Optional[bool]
    NumPermanentCementPlugsSet: Optional[int]
    NumCasingStringsCutAndRecovered: Optional[int]
    NumCasingSectionsMilled: Optional[int]
    NumPlugsOverLinerTopsCasingStubs: Optional[int]
    NumPackersRemovedByMilling: Optional[int]
    IsComplete: Optional[bool]
    ComplexityCategory: str
    AngleAtDeepestCementPlug: Optional[float]
    IsCombinationBarrierSet: Optional[bool]
    IsDiverInWater: Optional[bool]
    IsDiverSupport: Optional[bool]
    MaximumAngleAboveDeepestCementPlug: Optional[float]
    # Shared
    DES: _DES
    NonDES: _NonDES
    PreparatoryWork: _PreparatoryWork
    ExcludingPrep: _Subdivision
    IncludingPrep: _Subdivision


class _Phase3(RushmoreBaseModel):
    # Own
    IsComplete: Optional[bool]
    ComplexityCategory: str
    IsWorkFacilityBroughtInSpecifically: Optional[bool]
    BreakdownOfPreparatoryWorkTimePerWorkFacility: Optional[str]
    IsDiverInWater: Optional[bool]
    IsDiverSupport: Optional[bool]
    RemovalOfSurfaceTubularsIncluded: str
    # Shared
    DES: _DES
    NonDES: _NonDES
    PreparatoryWork: _PreparatoryWork
    ExcludingPrep: _Subdivision
    IncludingPrep: _Subdivision


class RushmoreAbandonment(RushmoreBaseModel):
    """Class for converting RAW output from Rushmore APR with cleaners and filters.

    The goal with this class is to predefined a set of rules for handling the different
    datapoints available in the Rushmore API.
    """

    # Own attributes
    WellId: int
    OperatorId: int
    OperatorStatusRevYrId: int
    Year: int
    Quarter: int
    GroupName: str
    OperatorName: str
    BusinessUnit: Optional[str]
    PreviousOperatorName: Optional[str]
    WellName: str
    InHouseName: str
    WellCategory: str
    IsReAbandonment: bool
    NumZonesToBeSeparated: Optional[int]
    FluidsInPermeableZone: str
    IsH2SPresent: Optional[bool]
    IsCO2Present: Optional[bool]
    LowRadioActiveScale: Optional[str]
    HPHTWell: str
    CompletionType: str
    ArtificialLift: str
    TypesOfDeepLines: str
    IsMultilateral: Optional[bool]
    TubularAccess: str
    AnnuliWithIntegrityIssues: Optional[int]
    QualityOfWellRecords: Optional[str]
    NumWellsInCampaign: str
    UniqueWellID: Optional[str]
    CampaignName: str
    Comments: str
    IsSpoolTypeWellhead: Optional[bool]
    WaterDepth: Optional[float]
    CausesOfMajorNPT: str
    DescriptionOfWorkscope: str
    AbandonmentComplexity: str
    IsRequiredDiverSupportInWater: bool
    TreeType: Optional[str]
    Days: float = Field(alias="Time")
    NPT: float
    WOW: float = Field(alias="WoW")
    PT: float = Field(alias="ProductiveTime")
    HasPhase1Data: bool
    HasPhase2Data: bool
    HasPhase3Data: bool
    # Subclasses
    Location: _Location
    PreparatoryWork: _PreparatoryWork
    Phase1: _Phase1
    Phase2: _Phase2
    Phase3: _Phase3
    IncludingPrep: _Subdivision
    ExcludingPrep: _Subdivision
    Costs: _Costs
    Deepwater: _Deepwater
    Dates: _Dates

    def __init__(self, **data: Any):
        super().__init__(**data)


class RushmoreAbandonments(RushmoreBaseModel):
    Abandonments: List[RushmoreAbandonment]
