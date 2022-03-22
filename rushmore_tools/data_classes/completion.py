from datetime import datetime
from typing import Any, List, Optional

from pydantic import Field

from ._base import RushmoreBaseModel


class _Location(RushmoreBaseModel):
    FieldBasinArea: str
    Country: str
    Region: str
    SubRegion: str
    BlockNumber: str


class _Rig(RushmoreBaseModel):
    Contractor: str
    Name: str


class _PullOldCompletion(RushmoreBaseModel):
    DaysPer1000m: Optional[float]
    TotalDays: Optional[float] = Field(alias="TimeIncludingNPTWoW")
    NPT: Optional[float] = Field(alias="NPTExcludingWoW")
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveDays")
    ProductiveDaysPer1000: Optional[float]


class _RemedialWork(RushmoreBaseModel):
    TotalDays: Optional[float] = Field(alias="TimeIncludingNPTWoW")
    NPT: Optional[float] = Field(alias="NPTExcludingWoW")
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _BorePrep(RushmoreBaseModel):
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000MTDm: Optional[float]
    ProductiveDaysPer1000: Optional[float]


class _FinalCasing(RushmoreBaseModel):
    StringType: str
    NumberOfProductionLiners: Optional[int]
    LinerIsolationType: str
    Description: str
    LinerCement: Optional[str]
    LinerLength: Optional[float]
    LinerSize: str
    LinerWeight: str
    LinerMaterial: str
    RigType: str
    EquipmentUsed: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000m: Optional[float]
    ProductiveDaysPer1000: Optional[float]
    BorePrep: _BorePrep


class _CleanUp:
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000SandCtrlm: Optional[float]


class _SandControl(RushmoreBaseModel):
    Description: str
    Length: Optional[float]
    Zones: Optional[int]
    SandScreenSize: str
    SandScreenWeight: Optional[str]
    SandScreenMaterial: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000m: Optional[float]
    ProductiveDaysPer1000: Optional[float]
    BorePrep: _BorePrep
    CleanUp: _CleanUp


class _Completion(RushmoreBaseModel):
    RigType: str
    Equipment: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000m: Optional[float]
    ProductiveDaysPer1000: Optional[float]


class _TubingHanger(RushmoreBaseModel):
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _Perforation(RushmoreBaseModel):
    RigType: str
    Equipment: str
    ConveyanceMethod: str
    TotalDays: Optional[float]
    CumulativePerforatedInterval: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    DaysPer1000m: Optional[float]
    ProductiveDaysPer1000: Optional[float]


class _Stimulation(RushmoreBaseModel):
    Type: str
    RigType: str
    Equipment: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _MoveOff(RushmoreBaseModel):
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _XmasTree(RushmoreBaseModel):
    RigType: str
    Equipment: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _OtherOperations(RushmoreBaseModel):
    RigType: str
    Equipment: str
    TotalDays: Optional[float]
    NPT: Optional[float] = Field(alias="NPTDaysExcludingWoW")
    WOW: Optional[float] = Field(alias="WoWDays")
    PT: Optional[float] = Field(alias="ProductiveDays")
    Types: str
    TimingsBreakdown: str


class _Preparation(RushmoreBaseModel):
    Activities: str
    ActivitiesTimes: str
    TotalDays: Optional[float] = Field(alias="TotalDaysIncludingNPTWoW")
    NPT: Optional[float] = Field(alias="NPTExcludingWoW")
    WOW: Optional[float] = Field(alias="WoW")
    PT: Optional[float] = Field(alias="ProductiveDays")


class _Workover(RushmoreBaseModel):
    Reasons: str
    FurtherDetails: str
    Preparation: _Preparation


class _Costs(RushmoreBaseModel):
    TotalIncludingOverheadsTangibleUSD: Optional[float]
    TotalExcludingOverheadsIncludingTangibleUSD: Optional[float]
    TangibleUSD: Optional[float]
    TotalExcludingTangibleUSD: Optional[float]
    TotalExcludingTangiblePerTotalDay: Optional[float]
    TotalExcludingTangiblePerMTD: Optional[float]
    TangiblePerMTD: Optional[float]
    PreliminaryOrFinal: str
    LocalCurrency: str
    ExchangeRate: float


