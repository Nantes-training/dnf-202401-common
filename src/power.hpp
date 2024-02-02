#include <string>

class Power
{
public:
    Power();
    Power(int strength, std::string name);
    ~Power();
    
private:
    int powerStrength_m;
    std::string powerName_m;
};

