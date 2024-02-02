#include "power.hpp"

Power::Power()
    : powerName_m("Nothing"), powerStrength_m(0)
{
}

Power::Power(int strength, std::string name)
    : powerName_m(name), powerStrength_m(strength)
{}

Power::~Power()
{
}
