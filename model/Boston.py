from dataclasses import dataclass


@dataclass
class BostonDto:
    CrimeRate: float = 0.0
    ZonedLand: float = 0.0
    NonRetailAcres: float = 0.0
    CharlesRiver: bool = 0
    Nox: float = 0.0
    NoOfRooms: float = 0.0
    BuildingAge: float = 0.0
    DistanceToEmpCenters: float = 0.0
    Accessibility: float = 0.0
    Tax: float = 0.0
    TeacherRatio: float = 0.0
    BlacksProposition: float = 0.0
    LowerStatus: float = 0.0
