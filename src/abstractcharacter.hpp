#include <string>

#include "abstractappliance.hpp"

class AbstractCharacter
{
public:
    AbstractCharacter();
    ~AbstractCharacter();

    virtual bool createCharacter(std::string name) = 0;

    virtual int timeToInstall() = 0;
    virtual int driveTo(std::string nextDestination) = 0;

    // TODO define some superpower
    virtual bool specialPower() = 0;

protected:
    std::string name_m;
    int competenceLevel_m;
    int age_m;
    std::string hairColor_m;
};
