import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import Field, ValidationError

from ._base import RushmoreBaseModel

logger = logging.getLogger(__name__)


class _Location(RushmoreBaseModel):
    Country: str
    Region: str
    SubRegion: str
    OffshoreLand: str
    FieldBasinArea: Optional[str]
    BlockNumber: Optional[str]
    Latitude: str
    Longitude: str
    DecimalLatitude: Optional[float]
    DecimalLongitude: Optional[float]


class _Casings(RushmoreBaseModel):
    PreExistingCasings: Optional[str]
    NewCasings: Optional[str]
    TotalCasingCount: Optional[int]
    NewCasingCount: Optional[int]
    PreExistingCasingSizes: List[Optional[str]] = Field(
        alias="PreExisitingCasingSizes"
    )  # Likely typo in column def
    NewCasingSizes: List[Optional[str]]


class _Costs(RushmoreBaseModel):
    PerDryHoleDayUSD: float
    DryHoleCostUSD: float
    DryHolePerMetreUSD: float
    TotalWellUSD: Optional[float]
    TotalPerMetreUSD: Optional[float]
    TotalPerTotalDayUSD: Optional[float]
    LocalCurrency: str
    ExchangeRate: float
    Complete: Optional[str]


class _TimeDepthRow(RushmoreBaseModel):
    Day: int
    Depth: float
    HoleSize: float


class _TimeDepth(RushmoreBaseModel):
    TimeDepth: List[_TimeDepthRow]


class _Dates(RushmoreBaseModel):
    Spud: Optional[datetime]
    DryHoleEnd: datetime
    Published: datetime
    LastUpdated: datetime
    EndOfWellOperations: Optional[datetime]
    UnTightFrom: Optional[datetime]