class _Dates(RushmoreBaseModel):
    PreviousWorkover: Optional[datetime]
    UnTightFrom: Optional[datetime]
    Start: Optional[datetime]
    End: datetime
    Published: datetime
    LastUpdated: datetime


class RushmoreCompletionWell(RushmoreBaseModel):
    """Class for converting RAW output from Rushmore Completion performance Review
    with cleaners and filters.

    The goal with this class is to predefined a set of rules for handling the different
    datapoints available in the Rushmore API.
    """

    # Own attributes
    Year: int
    WellId: int
    Quarter: int
    OperatorId: int
    OperatorStatusRevYrId: int
    GroupName: str
    OperatorName: str
    BusinessUnit: Optional[str]
    WellName: str
    InHouseName: str
    SchematicUrl: str
    TimePhaseChartUrl: str
    Platform: str
    MTD: float
    TVD: Optional[float]
    PlatformSubseaLand: str
    WaterDepth: Optional[float]
    Service: str
    Multilateral: str
    NumberOfLaterals: Optional[int]
    MultilateralJunctionType: str
    CompletionType: str
    NumberOfCompletionStrings: str
    CompletionLength: Optional[float]
    NumberOfCompletionTrips: Optional[int]
    MaximumAngle: Optional[int]
    TubingSize: str
    TubingWeight: str
    TubingMaterial: str
    XmasTreeType: str
    ArtificialLift: str
    IsWorkover: Optional[bool]
    IsSuspendedAfterDPR: Optional[bool]
    IsSuspendedBeforePerforation: Optional[bool]
    IsOtherSuspensions: Optional[bool]
    SuspendReEnterDays: Optional[float]
    UniqueWellID: str
    PlayType: Optional[str]
    DownHoleMonitoring: str
    IsHighPressure: str
    IsHighTemperature: str
    NumberOfIsolationZonesInIntelligentCompletion: Optional[int]
    MainCausesOfNPT: str
    FurtherDetails: str
    WellDataType: str
    IsIntelligentCompletion: Optional[bool]
    MaximumAngleThroughReservoir: Optional[int]
    LengthOfOldTubingPulled: Optional[float]
    NumberOfPermanentPackersPulled: Optional[int]
    NumberOfRetrievablePackersPulled: Optional[int]
    DownHoleActuation: Optional[int]
    SpecimenWellName: str
    CasingDrillingIndicator: Optional[str]
    DesignCO2Percentage: Optional[str]
    FluidInHolePriorCleanup: Optional[str]
    DesignH2S: Optional[str]
    NumberOfIsolationZonesCapableOfSelectiveProduction: Optional[int]
    TotalCompletionLength: Optional[float]
    Days: Optional[float]
    NPTDays: Optional[float]
    WoWDays: Optional[float]
    ProductiveDays: Optional[float]
    ProductiveDaysPer1000: Optional[float]
    DaysPer1000MTDm: Optional[float]
    DaysExcludingExternalNPT: Optional[float]
    NPTDaysExcludingExternalNPT: Optional[float]
    Comments: str
    # Subclasses
    Location: _Location
    Rig: _Rig
    PullOldCompletion: _PullOldCompletion
    RemedialWork: _RemedialWork
    FinalCasing: _FinalCasing
    SandControl: _SandControl
    Completion: _Completion
    TubingHanger: _TubingHanger
    Perforation: _Perforation
    Stimulation: _Stimulation
    MoveOff: _MoveOff
    XmasTree: _XmasTree
    OtherOperations: _OtherOperations
    Workover: _Workover
    Costs: _Costs
    Dates: _Dates


class RushmoreCompletionWells(RushmoreBaseModel):
    Wells: List[RushmoreCompletionWell]
