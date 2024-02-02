#include<string>

class AbstractApplicance
{
public:
    AbstractApplicance();
    ~AbstractApplicance();

    enum :uint8_t
    {
        BOILER = 0,
        HP,
        VED,
        VR42
    }ApplianceType;

protected:
    std::string applicanceName_m;
    bool isOTAUpossible_m;
    AbstractApplicance::ApplianceType applianceType_m;
};