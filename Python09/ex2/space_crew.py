from enum import Enum
import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime.datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> SpaceMission:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        if not any(member.rank in [Rank.captain, Rank.commander]
                   for member in self.crew):
            raise ValueError('Mission must have at least one\
                              Commander or Captain')
        if self.duration_days > 365:
            experience: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experience += 1
            if (experience / len(self.crew)) < 0.5:
                raise ValueError('Long missions need 50% experienced crew')
        if not all(member.is_active for member in self.crew):
            raise ValueError('All crew members must be active')
        return self


def main() -> None:
    print('Space Mission Crew Validation')
    print('=' * 38)

    sarah = CrewMember(
        member_id='001',
        rank=Rank.commander,
        name='Sarah Connor',
        age=48,
        specialization='Mission Commander',
        years_experience=15,
        is_active=True
    )

    john = CrewMember(
        member_id='010',
        rank=Rank.lieutenant,
        name='John Smith',
        age=35,
        specialization='Navigation',
        years_experience=10,
        is_active=True
    )

    alice = CrewMember(
        member_id='100',
        rank=Rank.officer,
        name='Alice Johnson',
        age=29,
        specialization='Engineering',
        years_experience=6,
        is_active=True
    )

    data_mission = SpaceMission(
        mission_id='M2024_MARS',
        mission_name='Mars Colony Establishment',
        destination='Mars',
        launch_date=datetime.datetime.now(),
        duration_days=900,
        crew=[sarah, john, alice],
        budget_millions=2500.0
    )

    print('Valid mission created:')
    print(f'Mission: {data_mission.mission_name}')
    print(f'ID: {data_mission.mission_id}')
    print(f'Destination: {data_mission.destination}')
    print(f'Duration: {data_mission.duration_days} days')
    print(f'Budget: ${data_mission.budget_millions}M')
    print(f'Crew size: {len(data_mission.crew)}')
    print('Crew members:')
    for members in data_mission.crew:
        print(f'- {members.name} ({members.rank.value}) -'
              f'{members.specialization}')
    print()
    print('=' * 38)

    no_actv_alice = alice.model_copy(update={'is_active': False})

    print('Expected validation error')
    try:
        SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date=datetime.datetime.now(),
            duration_days=900,
            crew=[no_actv_alice, john, sarah],
            budget_millions=2500.0
        )
    except ValidationError as e:
        for err in e.errors():
            print(err['msg'].removeprefix('Value error, '))


if __name__ == '__main__':
    main()
