"""
This module contains the class CovidModel.
"""


class CovidModel:
    """
    This class acts as a data class.
    It stores all the relevant data in form of properties.
    """

    def __init__(
        self, state_name, confirmed, active,
        recovered, deceased, tested, vaccine_doses
    ):
        self.state_name = state_name
        self.confirmed = confirmed
        self.active = active
        self.recovered = recovered
        self.deceased = deceased
        self.tested = tested
        self.vaccine_doses = vaccine_doses

    def __repr__(self):
        return f"State Name = {self.state_name}, Confirmed = {self.confirmed},\
        Active = {self.active}, Recovered = {self.recovered},\
        Deceased = {self.deceased},\
        Tested = {self.tested},\
        Vaccine Dosses Administered = {self.vaccine_doses}."


if __name__ == '__main__':
    model = CovidModel(
        state_name="delhi".title(),
        confirmed=109109,
        active=90,
        recovered=9090,
        deceased=78,
        tested=18208,
        vaccine_doses=90989
    )
    print(model.__repr__())