class RushmoreDrillWell(RushmoreBaseModel):
    """Class for converting RAW output from Rushmore Drilling Performance Review
    with cleaners and filters.

    The goal with this class is to predefined a set of rules for handling the different
    datapoints available in the Rushmore API.
    """

    # Own attributes

    WellId: int
    OperatorId: int
    OperatorStatusRevYrId: int
    Quarter: int
    Year: int
    GroupName: str
    OperatorName: str
    BusinessUnit: Optional[str]
    PreviousOperatorName: Optional[str]
    WellName: str
    InHouseName: str
    TimeDepthChartUrl: Optional[str]
    Platform: Optional[str]
    OwnerDrilled: Optional[str]
    WellType: str
    IsHighPressure: Optional[bool]
    IsHighTemperature: Optional[bool]
    HoleType: Optional[str]
    LocatorWellOrShallowGasPilotHole: Optional[str]
    IsMultilateral: Optional[bool]
    NumberOfLaterals: Optional[int]
    IsReSpud: Optional[bool]
    OriginalName: Optional[str]
    RigType: str
    DrillMethod: Optional[str]
    WaterDepth: Optional[float]
    SpudDepth: float
    MTD: float
    DrilledInterval: float
    TVD: Optional[float]
    MaximumAngle: Optional[int]
    HorizontalSectionLength: Optional[int]
    ComplexRatio: Optional[float]
    FinalBitSize: Optional[float]
    PressureBalance: Optional[str]
    DrillingFluid: Optional[str]
    TDMudWeight: Optional[float]
    MaximumMudWeight: Optional[float]
    CuttingsDisposalMethod: Optional[str]
    CoringDays: Optional[float]
    CoringInterval: Optional[float]
    LogDaysNotTD: Optional[float]
    LogDaysTD: Optional[float]
    PilotHoleEnlargementDays: Optional[float]
    PilotHoleEnlargementInterval: Optional[float]
    AgeOfDeepestReservoir: Optional[str]
    SlotRecoveryPreSpudDays: Optional[float]
    BatchCampaignDrilled: Optional[str]
    NumberOfWellSuspensions: Optional[int]
    SuspensionReEntryDays: Optional[float]
    TotalWellSiteDays: Optional[float]
    WellStatus: Optional[str]
    PAOrSUDays: Optional[float]
    TotalWoWDuringDryHoleDays: Optional[float]
    TotalNPTDuringDryHoleDays: Optional[float]
    FurtherDetails: str
    Comments: str
    RigMooringSystem: Optional[str]
    GOMAPINumber: Optional[str]
    Salt: Optional[str]
    TVDSaltStart: Optional[float]
    TVDSaltEnd: Optional[float]
    RigName: Optional[str]
    MultilateralJunctionType: Optional[str]
    WellDataType: str
    NumberOfContingencyGeologicalSidetracks: Optional[int]
    UnusedLengthContingencyGeologicaSidetracks: Optional[int]
    UnusedLengthLocatorWell: Optional[int]
    GeologicalSidetrackWhipstockDays: Optional[float]
    ExtendedReach: Optional[str]
    DrillFloorElevation: Optional[float]
    IsConductorInstalledByDrillingRig: Optional[bool]
    RigContractorNPT: Optional[float]
    ServiceCompanyNPT: Optional[float]
    OperatorProblemsNPT: Optional[float]
    ExternalProblemsNPT: Optional[float]
    DownholeProblemsNPT: Optional[float]
    CompletionDays: Optional[float]
    SpecimenWellName: Optional[str]
    RigContractor: Optional[str]
    RigMoveDays: Optional[float]
    IsRigMoveWithinField: Optional[bool]
    CasingDrilling: Optional[str]
    NumberOfMechanicalSidetracks: Optional[int]
    IsSplitConductor: Optional[bool]
    ExpandableCasingCount: Optional[int]
    DryHoleDaysExcludingCoringLogging: Optional[float]
    MetresPerDryHoleDayExcludingCoringLogging: Optional[float]
    DryHoleDaysExcludingCoringLoggingPer1000m: Optional[float]
    WoWPer1000m: Optional[float]
    NPTPer1000m: Optional[float]
    ProductiveDaysPer1000m: Optional[float]
    WoWPercentageOfDryHoleDays: Optional[float]
    NPTPercentageOfDryHoleDays: Optional[float]
    MetresPerDryHoleDay: float
    DryHoleDaysPer1000m: float
    PlayType: str
    IsDualActivityRig: Optional[bool]
    LogDaysTotal: Optional[float]
    UniqueWellID: str
    ProductiveDays: Optional[float]
    DaysSpentMooringDeMooring: Optional[float]
    WoWDuringMooringDeMooring: Optional[float]
    BurialDepth: Optional[float]
    SlotRecoveryIncludesAbandonmentTime: Optional[str]  # TODO: Check if discontinued
    IsComplexWellPath: Optional[bool]
    DeMoorDays: Optional[float]
    DryHoleDaysExcludingCoring: float
    DryHoleDaysExcludingCoringPer1000m: float
    IsFEWD: Optional[bool]
    MajorNPTEvents: Optional[str]
    MetresPerDryHoleDayExcludingCoring: float
    MoorDays: Optional[float]
    NewTechniques: Optional[str]
    IsSlotRecoveryPreSpudOffline: Optional[bool]  # TODO: Check if discontinued
    OtherOperationsDays: Optional[float]
    RDI2_1: Optional[int]
    REDD2_0: Optional[float]
    RDI3_1: Optional[float]
    REDD3_1: Optional[float]
    WoWBeforeDeMoorDays: Optional[float]  # TODO: Check if discontinued
    WoWDeMoorDays: Optional[float]
    WoWMoorDays: Optional[float]
    DryHoleDays: float
    Location: _Location
    Casings: _Casings
    Costs: _Costs
    TimeDepth: _TimeDepth
    Dates: _Dates


class RushmoreDrillWells(RushmoreBaseModel):
    Wells: Optional[List[RushmoreDrillWell]] = None

    def __init__(self, wells: List[Dict[str, Any]], **data: Any):
        super().__init__(**data)
        invalid = 0
        if self.Wells is None:
            self.Wells = []
        for well in wells:
            try:
                self.Wells.append(RushmoreDrillWell(**well))
            except ValidationError:
                invalid += 1
        logger.debug(
            f"Initialized {len(self.Wells):,} wells, found {invalid:,} invalid configurations."
        )
